from django.urls import path
from .views import (
    user_profile_view,
    edit_user_profile_view,
    notifikasi_view
)

urlpatterns = [
    path('notifikasi',notifikasi_view,name="notifikasi"),
    path('<str:username>/profile',user_profile_view,name="user_profile"),
    path('<str:username>/profile/edit',edit_user_profile_view,name="edit_user_profile"),
]