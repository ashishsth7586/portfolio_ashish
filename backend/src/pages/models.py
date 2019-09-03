from django.db import models


class SocialMedia(models.Model):
    facebook = models.CharField(max_length=50, default="https://facebook.com")
    twitter = models.CharField(max_length=50, default="https://www.twitter.com")
    instagram = models.CharField(max_length=50, default="https://www.instagram.com")
    github_link = models.CharField(max_length=50, default="https://www.github.com")
    linkedin = models.CharField(max_length=50, default="https://linkedin.com")

    class Meta:
        verbose_name = 'Social Media Link'
        verbose_name_plural = 'Social Media Links'

    def __str__(self):
        return "Social Media Links"


class Landing(models.Model):
    site_name = models.CharField(max_length=30, default="Portfolio")
    introduction = models.CharField(max_length=150, default="Hello, It's Name Surname")
    who_you_are = models.CharField(max_length=20, default="I'm ")
    first_skill = models.CharField(max_length=30, default="a Developer.")
    second_skill = models.CharField(max_length=30, default="an Electronics Engineer.")
    third_skill = models.CharField(max_length=30, default="a Freelancer.")
    fourth_skill = models.CharField(max_length=30, default="optional field", blank=True, null=True)
    short_description = models.TextField(default="It is a long orem ipsum", null=True)
    button_text = models.CharField(max_length=15, default="Hire Me Now!")

    banner_image = models.ImageField(upload_to='images/banner', null=True)

    class Meta:
        verbose_name = 'Landing'
        verbose_name_plural = 'Landing Pages'

    def __str__(self):
        return self.site_name + "'s Landing Page"


class About(models.Model):
    page_title = models.CharField(max_length=20, default="About")

    # Personal Details
    detail_heading = models.CharField(max_length=20, default="Peronal Details")
    short_detail = models.TextField(default="Lorem Ipsum is simply or ceturies.")
    name = models.CharField(max_length=30, default="Ashish Shrestha")
    email = models.EmailField()
    phone = models.BigIntegerField()
    location = models.CharField(max_length=100, default="Kaushaltar, Bhaktapur")

    # Skills
    skill_heading = models.CharField(max_length=25, default="My Skills")
    skill_one = models.CharField(max_length=25, default="Python")
    skill_one_level = models.IntegerField(default="80")
    skill_two = models.CharField(max_length=25, default="React & Redux")
    skill_two_level = models.IntegerField(default="80")
    skill_three = models.CharField(max_length=25, default="Embedded System Design")
    skill_three_level = models.IntegerField(default="80")
    skill_four = models.CharField(max_length=25, default="Machine Learning")
    skill_four_level = models.IntegerField(default="80")

    # Interests
    interest_one_title = models.CharField(max_length=20, default="Research")
    interest_one_detail = models.TextField()
    interest_two_title = models.CharField(max_length=20, default="Design")
    interest_two_detail = models.TextField()
    interest_three_title = models.CharField(max_length=20, default="Development")
    interest_three_detail = models.TextField()

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About Pages'

    def __str__(self):
        return self.page_title + ' ' + self.name


class Quote(models.Model):
    author_name= models.CharField(max_length=50, default="Steve Jobs")
    quotes = models.TextField(default="Design is not just what it looks like and feels like. Design is how it works")

    class Meta:
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'

    def __str__(self):
        return self.author_name + "'s Quote"


class Service(models.Model):
    svg_icon = models.FileField(upload_to="images/services/icon", null=True, blank=True)
    service_name = models.CharField(max_length=20, default="Web Design")
    service_description = models.CharField(max_length=180, default="Lorem ipsum is simply dummy")

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service_name


class Testimonial(models.Model):
    name = models.CharField(max_length=50, default="Omar Hampton")
    designation = models.CharField(max_length=50, default="Chief Executive Officer")
    company = models.CharField(max_length=50, default="Metrotarkari Pvt Ltd", blank=True)
    message = models.TextField()
    image = models.ImageField(upload_to='images/testimonials', null=True, blank=True)

    class Meta:
        verbose_name = 'testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.name

