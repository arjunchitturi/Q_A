from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext as _

from bootstrap.models import Question, ExampleFields

#custom text field
class TitleField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super(TitleField, self).__init__(*args, **kwargs)
        self.required = True
        self.widget = forms.TextInput(attrs={'size' : 70, 'autocomplete' : 'off',\
         'style':'width:600px', 'placeholder':_('please enter a descriptive title for your question') })
        self.max_length = 255
        self.label = _('Q title')
        #self.help_text = _('please enter a descriptive title for your question')
        self.initial = ''

    def clean(self, value):
        if len(value) < 5:
            raise forms.ValidationError(_('title must be > 5 characters'))

        return value

#custom text area field
class EditorField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super(EditorField, self).__init__(*args, **kwargs)
        self.required = True
        self.widget = forms.Textarea(attrs={'id':'editor',\
         'style':'height:100px;width:600px', 'placeholder':_('give your description')})
        self.label = _('Content')
        self.help_text = u''
        self.initial = ''

    def clean(self, value):
        if len(value) < 10:
            raise forms.ValidationError(_('question content must be > 10 characters'))

        return value

#question form.
class QuestionForm(forms.Form):
    title = TitleField()
    text = EditorField()

#answer form.
class AnswerForm(forms.Form):
    text = EditorField()

'''
    The following classes are for test purpose.
'''
class ExampleForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'xlarge'}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class':'xlarge'}))
    message = forms.CharField(
            widget=forms.Textarea(attrs={'class':'xxlarge'}))    
    class Meta:
        model = ExampleFields
        
class AjaxAutoComplete(forms.Form):
    name = forms.CharField(help_text="Enter a Star Wars character name, e.g Darth",
        label="Star Wars Character",
        widget=forms.TextInput(attrs={'class':'xlarge'}))  
        
class PopoverForm(forms.Form):
    popover_input = forms.CharField(label="Form Input Popover",
        widget=forms.TextInput(attrs={'class':'xlarge', 
            'data-content' : 'On focus, this appears - defined in forms.py',
            'data-original-title' : 'My title'}))

