from django.urls import path, include
from .views import LandingList, AboutList, SocialMediaList, QuotesList, ServicesList, TestimonialsList

urlpatterns = [
    path('banner/', LandingList.as_view()),
    path('about/', AboutList.as_view()),
    path('social/', SocialMediaList.as_view()),
    path('quotes/', QuotesList.as_view()),
    path('services/', ServicesList.as_view()),
    path('testimonials/', TestimonialsList.as_view()),
]