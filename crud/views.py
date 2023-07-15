from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import Article_serializer
from django.views.decorators.csrf import csrf_exempt 
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def article_list(request):
    if request.method=='GET':
        article = Article.objects.all()
        serializer = Article_serializer(article,many=True)
        return Response(
            serializer.data
        )
    
    elif request.method == 'POST':
        data = request.data
        serializer = Article_serializer(data=data,many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
            serializer.data,status=status.HTTP_201_CREATED
        )
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def detail_list(request,pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = Article_serializer(article)
        return JsonResponse(serializer.data)
    
    elif request.method =='PUT':
        data = JSONParser().parse(request)
        serializer = Article_serializer(article,data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        
        return JsonResponse(serializer.errors)
    
    elif request.method =='DELETE':
        article.delete()
        return HttpResponse(status=204)
        
    

    


    