import threading

from .models import *
from faker import Faker
fake = Faker()
import random


class CreateStuendtsThread(threading.Thread):
    
    def __init__(self, total):
        self.total = total
        threading.Thread.__init__(self)

    def run(self):
        try:
            print('Thread execution started')
            for i in range(self.total):
                print(i)
                Student.objects.create(
                    student_name = fake.name(),
                    student_email = fake.email(),
                    address = fake.address(),
                    age = random.randint(10,40)
                )
        except Exception as e:
            print(e)
