from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=255, default='User')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_ai = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"[{self.timestamp}] {self.sender}: {self.text[:50]}"
