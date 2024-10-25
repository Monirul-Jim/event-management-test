from django.shortcuts import render
from django.contrib import messages
from event.models import Event, Booking


# def home(request):
#     events = Event.objects.all()
#     booked_events = Booking.objects.filter(
#         user=request.user).values_list('event_id', flat=True)
#     return render(request, 'home.html', {'events': events, 'booked_events': booked_events})
def home(request):
    events = Event.objects.all()
    booked_events = []

    # Check if the user is authenticated
    if request.user.is_authenticated:
        booked_events = Booking.objects.filter(
            user=request.user).values_list('event_id', flat=True)

    return render(request, 'home.html', {'events': events, 'booked_events': booked_events})
