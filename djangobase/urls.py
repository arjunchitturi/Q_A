from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
#import settings
from django.views.generic.simple import direct_to_template

from bootstrap.views import *

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    #Registration
    (r'^accounts/', include('registration.urls')),
    
    #Q and A
    (r'^ask_question', ask_question),
    (r'^send_question', send_question),
    (r'^questions_list', questions_list),
    (r'^view_question/(?P<id>\d+)/$', view_question),
    (r'^remove_question/(?P<id>\d+)/$', remove_question),

    (r'^answer_question/(?P<id>\d+)/$', answer_question),
    (r'^send_answer', send_answer),
    #(r'^answers_list', answers_list),
    (r'^remove_answer/(?P<id>\d+)/(?P<qid>\d+)/$', remove_answer),

    (r'^$', home),
    (r'^inside/$', inside),

    #The following urls for test purpose.    
    #Ajax Form
    (r'^ajax_form', ajax_form),
    (r'^ajax_example', ajax_example),

    #modal dialog
    (r'^modal_dialog/$', modal_dialog),
    (r'^text_modal_dialog/$', text_modal_dialog),

    #ajax autocomplete
    (r'^ajax_autocomplete/$', ajax_autocomplete),
    (r'^ajax_autocomplete_lookup/$', ajax_autocomplete_lookup),
    (r'^ajax_autocomplete_get_selected_item/$', ajax_autocomplete_get_selected_item),

    #Popovers
    (r'^popover/$', popover),

    #Geolocation
    (r'^geolocation/$', geolocation),

    #Humans and Robots
    ('^humans.txt$', direct_to_template, {'template':'humans.txt', 'mimetype':'text/plain'}),
    ('^robots.txt$', direct_to_template, {'template':'robots.txt', 'mimetype':'text/plain'}),

)

'''
urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)
'''
