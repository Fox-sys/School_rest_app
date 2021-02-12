from django.urls import path, include

urlpatterns = [
    path("comms/", include('comm_service.urls')),
    path("diary/", include('diary_service.urls')),
    path("news/", include('news_service.urls')),
    path("profile/", include('profile_service.urls')),
    path("report/", include('report_service.urls')),
]
