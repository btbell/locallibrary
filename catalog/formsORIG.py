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
