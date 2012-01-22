from django.contrib import admin
#from bootstrap.forms import AnswerModelForm

from bootstrap.models import User, Question, Answer#, StarWarsCharacter

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1
    exclude = ('added_at',)    

class QuestionInline(admin.ModelAdmin):
    inlines = [ AnswerInline, ]
    exclude = ('added_at',)

admin.site.register(User)
admin.site.register(Question, QuestionInline)

#admin.site.register(Answer)
#admin.site.register(StarWarsCharacter)

