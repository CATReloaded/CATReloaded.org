from django.db import models


class Speaker(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    title = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=200, null=True, editable=False)
    social = models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return "Speaker {}: {}".format(self.id, self.name)


class Session(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    speaker = models.ForeignKey(Speaker, related_name='sessions', null=True, blank=True)
    date_time = models.DateTimeField()

    class Meta:
        ordering = ('date_time',)

    def __str__(self):
        return "Session {}: {}".format(self.id, self.title)
