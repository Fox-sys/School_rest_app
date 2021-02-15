# Diary Service
This service made for realizing diary system

# Models:

1) Subject
2) Group
3) Homework

## Subject:

### Required fields: 

1) name (Char Field) max length = 150 chars
2) description (Text Field)

### Optional fields:

teacher (Many To Many Field depends on profile_service.Teacher)

### str method: 

returns subject name

## Group:

### Required fields: 

1) name (Char Field) max lenght = 150 chars
2) subjects (Many To Many Field depends on diary_service.Subject) 

### Optional fields:

1) students (Many To Many Field depends on profile_service.Student)
2) curator (ForeignKey depends on profile_service.Teacher) on delete: set null
3) homework (Many To Many Field depends on diary_service.Homework)

### str method: 

returns group name

## Homework:

### Required fields: 

1) short_desc (Char Field) max lenght = 150 chars
2) end_date (Date Field) 
3) score (Char Field) choices: 10, 20, 30, 40 
4) subject (ForeignKey depends on diary_service.Subject) on delete: delete Homework

### Optional fields:

1) full_desc (Text Field)
2) teacher (ForeignKey depends on profile_service.Teacher) on delete: set null
3) start_date (Date Field) auto_now setting is True
4) pins (File Field) default location: /media/homework/

### str method: 

returns subject name and short_desc
 
# Serializers:

1) SubjectSerializer
2) GroupSerializer
3) HomeworkSerializer
4) HomeworkUpdateSerializer

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
id, short_desc, full_desc, teacher, start_date, end_date, pins, score, subject

# Views:

1) GroupListView
2) GroupUpdateDetailView
3) HomeworkListCreateView
4) HomeworkDetailView
5) HomeworkUpdateView
6) SubjectListView
7) SubjectDetailView

## GroupListView:
View for getting list of groups

### Filters: 
subject (id of subject)

## GroupUpdateDetailView:
View for getting and updating current group

## HomeworkListCreateView:
View for getting list of homework and creating homework

### Filters: 
start_date (date)
end_date (date)
teacher (id of teacher)
group (id of group)

## HomeworkDetailView:
View for getting current homework

## HomeworkUpdateView:
View for updating homework

## SubjectListView:
View for getting list of subjects

### Filters: 
teacher (id of teacher)
group (id of group)

## SubjectDetailView:
View for getting current subject