from django.contrib import admin

from other.models import other

class otherAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','author','tags','date','image','slug')

admin.site.register(other,otherAdmin)