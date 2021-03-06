from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({
				'placeholder' : self.fields[field].label,
				'class' : 'form-control',
			})
			self.fields[field].label = ''

	class Meta:
		model = Contact
		fields = '__all__'
