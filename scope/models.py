from django.db import models


class Speaker(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    title = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="speakers/")

    def __str__(self):
        return "Speaker {}: {}".format(self.id, self.name)


class Session(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    speaker = models.ForeignKey(Speaker, related_name='sessions')
    date_time = models.DateTimeField()

    def __str__(self):
        return "Session {}: {}".format(self.id, self.title)
