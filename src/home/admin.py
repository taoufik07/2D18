from django.contrib import admin

from .models import *


admin.site.register(SiteInfo)
admin.site.register(Attandant)
admin.site.register(OurProgram)
admin.site.register(FAQ)
admin.site.register(Sponsor)
admin.site.register(Register)


admin.site.site_header = "2D18 Administration"
admin.site.site_title = "2D18 Administration"