# Communication Service
This service made for providing communications (chats and messages)

# Models:

- Chat
- Message

## Chat:

### Required fields: 

Name (Char Field) max length = 150 chars

### Optional fields:

- members (Many to Many Field depends on profile_service.MainUser) 
- curator (Many to Many Field depends on profile_service.Teacher)
- is_curated (Boolean Field) default is True
- messages (Many to Many Field depends on comm_service.Message)

### str method: 

returns chat name

## Message:

### Required fields: 

- author (ForeignKey depends on profile_service.MainUser) on delete: delete message
- text (Char Field) max lenght = 2000 chars

### Optional fields:

- replies_to (ForeignKey depends on comm_service.Message)
- pins (File Field) default upload folder: /media/Message_files/
- date (Date Time Field) auto_now setting is True
- is_edited (Boolean Field) default is False

### str method: 

no str method

# Serializers:

- ChatSerializer
- MessageUpdateSerializer
- MessageSerializer
- MessageCreateSerializer

## ChatSerializer:

### Model: 
comm_service.Chat

### Fields:
id, name, members, curator, is_curated, messages

### Read Only Fields:
name, members, curator, is_curated

## MessageUpdateSerializer:

### Model: 
comm_service.Message

### Fields:
id, author, replies_to, text, pins, date, is_edited

### Read Only Fields:
author, date, is_edited

## MessageSerializer:

### Model: 
comm_service.Message

### Fields:
id, author, date

## MessageCreateSerializer:

### Model: 
comm_service.Message

### Fields:
id, author, replies_to, text, pins, date, chat


# Views:

- ChatListView
- ChatDetailView
- MessageListView
- MessageDetailView
- MesssageDeleteView
- MesssageUpdateView
- MessageCreateView

## ChatListView:
View for getting list of chats

### Filters: 
name (string)
user (id of user)

### Permissions:
AlloyAny

## ChatDetailView:
View for getting current chat

### Permissions:
UserIsInChat

## MessageListView:
View for getting list of messages

### Permissions:
IsAuthenticated

### Filters: 
chat (id of chat)
replies_to (id of message)

## MessageCreateView:
View for creating messages

### Permissions:
IsAuthenticated

## MesssageDetailView:
View for getting current message

### Permissions:
UserIsInChat

## MesssageUpdateView:
View for updating current message

### Permissions:
CanUseMessage

## MesssageDeleteView:
View for deleting current message

### Permissions:
CanUseMessage

# Entry Points:
- 'chats' - ChatListView
- 'chats/{pk}' - ChatDetailView
- 'messages' - MessageListView
- 'messages/{pk}' - MesssageDetailView
- 'messages/{pk}/update' - MesssageUpdateView
- 'messages/{pk}/delete' - MesssageDeleteView
- 'messages/create' - MessageCreateView

# permissions:
- CanUseMessage (you can read, change, delete message)
- UserIsInChat (Checks if you are in chat)