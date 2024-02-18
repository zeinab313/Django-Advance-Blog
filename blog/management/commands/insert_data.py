from io import StringIO
from typing import Any
from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import User,Profile
from blog.models import Post,Category
from datetime import datetime
import random
from accounts.models import User, Profile
from blog.models import Post, Category

#خودمان یه لیست تعریف کردیم که داده های دلخواه ما را اضافه کند
category_list = ["IT", "Design", "Fun"]



#کدهای این صفحه جهت ساخت داده های فیک است
class Command(BaseCommand):
    help="inserting dumy data"

    def __init__(self,*args,**kwargs) :
        super(Command,self).__init__(*args,**kwargs)
        self.fake=Faker()

    def handle(self, *args, **options) :
        #ساخت یک کاربر فیک
        user=User.objects.create_user(email=self.fake.email(),password="test@123456")
        profile=Profile.objects.get(user=user)
        print(user)
        print(profile)
        #ساخت یک پروفایل فیک
        profile.first_name=self.fake.first_name()
        print(profile.first_name)
        profile.last_name=self.fake.last_name()
        profile.description=self.fake.paragraph(nb_sentences=5)
        profile.save()

        for name in category_list:
            Category.objects.get_or_create(name=name)

        #متغیری تعریف نکردیم و خط تیره گذاشتیم چون برامون مهم نیست که متغیر چی باشه و نمیخوایم ازش استفاده کنیم
        #بااستفاده از این تابع هم 10 پست فیک استفاده کردیم
        for _ in range(10):
            Post.objects.create(
                auther=profile.user,
                title=self.fake.paragraph(nb_sentences=1),
                content=self.fake.paragraph(nb_sentences=10),
                status=random.choice([True, False]),
                category=Category.objects.get(name=random.choice(category_list)),
                published_date=datetime.now(),
            )
