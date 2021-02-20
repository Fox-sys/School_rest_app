# Diary Service
This service made for realizing diary system

# Models:

- Subject
- Group
- Homework

## Subject:

### Required fields: 

- name (Char Field) max length = 150 chars
- description (Text Field)

### Optional fields:

teacher (Many To Many Field depends on profile_service.Teacher)

### str method: 

returns subject name

## Group:

### Required fields: 

- name (Char Field) max lenght = 150 chars
- subjects (Many To Many Field depends on diary_service.Subject) 

### Optional fields:

- students (Many To Many Field depends on profile_service.Student)
- curator (ForeignKey depends on profile_service.Teacher) on delete: set null
- homework (Many To Many Field depends on diary_service.Homework)

### str method: 

returns group name

## Homework:

### Required fields: 

- short_desc (Char Field) max lenght = 150 chars
- end_date (Date Field) 
- score (Char Field) choices: 10, 20, 30, 40 
- subject (ForeignKey depends on diary_service.Subject) on delete: delete Homework

### Optional fields:

- full_desc (Text Field)
- teacher (ForeignKey depends on profile_service.Teacher) on delete: set null
- start_date (Date Field) auto_now setting is True
- pins (File Field) default location: /media/homework/

### str method: 

returns subject name and short_desc
 
# Serializers:

- SubjectSerializer
- GroupSerializer
- HomeworkSerializer
- HomeworkUpdateSerializer
- HomeworkCreateSerializer

## SubjectSerializer:

### Model: 
diary_service.Subject

### Fields:
id, teacher, name, description

## GroupSerializer:

### Model: 
diary_service.Group

### Fields:
id, name, students, curator, subjects, homework

### Read Only Fields:
name, students, curator, subjects

## HomeworkSerializer:

### Model: 
diary_service.Homework

### Fields:
id, short_desc, full_desc, teacher, start_date, end_date, pins, score, subject

### Overrided Fields:
score (returns choice display)

## HomeworkUpdateSerializer:

### Model: 
diary_service.Homework

### Fields:
id, short_desc, full_desc, end_date, pins, score

## HomeworkCreateSerializer:

### Model: 
diary_service.Homework

### Fields:
id, short_desc, full_desc, end_date, pins, score, teacher, subject

# Views:

- GroupListView
- GroupUpdateDetailView
- HomeworkListView
- HomeworkCreateView
- HomeworkDetailView
- HomeworkUpdateView
- SubjectListView
- SubjectDetailView
- HomeworkDestroyView

## GroupListView:
View for getting list of groups

### Filters: 
subject (id of subject)

### Permissions:
IsAuthenticated

## GroupUpdateDetailView:
View for getting and updating current group

### Permissions:
IsATeacher

## HomeworkListView:
View for getting list of homework

### Permissions:
IsATeacher or UserIsInGroup

### Filters: 
start_date (date)
end_date (date)
teacher (id of teacher)
group (id of group)

## HomeworkDetailView:
View for getting current homework

### Permissions:
IsATeacher or UserIsInGroup

## HomeworkUpdateView:
View for updating homework

### Permissions:
IsATeacher

## HomeworkDestroyView:
View for destroing homework

### Permissions:
IsATeacher

## HomeworkCreateView:
View for creating new homework 

### Permissions:
IsATeacher

## SubjectListView:
View for getting list of subjects

### Permissions:
AllowAny

### Filters: 
teacher (id of teacher)
group (id of group)

## SubjectDetailView:
View for getting current subject

### Permissions:
AllowAny

# Entry Points:
- 'groups' - GroupListView
- 'groups/{pk}' - GroupUpdateDetailView
- 'homework' - HomeworkListView
- 'homework/create' - HomeworkCreateView
- 'homework/{pk}' - HomeworkDetailDestroyView
- 'homework/{pk}/update' - HomeworkUpdateView
- 'homework/{pk}/destroy' - HomeworkDestroyView
- 'subjects' - SubjectListView
- 'subjects/{pk}' - SubjectDetailView

# Permissions:
IsATeacher (Checks if user is a teacher)
UserIsInGroup (Checks if user is in a group)