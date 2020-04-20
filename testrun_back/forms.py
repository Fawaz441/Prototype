from django import forms

SERVICE_OPTIONS = (
    ('Networking','Networking'),
    ('Data Analysis','Data Analysis'),
    ('Engineering','Engineering'),
    ('Hacking','Hacking'),
)

class OfferForm(forms.Form):
    client_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':"John"}))
    service = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'placeholder':"e.g Networking"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'john@yahoo.com'}))
    number = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':"+2348123456789"}))

class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)
    area = forms.CharField(max_length=20,widget=forms.SelectMultiple(choices=SERVICE_OPTIONS,attrs={'class':'choices'}))
