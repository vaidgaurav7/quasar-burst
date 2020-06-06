# Imports to run script in local env
import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "heroku_django.settings")
import django
django.setup()

from apis.models import TiLoginUserData2
g=TiLoginUserData2(user_id=20977,password='nicola*weakly')
n=TiLoginUserData2(user_id=20983,password='podunk*vocal')
g.save()
n.save()
