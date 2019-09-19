from django.db import models

# Create your models here.
class Shows(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    release_date = models.DateField('%m-%d-%Y')
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    def __repr__(self):
        return f"Shows: ({self.id})| Title: {self.title}| Network: {self.network}| Description: {self.description}| Release-Date: {self.release_date}"
