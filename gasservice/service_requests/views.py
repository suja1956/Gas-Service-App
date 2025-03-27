from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from service_requests.forms import ServiceRequestForm
from .models import ServiceRequest

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('service_requests:track_request', request_id=service_request.id)
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/submit_request.html', {'form': form})

def home(request):
    return render(request,'base.html')

@login_required
def track_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id, customer=request.user)
    return render(request, 'service_requests/request_detail.html', {'service_request': service_request})

@login_required
def list_requests(request):
    requests = ServiceRequest.objects.filter(customer=request.user).order_by('-submitted_at')
    return render(request, 'service_requests/track_request.html', {'requests': requests})
