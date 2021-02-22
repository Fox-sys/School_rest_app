from django.urls import path
from .apiviews import ChatListView, ChatDetailView, MessageListView, \
                      MessageDetailView, MessageCreateView, MesssageUpdateView, \
                      MesssageDeleteView

urlpatterns = [
    path('chats/', ChatListView.as_view(), name='chat_list'),
    path('chats/<int:pk>', ChatDetailView.as_view(), name='current_chat'),
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/create', MessageCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>', MessageDetailView.as_view(), name='current_message'),
    path('messages/<int:pk>/delete', MesssageDeleteView.as_view(), name='delete_message'),
    path('messages/<int:pk>/update', MesssageUpdateView.as_view(), name='update_message'),
]