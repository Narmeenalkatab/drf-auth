# from django.shortcuts import render
# from .models import Thing
# from .serializers import ThingSerializer
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# # Create your views here.
# from .permissions import OwnerOnly

# class ThinglistView(ListCreateAPIView):
#     queryset = Thing.objects.all()
#     serializer_class = ThingSerializer


# class ThingDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Thing.objects.all()
#     serializer_class = ThingSerializer
#     permission_classes =[OwnerOnly]


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({'message': 'This is a protected view!'})
