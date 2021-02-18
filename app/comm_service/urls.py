from django.urls import path
from .apiviews import ChatListView, ChatDetailView, MessageListView, \
                      MesssageDetailUpdateDeleteView, MessageCreateView

urlpatterns = [
    path('chats/', ChatListView.as_view(), name='chat_list'),
    path('chats/<int:pk>', ChatDetailView.as_view(), name='current_chat'),
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/create', MessageCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>', MesssageDetailUpdateDeleteView.as_view(), name='current_message'),
]