# News Service
This service made for realizing diary system

# Models:

 - News

## News:

### Required fields: 

- news_type (Char Field) choices: replacement (rp), new (nw), announcement (an)
- title (Char field) max_length=150
- info (Text Field)

### Optional fields:

- subject_from (ForeignKey depends on diary_service.Subject) should be filled only when news_type is replacement
- subject_to (ForeignKey depends on diary_service.Subject) should be filled only when news_type is replacement

### str method: 

returns news type and title

# Serializers:

- NewsSerializer
- NewsUpdateCreateSerializer

## NewsSerializer:

### Model: 
news_service.News

### Fields:
id, news_type, title, info, subject_from, subject_to

### Overrided Fields:
news_type (returns choice display)

## NewsUpdateCreateSerializer:
if news_type is replacement subject_from and subject_to should be filled

### Model: 
news_service.News

### Fields:
id, news_type, title, info, subject_from, subject_to

# Views:

- NewsListView
- NewsCreateView
- NewsUpdateView
- NewsDetailDeleteView

## NewsListView:
View for getting list of news

### Filters: 
news_type (short choice form)
subject_from (id of subject)
subject_to (id of subject))

## NewsCreateView:
View for creating news

## NewsUpdateView:
View for for updating current news

## NewsDetailDeleteView:
View for getting and deleting current news

# Entry Points:
'' - NewsListView
'{pk}' - NewsDetailDeleteView
'{pk}/update' - NewsUpdateView
'create' - NewsCreateView
