from django.shortcuts import render
import requests

def index(request):
    response=requests.get('https://saurav.tech/NewsAPI/top-headlines/category/health/in.json')
    data=response.json()
    news = data['articles']
    print(news)
    context ={
        "news":news,
    }
    return render(request,"index.html",context)
