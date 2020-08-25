from django import forms
from django.core import validators
from home.models import Users

# The code below will create custom validator
# use this validator when required with following line
# name = forms.CharField(validators=[check_name])
def check_name(value):
    if value[0].lower() != 'm' :
        raise forms.ValidationError("The Name field must start with 'm' ")



# This class creates the form
class FormName(forms.Form):
    # The variables below define the fields of the form
    name = forms.CharField()
    email = forms.EmailField()
    verifyEmail = forms.EmailField(label='Enter your email again!')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
    # The code below works as a validator for the botcatcher fields
    # It does not allow Bot to set the value, so no bot can fill out the forms
    # Only real human can fill the form
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #
    #     if len(botcatcher) > 0 :
    #         raise forms.ValidationError("You are caught, Mr. Bot!")
    #     return botcatcher
    # There are built-in validators available in Django
    # Instead of writing manual code, we can use that built-in validators

    # The method below will clean entire form and
    # check the emails are matched or not
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verifyEmail']
        if email != vemail :
            raise forms.ValidationError("The emails must match!")


class UserData(forms.ModelForm):
    class Meta():
        model = Users
        fields = '__all__'
