from django import forms
from .models import Book, Caterogy, Author


class CategoryForm(forms.ModelForm):
    # name = forms.CharField(help_text="this is name")
    # name = forms.CharField(max_length=10)

    class Meta:
        model = Caterogy
        fields = '__all__'
        # exclude = ['count']


# form = BookForm(instance=a)
    # {{form.as_form}}

# from django import forms
#
#
# class BookForm(forms.Form):
#     name = forms.CharField(max_length=10)
#
# form = BookForm(instance=a)
#     # {{form.as_form}}