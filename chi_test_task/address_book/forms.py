from django import forms

from address_book.models import Person


class AddressBookForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone', 'address']


class NewEntry(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    phone = forms.CharField(label='Phone', max_length=100)
    address = forms.CharField(label='Address', max_length=100)


class EditEntry(forms.ModelForm):
    pass






# def save(self):
#     new_entry = Person.objects.create(first_name=self.cleaned_data['first_name'],
#                                       last_name=self.cleaned_data['last_name'],
#                                       phone=self.cleaned_data['phone'],
#                                       address=self.cleaned_data['address'])
#     return new_entry
