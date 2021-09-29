from django import forms


class CreateBookForm(forms.Form):
    name = forms.CharField(max_length='25', required=True)
    authors = forms.CharField(max_length=50, required=True)
    pages = forms.IntegerField()
    price = forms.FloatField()
    publisher = forms.CharField(max_length=50, required=True)


class DeleteBookForm(forms.Form):
    book_id = forms.IntegerField(label='Book id')
