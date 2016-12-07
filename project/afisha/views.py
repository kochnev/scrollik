from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Event, Comment

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'afisha/index.html'
    context_object_name = 'latest_event_list'

    def get_queryset(self):
        """
        Return only checked events
        """
        return Event.objects.filter(is_checked=True).order_by('-start_date')[:3]

class DetailView(generic.DetailView):
    model = Event
    template_name = 'afisha/detail.html'

def add_comment(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    inputed_comment = request.POST['comment']
    if inputed_comment == '':
        # Redisplay the question voting form.
        return render(request, 'afisha/detail.html', {
            'event': event,
            'error_message': "You didn't input a comment.",
        })
    else:
        c = event.comment_set.create(comment_text=inputed_comment, pub_date = timezone.now())
        c.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('afisha:detail', args=(event.id,)))
