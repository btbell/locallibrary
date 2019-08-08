import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RenewBookForm(forms.Form):
  renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default is 3 weeks).")

  def clean_renewal_date(self):
    data = self.cleaned_data['renewal_date']

    # make sure date is not in the past
    if data < datetime.date.today():
      raise ValidationError(_('Invalid date - renewal in past'))

    # make sure date is in the allowed range
    if data > datetime.date.today() + datetime.timedelta(weeks=4):
      raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

    # return clean data
    return data

#form_test
# this is a test form from https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html
# on ways to modify form markup and styling
class ContactForm(forms.Form):
  name = forms.CharField(max_length=30)
  email = forms.EmailField(max_length=254)
  message = forms.CharField(
    max_length=2000,
    widget=forms.Textarea(),
    help_text='Write here your message!'
  )
  source = forms.CharField(  # A hidden input for internal use
    max_length=50,  # tell from which page the user sent the message
    widget=forms.HiddenInput()
  )

  def clean(self):
    cleaned_data = super(ContactForm, self).clean()
    name = cleaned_data.get('name')
    email = cleaned_data.get('email')
    message = cleaned_data.get('message')
    if not name and not email and not message:
      raise forms.ValidationError('You have to write something!')

class ColorfulContactForm(forms.Form):
  name = forms.CharField(
    max_length=30,
    widget=forms.TextInput(
      attrs={
        'style': 'border-color: blue;',
        'placeholder': 'Write your name here'
      }
    )
  )
  email = forms.EmailField(
    max_length=254,
    widget=forms.EmailInput(attrs={'style': 'border-color: green;'})
  )
  message = forms.CharField(
    max_length=2000,
    widget=forms.Textarea(attrs={'style': 'border-color: orange;'}),
    help_text='Write here your message!'
  )

# i'm testing add styles and attributes to Django form elements
#class AltCreateAuthorForm(form.Form):
 # first_name = forms.Charfield(
 #   max_length=40,
 #   widget=formsTextInput(
 #     attrs={
 #       'style': 'pink;',
 #       'placeholder': 'Placeholder testing'
 #     }
 #   )
 # )