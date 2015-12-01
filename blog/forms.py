from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()

    def clean_email(self):
    	email= self.cleaned_data.get ('email')
    	email_base, provider = email.split("@")
    	domain, extension = provider.split('.')
    	return email