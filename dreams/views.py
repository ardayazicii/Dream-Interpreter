
# Create your views here.
# views.py
import requests
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render
from .models import Dream






@csrf_exempt
def generate_interpretation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data.get('prompt')

        response = requests.post(
            "http://localhost:11434/api/generate",
            headers={"Content-Type": "application/json"},
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )

        if response.status_code == 200:
            result = response.json()
            return JsonResponse({"response": result["response"]})
        else:
            return JsonResponse({"error": "API error"}, status=500)
    
    return JsonResponse({"error": "Only POST allowed"}, status=405)

def dream_input(request):
    return render(request, 'dreams/dream_input.html')


def dream_list(request):
    dreams = Dream.objects.all().order_by('-id')  # en yeni en üstte
    return render(request, 'dreams/dream_list.html', {'dreams': dreams})