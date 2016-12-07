from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from .models import Event

class EventMethodTests(TestCase):
    def test_was_published_recently_with_future_event(self):
        """ was_published_recently should return False form
        events whose
            pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_event = Event(title="Test event", pub_date = time)
        self.assertIs(future_event.was_published_recently(), False)

    def test_was_published_recently_with_old_event(self):
        """
        was_published_recently() should return False for events whose
        pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_event = Event(pub_date=time)
        self.assertIs(old_event.was_published_recently(), False)

    def test_was_published_recently_with_recent_event(self):
        """
        was_published_recently() should return True for events whose
        pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_event = Event(pub_date=time)
        self.assertIs(recent_event.was_published_recently(), True)

def create_event(title, days):
    """
    Creates a event with the given `event_text` and published the
    given number of `days` offset to now (negative for events published
    in the past, positive for events that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Event.objects.create(title=title, pub_date=time)

class EventViewTest(TestCase):
    def text_index_view_with_a_checked_events(self):
        """
        Events have to be displayed only if they are checked by administrator
        """
        response = self.client.get(reverse('afisha:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No events are available.")
        self.assertQuerysetEqual(response.context['latest_event_list'], [])
