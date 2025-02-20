from rest_framework import generics, status,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Event, Ticket
from .serializers import UserSerializer, EventSerializer
from .permissions import IsAdminRole ,IsUserRole


class RegisterUser(generics.CreateAPIView):
    """API to register users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class CreateEvent(generics.CreateAPIView):
    """API to create events (Admin only)"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminRole]

    def perform_create(self, serializer):
        if self.request.user.role != 'admin':
            return Response({"error": "Only admins can create events"}, status=status.HTTP_403_FORBIDDEN)
        serializer.save()


class EventList(generics.ListAPIView):
    """API to list all events"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]


class PurchaseTicketView(APIView):
    """API to purchase tickets"""
    permission_classes = [permissions.IsAuthenticated,IsUserRole]

    def post(self, request, event_id):
        event = Event.objects.get(id=event_id)
        quantity = request.data.get('quantity')

        if event.tickets_sold + quantity > event.total_tickets:
            return Response({"error": "Not enough tickets available"}, status=status.HTTP_400_BAD_REQUEST)

        event.tickets_sold += quantity
        event.save()

        Ticket.objects.create(user=request.user, event=event, quantity=quantity)

        return Response({"message": "Tickets purchased successfully"}, status=status.HTTP_201_CREATED)
