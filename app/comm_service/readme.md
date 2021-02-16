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
- MessageSerializer

## ChatSerializer:

### Model: 
comm_service.Chat

### Fields:
id, name, members, curator, is_curated, messages

### Read Only Fields:
name, members, curator, is_curated

## MessageSerializer:

### Model: 
comm_service.Message

### Fields:
id, author, replies_to, text, pins, date, is_edited

### Read Only Fields:
author, date, is_edited

# Views:

- ChatListView
- ChatDetailUpdateView
- MessageListCreateView
- MesssageDetailUpdateDeleteView

## ChatListView:
View for getting list of chats

### Filters: 
name (string)
user (id of user)

## ChatDetailUpdateView:
View for getting and updating current chat

## MessageListCreateView:
View for getting list of messages and creating message

### Filters: 
chat (id of chat)
replies_to (id of message)

## MesssageDetailUpdateDeleteView:
View for getting updating and deleting current message

# Entry Points:
- 'chats' - ChatListView
- 'chats/{pk}' - ChatDetailUpdateView
- 'messages' - MessageListCreateView
- 'messages/{pk}' - MesssageDetailUpdateDeleteView