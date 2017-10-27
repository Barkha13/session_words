from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request,"session_words_app/index.html")

def word_process(request):
    if 'word' not in request.session:
        request.session['word'] = ""
    if 'color' not in request.session:
        request.session['color'] = ""
    if 'word_list' not in request.session:
        request.session['word_list'] = []
    if 'fonts' not in request.session:
        request.session['fonts'] = ""
    request.session['word'] = request.POST['word']
    request.session['color'] = request.POST['color']
    print "checkbox valueeeeeeeee...{}".format(request.POST['fonts'])
    request.session['fonts'] = request.POST['fonts']
    
    request.session['word_list'].append(request.session['word'])
    
    request.session.modified = True
    
    return redirect('/')

def clear(request):
    del request.session['word']
    del request.session['word_list']
    del request.session['color']
    del request.session['fonts']
    return redirect('/')


