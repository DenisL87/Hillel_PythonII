from django import forms

from address_book.models import Person


class AddressBookForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone', 'address', 'url', 'image']


class NewEntry(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    phone = forms.CharField(label='Phone', max_length=100)
    address = forms.CharField(label='Address', max_length=100)
    url = forms.URLField(label='URL')
    image = forms.ImageField(label='Image')


class SearchEntry(forms.Form):
    input = forms.CharField(label='Type here:', max_length=100)
    matches = []


class EditEntry(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone', 'address', 'url', 'image']


class DeleteEntry(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone', 'address', 'url', 'image']
