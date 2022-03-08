from functools import partial
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import status


def list(request, model_class, serializer_class):

    if request.method == 'GET':
        list = model_class.objects.all()
        serializer = serializer_class(list, many=True,context={'request':request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializer_class(data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def detail(request, uuid, model_class, serializer_class):

    model = get_object_or_404(model_class, uuid=uuid)

    if request.method == 'GET':
        serializer = serializer_class(model)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializer_class(model, data=request.data,context={'request':request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)