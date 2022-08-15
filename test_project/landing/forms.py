from django import forms
from .models import *


class SubscribersForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        exclude = [""]
        # exclude = ["slug", "uuid", "is_featured", "created_by", "update_by", "created", "updated"]
