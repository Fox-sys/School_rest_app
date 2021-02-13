from django.urls import path
from .apiviews import ChatListView, ChatDetailView

urlpatterns = [
    path('chats/', ChatListView.as_view(), name='chat_list'),
    path('chats/<int:pk>', ChatDetailView.as_view(), name='current_chat')
]