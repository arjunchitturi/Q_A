from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
#from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
#from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.utils import simplejson

from bootstrap.forms import QuestionForm, AnswerForm \
#, ExampleForm, AjaxAutoComplete, PopoverForm
from bootstrap.models import User, Question, Answer \
#StarWarsCharacter


#Home Page
def home(request):
    context = {}
    context.update(csrf(request))
    context["user"] = request.user
    context["hero_title"] = "Welcome to Q and A"
    return render_to_response("bootstrap/home.html", context)


#new question form
def ask_question(request):
    RequestContext = {}
    RequestContext["form"] = QuestionForm()
    RequestContext["user"] = request.user
    RequestContext["hero_title"] = "Question Form"
    RequestContext.update(csrf(request))
    return render_to_response("bootstrap/example.html", RequestContext)


#submit question using ajax.
def send_question(request):
    RequestContext = {}
    RequestContext["user"] = request.user
    if request.method == "POST" and "text" in request.POST:
        form = QuestionForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated():

                #Do Something, e.g. save, send an email
                title = form.cleaned_data.get('title', None)
                text = form.cleaned_data['text']
                user, new_or_old = User.objects.get_or_create(user = request.user)
                qus, update_text = Question.objects.get_or_create(title = title, author = user)
                qus.text = text
                qus.save()
                template = "bootstrap/example_form_success.html"
                success = True

        else:
            template = "bootstrap/question_form.html"
            RequestContext["form"] = form
            success = False

    else:
        template = "bootstrap/question_form.html"
        RequestContext["form"] = QuestionForm()
        success = False

    html = render_to_string(template, RequestContext)
    response = simplejson.dumps({"success": success, "html": html})
    return HttpResponse(response, content_type = "application/javascript; charset = utf-8")


#display the list of questions.
def questions_list(request):
    c = {}
    questions = Question.objects.all()
    c['questions'] = questions
    c['user'] = request.user
    c['hero_title'] = "Hello, " + str(request.user.username) + "!"
    return render_to_response('bootstrap/questions_list.html', c)


#vew a single question, and its answers.
def view_question(request, id):
    c = {}
    q = Question.objects.get(id = int(id))
    c['question'] = q
    c['user'] = request.user
    return render_to_response('bootstrap/view_question.html', c)


#delete a question.
@login_required
def remove_question(request, id):
    to_del = Question.objects.get(id = int(id))
    to_del.delete()
    return redirect('/questions_list')


#form to add a new answer a question
def answer_question(request, id):
    c = {}
    q = Question.objects.get(id = int(id))
    c['question'] = q
    c["form"] = AnswerForm()
    c["user"] = request.user
    c["hero_title"] = "Answer Form"
    c.update(csrf(request))
    return render_to_response('bootstrap/answer_form.html', c)


#submit the answer using ajax.
def send_answer(request):
    RequestContext = {}
    #qid = Question.objects.get(id = int(id))
    RequestContext["user"] = request.user
    RequestContext["hero_title"] = "Answer Form"
    if request.method == "POST" and "text" in request.POST:
        req = request.POST.copy()
        id = req['qid']
        #req.pop('qid')
        form = AnswerForm(req)
        if form.is_valid():
            if request.user.is_authenticated():
                #Do Something, e.g. save, send an email
                text = form.cleaned_data['text']
                user = User.objects.get(user=request.user)
                qid = Question.objects.get(id = int(id))
                Answer.objects.create(text=text, author=user, question=qid)
                template = "bootstrap/example_form_success.html"
                success = True
        else:
            template = "bootstrap/answer_question.html"
            RequestContext["form"] = form
            success = False
    else:
        template = "bootstrap/answer_question.html"
        RequestContext["form"] = AnswerForm()
        success = False

    html = render_to_string(template, RequestContext)
    response = simplejson.dumps({"success": success, "html": html
    })
    return HttpResponse(response,
                        content_type=\
                            "application/javascript; charset=utf-8")


