import os, sys
djangoproject_home = "C:\Users\nick\Documents\GitHub\NHLNLP\tutorial\mysite\mysite"
sys.path.append(djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
print(sys.path)
print(os.environ)

from models import Entities

e = Entities(1,"entity text", 'type', '0.2343','positive','0.555')
e.save()