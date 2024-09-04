from dataclasses import dataclass
from datetime import datetime
from typing import List

from utils.models import BaseModel, apply_default_filters


@dataclass
class Event(BaseModel):
    url = '/api/event/'

    start: datetime
    end: datetime
    title: dict
    sub_tasks: list
    regular_event: int

    @property
    def duration(self):
        return self.end - self.start if self.end else (max(datetime.utcnow().astimezone(), self.start) - self.start)

    @property
    def duration_seconds(self):
        return self.duration.total_seconds()


@dataclass
class PlannedEvent(BaseModel):
    url = '/api/event-planned/'

    planned: bool
    plane_type: str
    title: dict
    description: str
    event_planned_timer: list
    sub_tasks: list


@dataclass
class RegularEvent(BaseModel):
    url = '/api/regular-event/'

    name: dict
    weekdays: list
    public: bool
    delayed_start_at: bool
    started_at: datetime
    max_duration: int
    duration_required: bool

    @apply_default_filters('-start')
    def events(self, start=None, end=None, start_lte=None, end_lte=None, start_gte=None, end_gte=None, **kwargs) -> List[Event]:
        return Event.get_objects(regular_event=self.id, start_gte=start_gte)

    def planned_events(self, start_gte=None, end_gte=None, **kwargs):
        return PlannedEvent.get_objects(regular_event=self.id, start_gte=start_gte)

#
#
# pipeline {
#   agent {
#       docker {
#           image 'mycalendar/jenkins_agent'
#           args  '--net="new_v2_calendar"'
#       }
#   }
#   stages {
#     stage('HelloWorld') {
#       steps {
#         echo 'Hello World'
#       }
#     }
#     stage('git clone') {
#       steps {
#          cleanWs()
#          script {
#              img = 'mycalendar/handler'
#              sh 'curl web:8000'
#              sh 'git clone https://github.com/lolvalolee/calendar_scripts.git'
#              withEnv(["TOKEN=$jwt_token"]){
#                      dir('./calendar_scripts') {
#                          sh 'git checkout user_${user_id}'
#                          sh 'touch /tmp/dump.txt'
#                          sh 'tcpdump -v > /tmp/dump.txt &'
#                          sh 'python ${handler_name}'
#                          sh 'cat /tmp/dump.txt'
#                          sh 'echo ----------------'
#                          sh 'echo ----------------'
#                          sh 'echo ----------------'
#                          sh 'echo ----------------'
#                          sh 'wc -l < /tmp/dump.txt'
#                 }
#              }
#          }
#       }
#     }
#   }
# }