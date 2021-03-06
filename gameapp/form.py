from django import forms
from .models import UserAnswers


class GetUserAnswer(forms.ModelForm):
    class Meta:
        model = UserAnswers
        fields = ('answer','level')
        # fields ='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'answer':
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''
            else:
                field.widget = forms.HiddenInput()