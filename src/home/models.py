from django.db import models

from django.core.validators import RegexValidator

class SiteInfo(models.Model):
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=200)
	theme_title = models.CharField(max_length=200)
	theme_description = models.TextField()
	video_title = models.CharField(max_length=200)
	video_subtitle = models.CharField(max_length=200)
	video_description = models.TextField()
	video_link = models.URLField()
	conference_title = models.CharField(max_length=200, null=True, blank=True)
	conference_subtitle = models.CharField(max_length=200, null=True, blank=True)
	sponsor_title = models.CharField(max_length=100, null=True, blank=True)
	sponsor_description = models.TextField(null=True, blank=True)
	register_title = models.CharField(max_length=100, null=True, blank=True)
	register_subtitle = models.TextField(null=True, blank=True)
	register_description = models.TextField(null=True, blank=True)
	contact_title = models.CharField(max_length=100, null=True, blank=True)
	contact_description = models.TextField(null=True, blank=True)
	facebook = models.URLField(null=True, blank=True)
	twitter = models.URLField(null=True, blank=True)
	linkedin = models.URLField(null=True, blank=True)

	def __str__(self):
		return self.title


class Attandant(models.Model):
	full_name = models.CharField(max_length=150)
	avatar = models.ImageField(upload_to="attandant/")
	about = models.TextField()

	def __str__(self):
		return self.full_name


class OurProgram(models.Model):
	attandant = models.ForeignKey(Attandant)
	title = models.CharField(max_length=200)
	time = models.TimeField()
	room = models.CharField(max_length=50)
	description = models.TextField(null=True, blank=True) 

	def __str__(self):
		return "{} by {}".format(self.title, self.attandant)

class FAQ(models.Model):
	question = models.CharField(max_length=200)
	answer = models.TextField()

	def __str__(self):
		return self.question


class Sponsor(models.Model):
	title = models.CharField(max_length=100)
	logo = models.ImageField(upload_to="sponsors")

	def __str__(self):
		return self.title

STATUS = (
	('1', 'Professor'),
	('2', 'Student'),
)

class Register(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone_regex = RegexValidator(
		regex=r'^[0-9]{10}$',
		message="Merci d'insérer un numéro valide"
	)
	gsm = models.CharField(
		"Phone number",
		validators=[phone_regex],
		max_length=10,
		null=True,
		blank=True
	)
	email = models.EmailField('Email Address')
	birthday = models.DateField(null=True, blank=True)
	status = models.CharField(
		choices=STATUS,
		max_length=2,
		null=True,
		blank=True
	)

	class Meta:
		verbose_name = "Registred"
		verbose_name_plural = "Registred"

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name)