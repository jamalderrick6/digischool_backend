from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User
from django.db.models.indexes import Index

from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print(instance.__dict__)
    # instance.profile.save(using="auth_db")


class Profile(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    image = models.TextField(blank=True, null=True)
    login_count = models.IntegerField(default=0)
    prior_experience = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id


class Course(models.Model):
    name = models.CharField(max_length=50, blank=False, db_index=True)
    headline = models.TextField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    icon = models.TextField(blank=True)
    level = models.ForeignKey('Level', on_delete=models.PROTECT, db_index=True)
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], default=0)

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.TextField(max_length=20, db_index=True, blank=False)

    def __str__(self):
        return self.name


class Price(models.Model):
    name = models.CharField(max_length=50, blank=False)
    age_range = models.ForeignKey(
        'YearRange', on_delete=models.PROTECT, db_index=True)
    amount = models.IntegerField(default=0000, blank=False)
    features = models.ManyToManyField('Feature')

    def __str__(self):
        return self.name


class YearRange(models.Model):
    smallest_age = models.IntegerField(blank=False, default=1)
    highest_age = models.IntegerField(blank=False, default=1)
    range = models.CharField(max_length=50, default='8 - 9 years')

    def save(self):
        self.range = "{} - {} years".format(self.smallest_age,
                                            self.highest_age)
        return super(YearRange, self).save()

    def __str__(self):
        return self.range


class Feature(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
