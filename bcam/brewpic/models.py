from django.db import models

def upload_location (instance, filename):
    return "%s" %( filename )

class Images(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(
		upload_to=upload_location,
		null=True,
		blank=True,
		)
