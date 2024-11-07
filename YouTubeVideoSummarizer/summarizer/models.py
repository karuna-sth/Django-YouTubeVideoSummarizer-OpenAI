from django.db import models

import uuid

# Create your models here.
class Summary(models.Model):

    CONTENT_TYPE_CHOICES = [
        ('blog', 'Blog'),
        ('summary', 'Summary'),
    ]

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255)
    content_type = models.CharField(
        max_length=10,
        choices=CONTENT_TYPE_CHOICES,
        default='summary',  
    )
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.content_type})"

