from django.contrib import admin
from .models import Debate

# Register your models here.
@admin.register(Debate)
class DebateAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'title', 'description', 'status']