from django.db import models
from hashlib import md5
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from graphql import GraphQLError

class Url(models.Model):
    full_url = models.URLField(unique=True)
    url_hash = models.URLField(unique=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_url

    def clicked(self):
        self.clicks += 1
        self.save()

    def save(self,*args,**kwargs):
        if not self.id:
            self.url_hash = md5(self.full_url.encode()).hexdigest()[:10]
        validate = URLValidator()
        try:
            validate(self.full_url)
        except Exception as e:
            raise GraphQLError('Url Invalid')

        return super().save(*args,**kwargs)
        

