from django.views.generic import TemplateView

from fest_list.models import Fest

class FestList(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(FestList, self).get_context_data(**kwargs)

        context['fest_list'] = Fest.objects.all()
        return context
