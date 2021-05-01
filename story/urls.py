from django.urls import path
from .views import (
    stories_view,
    popular_stories_view,
    best_stories_view,
    featured_stories_view,
    stories_view,
    story_view,
    post_story_view,
    edit_story_view,
    delete_story_view,
    add_comment_view
)

urlpatterns = [
    path('',stories_view,name="stories"),
    path('popular',popular_stories_view,name="popular_stories"),
    path('best',best_stories_view,name="best_stories"),
    path('featured',featured_stories_view,name="featured_stories"),
    path('<int:story_id>',story_view,name="story"),
    path('post',post_story_view,name="post_story"),
    path('<int:story_id>/edit',edit_story_view,name="edit_story"),
    path('<int:story_id>/delete',delete_story_view,name="delete_story"),
    path('<int:story_id>/comment/add',add_comment_view,name="add_comment"),
]