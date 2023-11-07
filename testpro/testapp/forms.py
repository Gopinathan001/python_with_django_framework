from django import forms  
from testapp.models import Details 



class BankForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = "__all__"