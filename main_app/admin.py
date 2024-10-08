from django.contrib import admin
from .models import Diary, Goals, Physical, Mental, Emotional

# Register your models here.
admin.site.register(Diary)
admin.site.register(Goals)
admin.site.register(Physical)
admin.site.register(Mental)
admin.site.register(Emotional)

