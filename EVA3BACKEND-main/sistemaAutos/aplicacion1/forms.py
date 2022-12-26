from django import forms
from aplicacion1.models import Auto
from aplicacion1.models import PersonalRRHH
from aplicacion1.models import Cliente

class FormAuto(forms.ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'
        
class FormRRHH(forms.ModelForm):
    class Meta:
        model = PersonalRRHH
        fields = '__all__'
        
class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'