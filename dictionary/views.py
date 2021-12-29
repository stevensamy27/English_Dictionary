from django.shortcuts import render
from PyDictionary import PyDictionary
# Create your views here.

def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.Get.get('search')
    dictionary =  PyDictionary()
    meaning = dictionary.meaning(search)
    synonyms = dictionary.synonym(search)
    antonyms = dictionary.antonyms(search)
    return render(request, 'word.html') 