#delete answer for a particular question (qid).
@login_required
def remove_answer(request, id, qid):
    to_del = Answer.objects.get(id = int(id))
    to_del.delete()
    #return redirect('/questions_list')
    #return HttpResponseRedirect(reverse('view_question', args=[qid]))
    return redirect('/view_question/' + qid)

'''
    The following definitions are for test purpose.

def ajax_form(request):
    context = {}
    context["form"] = ExampleForm()
    context["user"] = request.user
    context["hero_title"] = "Ajax Form"
    context.update(csrf(request))
    return render_to_response("bootstrap/example.html", context)


def ajax_example(request):
    context = {}
    if request.POST:
        form = ExampleForm(request.POST)
        if form.is_valid():
            #Do Something, e.g. save, send an email
            template = "bootstrap/example_form_success.html"
            success = True
        else:
            template = "bootstrap/example_form.html"
            context["form"] = form
            success = False
    else:
        template = "bootstrap/example_form.html"
        context["form"] = ExampleForm()
        success = False
    html = render_to_string(template, context)
    response = simplejson.dumps({"success": success, "html": html})
    return HttpResponse(response,
                        content_type=\
                            "application/javascript; charset=utf-8")


def modal_dialog(request):
    context = {}
    context["user"] = request.user
    context["hero_title"] = "Modal Dialog"
    context.update(csrf(request))
    return render_to_response("bootstrap/modal/modal_dialog.html", context)


def text_modal_dialog(request):
    if request.POST.get('id', False):
        # String provided for ease of demonstration
        # Replace with model lookup, e.g.
        # wording = User.objects.get(id=request.POST.get('id', False))
        wording = "ABC"
    else:
        wording = False
    template = "bootstrap/modal/modal_dialog_text.html"
    html = render_to_string(template, {"wording": wording})
    response = simplejson.dumps({"html": html})
    return HttpResponse(response,
                        content_type=\
                            "application/javascript; charset=utf-8")


def ajax_autocomplete(request):
    context = {}
    context["user"] = request.user
    context["hero_title"] = "Ajax Autocomplete"
    context["form"] = AjaxAutoComplete()
    context.update(csrf(request))
    return render_to_response("bootstrap/autocomplete/autocomplete.html", context)


def ajax_autocomplete_lookup(request):
    results = []
    if request.GET.has_key("term"):
        value = request.GET[u'term']
        characters = StarWarsCharacter.objects.filter(name__icontains=value)
        for character in characters:
            character_dict = {}
            character_dict["id"] = character.id
            character_dict["label"] = character.name
            results.append(character_dict)
    response = simplejson.dumps(results)
    return HttpResponse(response,
                        content_type=\
                            "application/javascript; charset=utf-8")


def ajax_autocomplete_get_selected_item(request):
    character_id = request.POST.get("character_id", False)
    if character_id:
        try:
            character = StarWarsCharacter.objects.get(id=character_id)
        except StarWarsCharacter.DoesNotExist:
            character = None
    else:
        character = None
    template = "bootstrap/autocomplete/select_result.html"
    html = render_to_string(template, {"character": character})
    response = simplejson.dumps({"html": html})
    return HttpResponse(response,
                        content_type=\
                            "application/javascript; charset=utf-8")

def popover(request):
    context = {}
    context["user"] = request.user
    context["hero_title"] = "Popovers"
    context["form"] = PopoverForm()
    context.update(csrf(request))
    return render_to_response("bootstrap/popover/popover.html", context)

def geolocation(request):
    context = {}
    context["user"] = request.user
    context["hero_title"] = "Geolocation"
    context.update(csrf(request))
    return render_to_response("bootstrap/geolocation/geolocation.html", context)

@login_required
def inside(request):
    context = {}
    context["user"] = request.user
    return render_to_response("bootstrap/inside.html", context)
'''
