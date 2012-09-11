from django_ical.views import ICalFeed
from intranet.models import Event

class EventFeed(ICalFeed):
    """
    A simple event calender
    """
    product_id = '-//Apple Inc.//iCal 5.0.3//EN'
    timezone = 'America/Chicago'
    title = "ACM@UIUC Calendar"
    description = "All the events happening at ACM and in the CS department"

    def items(self):
        return Event.objects.all().order_by('-starttime')

    def item_guid(self,item):
        return "acm.uiuc.edu:%d"%(item.id)

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        description_out = item.description.replace('\n'," ")
        return description_out

    def item_start_datetime(self, item):
        return item.starttime

    def item_end_datetime(self, item):
        return item.endtime

    def item_location(self, item):
        return item.location

    def item_link(self, item):
        return "http://www.acm.uiuc.edu/calendar/details/%d/"%(item.id)