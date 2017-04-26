from django.views.generic import TemplateView
from django.conf import settings

from .models import Session, Speaker


def add_image_url(speaker):
    url = "{}speakers/{}.jpg"
    speaker.image = url.format(settings.STATIC_URL, speaker.name)
    speaker.save()
    return speaker

class ScopeIndex(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(ScopeIndex, self).get_context_data(**kwargs)
        speakers = [add_image_url(speaker) for speaker in Speaker.objects.all()]
        day_one_sessions = Session.objects.filter(date_time__day=29)
        day_two_sessions = Session.objects.filter(date_time__day=30)
        context['speakers'] = speakers
        context['day_one'] = day_one_sessions
        context['day_two'] = day_two_sessions
        print(context)
        return context
