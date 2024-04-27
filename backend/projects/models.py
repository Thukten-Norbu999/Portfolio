from django.db import models
import uuid
from user.models import User

# Create your models here.
class Project(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    name = models.CharField(verbose_name="Project Name", max_length=150)
    client = models.CharField(verbose_name="Client", max_length=150)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Uploader")
    testimonial = models.TextField(max_length=250)


