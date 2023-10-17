from django.db.models import Model, ForeignKey, CharField, DO_NOTHING
from django.db import models
from django.contrib.auth.models import User


class Channel(Model):
    name = CharField(max_length=100)
    description = CharField(max_length=1000)
    created_by_user = ForeignKey(User, on_delete=DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Message(Model):
    from_user = ForeignKey(User, on_delete=DO_NOTHING, null=True)
    channel = ForeignKey(Channel, on_delete=DO_NOTHING, null=True)
    content = CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"{self.channel.name}: {self.from_user.username}: {self.content[:100]}"
        )
