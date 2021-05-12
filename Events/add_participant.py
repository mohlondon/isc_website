import pandas as pd
from events.models import Participant, Event
from Users.models import CustomUser
from django.contrib.auth.hashers import make_password


class adding_Participant():
    def __init__(self, file):
        self.defaultPass = make_password("admin")
        self.ParticipantList = pd.read_csv(file)

    def check_Customer(self, email):
        try:
            CustomUser.objects.get(email=email)
            print('cust exist')
            return False
        except CustomUser.DoesNotExist:
            return True

    def check_Participation(self, part, event):
        try:
            Participant.objects.get(participant=part, Event=event)
            print('part exist')
            return False
        except Participant.DoesNotExist:
            return True

    def add_Participant(self, title,group):
        for index, row in self.ParticipantList.iterrows():
            if self.check_Customer(row['email']):
                CustomUser.objects.create(
                    username=row['fullname'], email=row['email'], password=self.defaultPass)
            part = CustomUser.objects.get(email=row['email'])
            event = Event.objects.get(title=title)
            if self.check_Participation(part, event):
                Participant.objects.create(participant=part,group=group, Event=event)
