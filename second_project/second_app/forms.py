from django import forms
from second_app.models import Users


class NewUserForm(forms.ModelForm):
    class Meta:
        model =Users
        fields = '__all__'
