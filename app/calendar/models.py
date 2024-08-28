from utils.models import BaseModel


class RegularEvent(BaseModel):
    url = '/api/regular-event/'

    def events(self, start=None, end=None):
        return Event.get_objects(regular_event=self.id)


class Event(BaseModel):
    url = '/api/event/'


