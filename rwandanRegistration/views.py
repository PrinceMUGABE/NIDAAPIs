from rest_framework import viewsets
from rest_framework.response import Response
from .models import Rwandan
from .serializers import RwandanSerializer

class RwandanViewSet(viewsets.ViewSet):

    def list_all(self, request):
        queryset = Rwandan.objects.all()
        serializer = RwandanSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = RwandanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update_by_id(self, request, pk):
        try:
            rwandan = Rwandan.objects.get(pk=pk)
        except Rwandan.DoesNotExist:
            return Response({'error': 'Rwandan not found'}, status=404)

        serializer = RwandanSerializer(rwandan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def update_by_identity_no(self, request, identity_no):
        try:
            rwandan = Rwandan.objects.get(identity_No=identity_no)
        except Rwandan.DoesNotExist:
            return Response({'error': 'Rwandan not found'}, status=404)

        serializer = RwandanSerializer(rwandan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete_by_id(self, request, pk):
        try:
            rwandan = Rwandan.objects.get(pk=pk)
        except Rwandan.DoesNotExist:
            return Response({'error': 'Rwandan not found'}, status=404)

        rwandan.delete()
        return Response({'success': 'Rwandan deleted'}, status=204)

    def delete_by_identity_no(self, request, identity_no):
        try:
            rwandan = Rwandan.objects.get(identity_No=identity_no)
        except Rwandan.DoesNotExist:
            return Response({'error': 'Rwandan not found'}, status=404)

        rwandan.delete()
        return Response({'success': 'Rwandan deleted'}, status=204)

    def retrieve_by_id(self, request, pk):
        try:
            rwandan = Rwandan.objects.get(pk=pk)
        except Rwandan.DoesNotExist:
            return Response({'error': 'Rwandan not found'}, status=404)

        serializer = RwandanSerializer(rwandan)
        return Response(serializer.data)

    def retrieve_by_identity_no(self, request, identity_no):
        try:
            rwandan = Rwandan.objects.get(identity_No=identity_no)
        except Rwandan.DoesNotExist:
            return Response({'error': 'Rwandan not found'}, status=404)

        serializer = RwandanSerializer(rwandan)
        return Response(serializer.data)