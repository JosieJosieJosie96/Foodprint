from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Didyouknow
from .serializers import DidyouknowSerializer

class DidYouKnowViewSet(viewsets.ModelViewSet):
    queryset = Didyouknow.objects.all()
    serializer_class = DidyouknowSerializer

    def list(self, request, *args, **kwargs):
        data = list(Didyouknow.objects.all().values())
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        data = list(Didyouknow.objects.filter(id=kwargs['pk']).values())
        return Response(data)

    def create(self, request, *args, **kwargs):
        serializer = DidyouknowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Did You Know item added successfully", "status": status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Please provide valid details", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        item = Didyouknow.objects.filter(id=kwargs['pk'])
        if item.exists():
            item.delete()
            return Response({"message": "Did You Know item deleted successfully", "status": status.HTTP_204_NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "Did You Know item not found"}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        item = Didyouknow.objects.get(id=kwargs['pk'])
        serializer = DidyouknowSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Did You Know item updated successfully", "status": status.HTTP_200_OK}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Please provide valid details", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

