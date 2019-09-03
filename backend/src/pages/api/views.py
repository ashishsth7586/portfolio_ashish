from rest_framework import generics
from ..models import Landing, About, SocialMedia, Quote, Testimonial, Service
from .serializers import LandingSerializer, AboutSerializer, SocialMediaSerializer, QuotesSerializer, ServicesSerializer, TestimonialsSerializer
from rest_framework.permissions import IsAuthenticated


class LandingList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Landing.objects.all()
    serializer_class = LandingSerializer


class AboutList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class SocialMediaList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


class QuotesList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Quote.objects.all()
    serializer_class = QuotesSerializer


class ServicesList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer


class TestimonialsList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialsSerializer
