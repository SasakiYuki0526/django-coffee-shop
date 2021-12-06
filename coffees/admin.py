from django.contrib import admin

# Register your models here.
#從models匯入
from .models import *

admin.site.register(Coffee)
admin.site.register(MainProcessing)
admin.site.register(OriginPlace)
admin.site.register(Grinding)