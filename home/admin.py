from django.contrib import admin
from .models import Stoyo
from .models import Publisher
from .models import Temporary

# Register your models here.

admin.site.register(Stoyo)
admin.site.register(Publisher)
admin.site.register(Temporary)
