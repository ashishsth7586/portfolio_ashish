from ..models import Landing, About, SocialMedia, Quote, Testimonial, Service
from rest_framework import serializers


class LandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landing
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'


class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'
