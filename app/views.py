from django.shortcuts import render
from .models import Article
#from .maclasse import Circuit
import requests
#from django.http import HttpResponse

url = 'http://ergast.com/api/f1/'
years = ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
# Create your views here.
def home(request):
    list_articles=Article.objects.all()
    context={"liste_articles":list_articles}
    return render(request, "index.html",context)

def detail(request, id_article):
    #print("L'identité de l'article est: ", id_article)
    article=Article.objects.get(id=id_article)
    #circuit=Circuit.objects.all()
    return render(request, 'detail.html', {"article":article})

# def fnc_circuit(request):
#     circuit = Circuit.objects.get()
#     return render(request, 'detail.html', {"circuit": circuit})

# def fnc_circuit(request):
#     for year in years:
#          # print(url+x+'/circuits.json')
#          r = requests.get(url + year + '/circuits.json')
#          data = r.json()
#          data_circuit = data['MRData']['CircuitTable']['Circuits']
#          for year in data_circuit:
#              print(year['circuitName'], year['Location']['locality'], year['Location']['country'])
#              #return HttpResponse
#              #return render(request, 'detail.html')
