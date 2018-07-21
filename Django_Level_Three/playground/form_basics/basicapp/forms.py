from django import forms
from django.core import validators

#Validate if a name should start with 'Z'
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name have to start with Z letter")

class FormName(forms.Form):
    #name = forms.CharField(validators = [check_for_z])
    name = forms.CharField(validators = [check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label = 'Enter your email again:')
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required = False,
                                 widget = forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_email = all_clean_data['verify_email']
        if email != v_email:
            raise forms.ValidationError("EMAILS NOT MATCH!")
