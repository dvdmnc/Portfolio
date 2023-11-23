from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'portfolio/index.html', {
        'language' : 'french'
    })

def english(request):
    return render(request, "portfolio/indexenglish.html", {
        'language' : 'english'
    })