from django import forms

class SecretForm(forms.Form):
    secret = forms.CharField(widget=forms.Textarea, 
                             attrs={"rows": 5, "cols": 20}, 
                             label="Secret",
                             help_text="Enter your secret here")
    