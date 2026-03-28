from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer


# -------------------------------
# POST - Save Contact Form
# -------------------------------
@api_view(['POST'])
def create_contact(request):
    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()  # ✅ saves via Django ORM

        return Response({
            "success": True,
            "message": "Contact form submitted successfully"
        })

    return Response({
        "success": False,
        "errors": serializer.errors
    })


# -------------------------------
# GET - Fetch All Contacts
# -------------------------------
@api_view(['GET'])
def get_contacts(request):
    contacts = Contact.objects.all().order_by('-created_at')

    serializer = ContactSerializer(contacts, many=True)

    return Response({
        "success": True,
        "data": serializer.data
    })