from rest_framework import status, viewsets
from rest_framework.response import Response

from todo.models import ToDo

from .serializer import ToDoSerializer


class ToDoViewSet(viewsets.ViewSet):

    # GETリクエスト(ユーザーの全てのtodoを取得)
    def list(self, request):
        todo = ToDo.objects.filter(user_id=request.user.id)
        todo = ToDoSerializer(todo, many=True)

        return Response(data={
            'todo': todo.data
        },
            status=status.HTTP_200_OK)

    # GETリクエスト(id指定でtodo単体取得)
    def retrieve(self, request, pk=None):
        todo = ToDo.objects.filter(user_id=request.user.id).filter(id=pk)
        if not todo:
            return Response(data={
                '許可がありません。'
            },
                status=status.HTTP_403_FORBIDDEN)

        todo = ToDoSerializer(todo, many=True)

        return Response(data={
            'todo': todo.data
        },
            status=status.HTTP_200_OK)

    # POSTリクエストで新規ToDoの追加
    def create(self, request):
        serializer = ToDoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data={
                'todo': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
