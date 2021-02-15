# Communication Service
This service made for providing communications (chats and messages)

# Models:

1) Chat
2) Message

## Chat:

### Required fields: 

Name (Char Field) max length = 150 chars

### Optional fields:

1) members (Many to Many Field depends on profile_service.MainUser) 
2) curator (Many to Many Field depends on profile_service.Teacher)
3) is_curated (Boolean Field) default is True
4) messages (Many to Many Field depends on comm_service.Message)

### str method: 

returns chat name

## Message:

### Required fields: 

1) author (ForeignKey depends on profile_service.MainUser) on delete: delete message
2) text (Char Field) max lenght = 2000 chars

### Optional fields:

1) replies_to (ForeignKey depends on comm_service.Message)
2) pins (File Field) default upload folder: /media/Message_files/
3) date (Date Time Field) auto_now setting is True
4) is_edited (Boolean Field) default is False

### str method: 

no str method

# Serializers:

1) ChatSerializer
2) MessageSerializer

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

1) ChatListView
2) ChatDetailUpdateView
3) MessageListCreateView
4) MesssageDetailUpdateDeleteView

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