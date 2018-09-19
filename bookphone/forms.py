from django import forms

from .models import Personal_unidad, Unidad, Personal_secretaria, Secretaria


class SecretariaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SecretariaForm, self).__init__(*args, **kwargs)
        self.fields['lat'].widget.attrs['readonly'] = True
        self.fields['lng'].widget.attrs['readonly'] = True

    class Meta:
        model = Secretaria
        fields = '__all__'


class UnidadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UnidadForm, self).__init__(*args, **kwargs)
        self.fields['lat'].widget.attrs['readonly'] = True
        self.fields['lat'].widget.attrs['class'] = 'lat_unidad'
        self.fields['lng'].widget.attrs['readonly'] = True
        self.fields['lng'].widget.attrs['class'] = 'lng_unidad'

    class Meta:
        model = Unidad
        fields = '__all__'


class PersonalSecretariaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonalSecretariaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Personal_secretaria
        fields = '__all__'


class PersonalUnidadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonalUnidadForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Personal_unidad
        fields = '__all__'