from django.contrib import admin

# Register your models here.
from django.contrib import admin

from.models import Faculty, Campus, Job,Message,Employee,Cursus, Student,Invitation

admin.site.register(Faculty)

admin.site.register(Campus)

admin.site.register(Message)
admin.site.register(Job)

admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(Cursus)
admin.site.register(Invitation)







