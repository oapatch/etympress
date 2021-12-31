from django.shortcuts import render
from django.views.generic.base import TemplateView, ContextMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from war.models import Weekday, Repetition, Month
from post.models import Entry


class TodaysContextMixin(ContextMixin):
    """adds today's context data for each view """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weekday'] = Weekday(Weekday.today()).label
        context['repetition'] = Repetition(Repetition.today()).label
        context['month'] = Month(Month.today()).label
        return context


class Write(TodaysContextMixin, CreateView):
    """Write page for submitted a journal entry """
    # old journal of a plague year code
    model = Entry
    fields = ['entry']
    template_name = 'write.html'
    success_url = reverse_lazy('today')



class Today(TodaysContextMixin, ListView):
    """ Today page for viewing today's journal entries """
    model = Entry
    context_object_name = 'entries'
    queryset = Entry.objects.filter(weekday=Weekday.today()
            ).filter(repetition=Repetition.today()
            ).filter(repetition=Month.today()
            ).order_by('-pk')
    template_name = 'today.html'


class Downtime(Write):
    template_name = 'downtime.html'


class Jade(TodaysContextMixin, TemplateView):
    # Ok this is a """"Lore""""" reference, maybe this "The War's Head Inn"
    # play will have some weird references to, idk, actual metafiction, as well
    # as having contemporary real-world applications in distributed politics
    # community world-working!!! # TODO edit for...clarity.....and
    # professionalism...
    template_name = 'war.html'
    name = 'jade'


class WarInn(TodaysContextMixin, TemplateView):
    template_name = 'inn.html'
    name = 'inn'
    model = Entry
    context_object_name = 'parafederalist'
    queryset = Entry.objects.filter(category='parafederalist').order_by('-pk')
    # Ok this should be a ListView!!! 
    # Also, should have more than just the parafederalist entries!!! But that's
    # a start!!!!


class WarPost(TodaysContextMixin, TemplateView):
    """ Posts! Blogs! Para-federalist papers in the milleu of the Federalist
    Paper quasi-blog of the Confederacy->Federal transition!! Organizational
    memos and distributed strategic advice across districts! # TODO
    contributions welcome, email ber@etympress.com ! """
    template_name = 'board.html'
    name = 'board'


class WarEntrance(TodaysContextMixin, TemplateView):
    """ A rate-flowing algorithm ! or idk smthng """
    template_name = 'entrance.html'
    name = 'entrance'

