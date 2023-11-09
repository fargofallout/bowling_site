from django.contrib import admin

from .models import Bowler, Team, League

# Register your models here.
admin.site.register(Bowler)
admin.site.register(Team)
admin.site.register(League)
