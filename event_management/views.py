# from django.shortcuts import render
# from django.contrib import messages
# from event.models import Event, Booking


# def home(request):
#     events = Event.objects.all()
#     booked_events = []

#     # Check if the user is authenticated
#     if request.user.is_authenticated:
#         booked_events = Booking.objects.filter(
#             user=request.user).values_list('event_id', flat=True)

#     return render(request, 'home.html', {'events': events, 'booked_events': booked_events})
from django.shortcuts import render
from django.contrib import messages
from event.models import Event, Booking
from django.db.models import Q


# def home(request):
#     events = Event.objects.all()
#     booked_events = []
#     query = request.GET.get('search', '')

#     if request.user.is_authenticated:
#         booked_events = Booking.objects.filter(
#             user=request.user).values_list('event_id', flat=True)

#     # Filter events based on search query if provided
#     if query:
#         events = events.filter(
#             Q(name__icontains=query) |
#             Q(location__icontains=query) |
#             Q(date__icontains=query)
#         )

#     return render(request, 'home.html', {
#         'events': events,
#         'booked_events': booked_events,
#         'search_query': query
#     })
def home(request):
    events = Event.objects.all()
    booked_events = []
    query = request.GET.get('search', '')
    category = request.GET.get('category', '')

    if request.user.is_authenticated:
        booked_events = Booking.objects.filter(
            user=request.user).values_list('event_id', flat=True)

    # Filter events based on search and category
    if query:
        events = events.filter(
            Q(name__icontains=query) |
            Q(location__icontains=query) |
            Q(date__icontains=query)
        )

    if category:
        events = events.filter(category=category)

    return render(request, 'home.html', {
        'events': events,
        'booked_events': booked_events,
        'search_query': query,
        'selected_category': category,
    })
