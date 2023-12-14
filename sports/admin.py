from django.contrib import admin

from sports.models import Sports

class SportsAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','author','tags','date','image')

admin.site.register(Sports,SportsAdmin)