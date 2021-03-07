from django.urls import path
from .views import (
    stories_view,
    popular_stories_view,
    best_stories_view,
    featured_stories_view,
    stories_view,
    story_view
)

urlpatterns = [
    path('',stories_view,name="stories"),
    path('popular',popular_stories_view,name="popular_stories"),
    path('best',best_stories_view,name="best_stories"),
    path('featured',featured_stories_view,name="featured_stories"),
    path('<int:story_id>',story_view,name="story")
]