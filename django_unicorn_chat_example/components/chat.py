from django_unicorn.components import UnicornView

from ..models import Message


class ChatView(UnicornView):
    channel_pk: int = 1
    user_pk: int = 1
    messages = Message.objects.none()

    def add(self, message: str):
        Message.objects.create(
            channel_id=self.channel_pk,
            from_user_id=self.request.user.pk,
            content=message,
        )
        self.get_messages()

    def get_messages(self):
        self.messages = Message.objects.filter(channel=self.channel_pk)

    def mount(self):
        self.get_messages()
