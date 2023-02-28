from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import random

class User(AbstractUser):

    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    phone = models.CharField(max_length=15)

    def get_absolute_url(self):
       
        return reverse("users:detail", kwargs={"username": self.username})


class Code(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return f"{self.number}"

    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]
        code_items = ''
        for i in range(6):
            num = random.choice(number_list)
            code_items += str(num)
        self.number = code_items
        super().save(*args, **kwargs)
