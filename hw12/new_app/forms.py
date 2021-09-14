from django import forms
from datetime import datetime

from prompt_toolkit.validation import ValidationError


class NewForm(forms.Form):
    email = forms.EmailField(label="E-mail", required=True)
    reminder = forms.CharField(label='Reminder')
    date_time = forms.DateTimeField(label='Datetime')
    message = forms.CharField(widget=forms.Textarea, required=True)

    def date_validate(self):
        data = self.cleaned_data['date_time']

        if (data - datetime.today()).days > 2 and datetime.now() < data:
            raise ValidationError('Invalid data')
        return data

