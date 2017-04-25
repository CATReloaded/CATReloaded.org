from django.views.generic import TemplateView

from .models import Session, Speaker


class ScopeIndex(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(ScopeIndex, self).get_context_data(**kwargs)
        speakers = Speaker.objects.all()
        day_one_sessions = Session.objects.filter(date_time__day=29)
        day_two_sessions = Session.objects.filter(date_time__day=30)
        context['speakers'] = speakers
        context['day_one'] = day_one_sessions
        context['day_two'] = day_two_sessions
        return context
