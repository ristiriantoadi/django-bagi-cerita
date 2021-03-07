from django.urls import path
# from .views import (
#     product_detail_view,
#     product_create_view,
#     dynamic_url,
#     delete_data_view,
#     product_list_view
# )

urlpatterns = [
    path('',stories_view,name="stories"),
    path('popular',popular_stories_view,name="popular_stories"),
    path('best',best_stories_view,name="best_stories"),
    path('featured',featured_stories_view,name="featured_stories")
    path('<int:story_id>',story_view,name="story")
]