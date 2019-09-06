from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea()
    )
    source = forms.CharField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message', 'source')

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')