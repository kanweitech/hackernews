from django.shortcuts import render
from django.http import HttpResponse
import requests


def news(request):

	#pull data from third party rest api
	response = requests.get('https://hackernews.api-docs.io')

	#convert response data into json
	news = response.json()

	return HttpResponse("news")
	pass
