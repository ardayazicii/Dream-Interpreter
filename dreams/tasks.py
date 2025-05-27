from celery import shared_task
import requests
import json

@shared_task
def analyze_dream(dream_id, description):
    payload = {
        "model": "mistral",
        "prompt": f"Analyze this dream: {description}",
        "stream": False
    }
    
    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        response.raise_for_status()
        result = response.json()
        
        # 💥💥💥 BURAYI EKLİYORSUN
        print("OLLAMA RESPONSE:", result)  # 🔥 burada raw sonucu göreceğiz!

        interpretation = result.get("response", "No interpretation available.")
    
    except requests.exceptions.RequestException as e:
        interpretation = f"Request failed: {str(e)}"
    except ValueError:
        interpretation = "Invalid JSON received from LLM."
    
    from .models import Dream
    try:
        dream = Dream.objects.get(id=dream_id)
        dream.interpretation = interpretation
        dream.save()
    except Dream.DoesNotExist:
        pass




