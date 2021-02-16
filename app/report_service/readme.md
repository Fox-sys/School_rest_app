# Report Service
This service made for realizing report system

# Models:

 - StatElement

## StatElement:

### Required fields: 

- element (Char Field) choices: absenteeism (1), serious reason (2), late (3), mark 2 (4), mark 3 (5), mark 4 (6), mark 5 (7),
- subject (ForeignKey depends on diary_service.Subject) on delete: delete Stat Element
- student (ForeignKey depends on profile_service.Student) on delete: delete Stat Element
- info (Text Field)

### Optional fields:

- score (Char Field) choices: 10 (1), 20 (2), 30 (3), 40 (4)
- teacher (ForeignKey depends on profile_service.Teacher) on delete: set null

### str method: 

returns student, element, score, subject

# Serializers:

- StatElementUpdateCreateSerializer
- StatElementUpdateCreateSerializer

## NewsSerializer:

### Model: 
report_service.StatElement

### Fields:
id, element, score, subject, student, teacher

### Overrided Fields:
element (returns choice display)
score (returns choice display)

## StatElementUpdateCreateSerializer:

### Model:
report_service.StatElement

### Fields:
id, element, score, subject, student, teacher

# Views:

- StatElementListView
- StatElementDetailDeleteView
- StatElementCreateView
- StatElementUpdateView

## StatElementListView:
View for getting list of stat elememt

### Filters: 
element (short choice form)
score (short choice form)
subject (id of subject)
teacher (id of teacher)
student (id of student)

## StatElementCreateView:
View for creating stat elememt

## StatElementUpdateView:
View for for updating current stat elememt

## StatElementDetailDeleteView:
View for getting and deleting current stat elememt

# Entry Points:
- ' ' - StatElementListView
- {pk} - StatElementDetailDeleteView
- {pk}/update - StatElementUpdateView
- create - StatElementCreateView
