import random
import string

from django.db import models

# Create your models here.
class ShortLinks(models.Model):
	full_link = models.URLField(max_length=256)
	short_link = models.CharField(max_length=6)

	def __str__(self):
		return f"/{self.id}/{self.short_link}/{self.full_link}"

	__repr__ = __str__

	def save(self, *args, **kwargs):
		self.short_link = self.get_random_string()
		super(self.__class__, self).save(*args, **kwargs)

	@staticmethod
	def get_random_string(max_length: int=6) -> str:
		letters = list(string.ascii_letters + string.digits)
		random.shuffle(letters)
		return ''.join(random.sample(letters, 6))