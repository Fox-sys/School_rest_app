# Profile Service
This service made for realizing profile system

# Models:

- MainUser
- Teacher
- Student

## MainUser:

### Required fields: 

- middle_name (Char Field) max length = 150 chars
- phone (Char Field) max_length = 13
- and abstract user field (find it in django docs)

### Optional fields:

- chats (Many To Many Field depends on comm_service.Chat)
- and abstract user field (find it in django docs)

### str method: 

returns username, last_name, first_name and middle_name

## Teacher:

### Required fields: 

- user (ForeignKey depends on profile_service.MainUser) on delete: delete Teacher
- photo (File Field) default location: /media/teacher_photos/
- info (Text Field)
- subjects (Many To Many Field depends on diary_service.Subject)

### Optional fields:

- is_group_curator (Boolean Field) default is False
- is_chat_curator (Boolean Field) default is False
- curated_group (ForeignKey depends on diary_service.Group) on delete: set null
- curated_chat (ForeignKey depends on comm_service.Chat) on delete: set null

### str method: 

returns username, last_name, first_name and middle_name

## Student:

### Required fields: 

- user (ForeignKey depends on profile_service.MainUser) on delete: delete Student

### Optional fields:

- group (ForeignKey depends on diary_service.Group) on delete: set null
- stats (Many To Many Field depends on report_service.StatElement)

### str method: 

returns username, last_name, first_name and middle_name
 
# Serializers:

- MainUserSerializer
- StudentSerializer
- TeacherSerializer

## MainUserSerializer:

### Model: 
profile_service.MainUser

### Fields:
id, username, last_name, first_name, middle_name, email, phone, chats, is_staff, is_active

## StudentSerializer:

### Model: 
profile_service.Student

### Fields:
id, user, group, stats

### Read Only Fields:
user, group

## TeacherSerializer:

### Model: 
profile_service.Teacher

### Fields:
id, user, is_group_curator, is_chat_curator, curated_group, curated_chat, photo, info, subjects

# Views:

- StudentListView
- StudentDetailUpdateView
- MainUserDetailView
- TeacherListView
- TeacherDetailView

## StudentListView:
View for getting list of students

### Filters: 
group (group id)

## StudentDetailUpdateView:
View for getting and updating current student

## MainUserDetailView:
View for getting current MainUser

## TeacherListView:
View for getting list of teachers

### Filters: 
is_group_curator (Boolean (1, 0, True, False))
is_chat_curator (Boolean (1, 0, True, False))

## TeacherDetailView:
View for getting current teacher

# Entry Points:
- 'students' - StudentListView
- 'students/{pk}' - StudentDetailUpdateView
- 'teachers' - TeacherListView
- 'teachers/{pk}' - TeacherDetailView
- 'users/{pk}' - MainUserDetailView
