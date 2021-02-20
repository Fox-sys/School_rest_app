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
- MesssageDetailUpdateDeleteView
- MessageCreateView

## ChatListView:
View for getting list of chats

### Filters: 
name (string)
user (id of user)

## ChatDetailView:
View for getting current chat

## MessageListView:
View for getting list of messages

### Filters: 
chat (id of chat)
replies_to (id of message)

## MessageListView:
View for creating messages

## MesssageDetailUpdateDeleteView:
View for getting updating and deleting current message

# Entry Points:
- 'chats' - ChatListView
- 'chats/{pk}' - ChatDetailView
- 'messages' - MessageListView
- 'messages/{pk}' - MesssageDetailUpdateDeleteView
- 'messages/create' - MessageCreateView

# permissions:
- CanUseMessage (you can read, change, delete message)
- UserIsInChat (Checks if you are in chat)