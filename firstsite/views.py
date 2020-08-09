from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'homepage.html')
def index(request):
    return render(request,'index_mod.html')
def analyze(request):
    intext=request.POST.get('text','default')
    removepuncbtn=request.POST.get('removepunc','off')
    fullcapsbtn=request.POST.get('fullcaps','off')
    extraspaceremoverbtn = request.POST.get('extraspaceremover','off')
    lineremoverbtn=request.POST.get('lineremover','off')
    charcountbtn=request.POST.get('charcount','off')


    if removepuncbtn == "on":
        analyzed = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*|_~'''
        for char in intext:
            if char not in punctuations:
                analyzed += char
        params={'purpose':'Remove Punctuation','analyzed_text':analyzed}
        intext = analyzed

    if fullcapsbtn == "on":
        analyzed = ''
        for char in intext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalizing your text', 'analyzed_text': analyzed}
        intext = analyzed

    if extraspaceremoverbtn == 'on':
        analyzed = ''
        for index,char in enumerate(intext):
            if intext[index] == " " and intext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Removing extra spaces', 'analyzed_text': analyzed}
        intext = analyzed

    if lineremoverbtn == 'on':
        analyzed = ''
        for char in intext:
            if char != '\n' and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removing Lines', 'analyzed_text': analyzed}
        intext = analyzed


    if charcountbtn == 'on':
        analyzed = 0
        for char in intext:
            analyzed += 1
        params = {'purpose': 'Character counted', 'analyzed_text':f"the number of characters in your text = {analyzed} "}
        return render(request, 'analyzed_mod.html', params)
    if removepuncbtn != 'on' and fullcapsbtn != 'on' and extraspaceremoverbtn != 'on' and lineremoverbtn != 'on' and charcountbtn !='on':
        return render(request,'error.html')
    return render(request, 'analyzed_mod.html', params)

def aboutus(request):
    return render(request,'aboutus.html')
def check(request):
    return render(request,'check.html')

