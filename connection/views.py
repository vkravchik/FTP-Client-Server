from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import Connection
from .serializer import ConnectionSerializer


@api_view(['GET', 'POST'])
@csrf_exempt
def get_or_post(request):
    if request.method == 'GET':
        connections = Connection.objects.all()
        serializer = ConnectionSerializer(connections, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ConnectionSerializer(data=request.data)

        is_exist = Connection.objects.filter(host=request.data.get('host'), isSFTP=request.data.get('isSFTP')).count()

        if serializer.is_valid() and is_exist == 0:
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def get_or_put_or_delete(request, pk):
    try:
        connection = Connection.objects.get(pk=pk)
    except Connection.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ConnectionSerializer(connection)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ConnectionSerializer(connection, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        connection.delete()
        return Response(status=204)
