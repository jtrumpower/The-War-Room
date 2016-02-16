from django.contrib import admin

# Register your models here.
from .models import Wars,Bases,Comments,Calls,Members

admin.site.register(Wars)
admin.site.register(Bases)
admin.site.register(Comments)
admin.site.register(Calls)
admin.site.register(Members)
