from django.db import models

permission_choices = [
    ('a', 'admin'),
    ('u', 'user'),
    ('s', 'shoper'),
]

class User(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    permission = models.CharField(max_length=1, choices=permission_choices, null=True)
    description = models.TextField()

    def __str__(self):
        return f"User | {self.user_name}"
