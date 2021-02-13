from django.urls import path
from .apiviews import ChatListView, ChatDetailUpdateView, MessageListCreateView, \
                      MesssageDetailUpdateDeleteView

urlpatterns = [
    path('chats/', ChatListView.as_view(), name='chat_list'),
    path('chats/<int:pk>', ChatDetailUpdateView.as_view(), name='current_chat'),
    path('messages/', MessageListCreateView.as_view(), name='message_list'),
    path('messages/<int:pk>', MesssageDetailUpdateDeleteView.as_view(), name='current_message'),
]