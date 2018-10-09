from django.contrib.auth import get_user_model
from models import Events

User = get_user_model
User.site.register(Events)
