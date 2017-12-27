from django import forms

from .models import Register
from django.core.validators import RegexValidator

gsm_validator = RegexValidator(
	regex=r'^[0-9]{10}$',
	message="Merci d'insérer un numéro valide"
)

class RegisterForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({
				'placeholder' : self.fields[field].label,
				'class' : 'form-control',
			})
			self.fields[field].label = ''
		self.fields["gsm"].validators.append(gsm_validator)
		print(self.fields["gsm"].__dict__)
	class Meta:
		model = Register
		fields = '__all__'