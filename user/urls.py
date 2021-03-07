from django.urls import path
from .views import (
    user_profile_view,
    edit_user_profile_view
    # product_detail_view,
    # product_create_view,
    # dynamic_url,
    # delete_data_view,
    # product_list_view
)

urlpatterns = [
    path('<int:user_id>/profile',user_profile_view,name="user_profile"),
    path('<int:user_id>/profile/edit',edit_user_profile_view,name="edit_user_profile"),
]