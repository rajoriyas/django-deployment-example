from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator

# See alternative in forms.py
"""
class OptinalSchemeURLValidator(URLValidator):
    def __call__(self, value):
        if '://' not in value:
            value = 'http://'+value
        super(OptinalSchemeURLValidator, self).__call__(value)
"""

class UserProfileInfoModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional
    
    #portfolio_site = models.URLField(blank=True, validators=[OptinalSchemeURLValidator,])
    portfolio_site = models.URLField(blank=True)
    #profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    profile_pic = models.FileField(upload_to='profile_pics', blank=True)
    def __str__(self):
        return self.user.username
