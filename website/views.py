from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import ContactSubmission
import json
from django.http import JsonResponse
def home(request):
    return render(request, 'home.html')
@csrf_exempt
@require_http_methods(["POST"])
def submit_contact_form(request):
    try:
        data = json.loads(request.body)
        submission = ContactSubmission.objects.create(
            name=data.get('name'),
            phone=data.get('phone'),
            email=data.get('email'),
            requirements=data.get('requirements')
        )
        return JsonResponse({'status': 'success'}, status=200)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)