''' yare yare zannendana'''

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def capitalize(request):
    dText = (request.GET.get('text', 'default'))
    puncRemove = request.GET.get('puncremove', 'default')
    capitalAll = request.GET.get('capitalall', 'default')
    removeNew = request.GET.get('removenew', 'default')
    removeSpace = request.GET.get('removespace', 'default')
    if puncRemove == "on":
        analyzed = ""
        puncSymbols = "?()?/@!*&^$%#"
        for char in dText:
            if char not in puncSymbols:
                analyzed = analyzed + char
        params = {'purpose': 'Punctuations removed', 'analyzed_text': analyzed}
        dText = analyzed
    if capitalAll == 'on':
        analyzed = ""
        for char in dText:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalized format', 'analyzed_text': analyzed}
        dText = analyzed
    if removeNew == 'on':
        analyzed = ""
        for char in dText:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        dText = analyzed
    if removeSpace == 'on':
        analyzed = ""
        for index, char in enumerate(dText):
            if not (dText[index] == " " and dText[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra spaces removed', 'analyzed_text': analyzed}

    if (puncRemove != 'on' and capitalAll != 'on' and removeSpace != 'on' and removeNew != 'on'):
        return HttpResponse(
            '<h1 style="color: darkred; justify-content: center; text-align: center;'
            'font-size: 50px; margin-top: 15rem">Please select some options and try again!</h1>')

    return render(request, 'updated.html', params)
