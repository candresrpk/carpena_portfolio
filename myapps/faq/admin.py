from django.contrib import admin
from .models import Faq, Tag, Faq_tag, Faq_detail
# Register your models here.


admin.site.register(Faq)
admin.site.register(Tag)
admin.site.register(Faq_tag)
admin.site.register(Faq_detail)


