from django.contrib import admin
from lib.models import Book,Author,BookIstance,Genre

# Register your models here.

#admin.site.register(Student)
#admin.site.register(Klass)
#admin.site.register(Country)
#admin.site.register(Teacher)
#admin.site.register(District)
#admin.site.register(Book)

#using classes under admin site for advanced config

class BookAdmin(admin.ModelAdmin):

	list_display = ('title','author','isbn','summary')

admin.site.register(Book,BookAdmin)

#admin.site.register(Author)

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('First_Name','Last_Name','DOB','DOD')

admin.site.register(Author,AuthorAdmin)

admin.site.register(BookIstance)
admin.site.register(Genre)
