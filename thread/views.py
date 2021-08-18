from django.shortcuts import render
from .models import *
from faker import Faker
fake = Faker()
import random
from .thread import CreateStuendtsThread


def student_details(request):
    count = 100
    CreateStuendtsThread(count).start()
    # for i in range(count):
        # print(i)
        # Student.objects.create(
        #     student_name = fake.name(),
        #     student_email = fake.email(),
        #     address = fake.address(),
        #     age = random.randint(10,40)
        # )

    return render(request,'index.html',{"data":"yes"})

