from django.contrib import admin
from .models import Subscriber

# Register your models here.

class SubscriberAdmin(admin.ModelAdmin):
    # list_display = ("name", "email")
    list_display = [field.name for field in Subscriber._meta.fields]
    fields = ("email",)
    list_filter = ('name',)
    search_fields = ('name', 'email')
    # exclude = ("email",)

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)
