from django.contrib import admin


from .models import Contact, Agent, Properties, Blog, Comment
# Register your models here.
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Agent)
admin.site.register(Properties)
admin.site.register(Comment)
