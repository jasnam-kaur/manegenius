from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # We are adding these fields to the default Django user
    enrollment_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    course_and_shift = models.CharField(max_length=100, blank=True, null=True)
    college = models.CharField(max_length=150, blank=True, null=True)

    # Standard Django fields we already have from AbstractUser:
    # - username
    # - first_name
    # - last_name
    # - email
    # - password (hashed)
    
    def __str__(self):
        # This controls how the user is listed in the Admin panel
        return f"{self.email} ({self.enrollment_number})"