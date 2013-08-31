# -*- coding: utf-8 -*-
import django.core.management
from paper import settings
django.core.management.setup_environ(settings)
from writer import models as wmodels
from customer import models as cmodels
from paper import mail

writernumber=wmodels.Profile.objects.count()
customernumber=cmodels.Profile.objects.count()
report=u"写手总数:%d 需求者总数:%d" % (writernumber,customernumber)
mail.sendmailthread('每日报告',report,'85lunwen@gmail.com', ['fanshaorui@gmail.com']).start()