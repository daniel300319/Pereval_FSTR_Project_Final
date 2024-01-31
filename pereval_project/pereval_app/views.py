from rest_framework.generics import CreateAPIView
from .serializers import PerevalSerializer, UserSerializer


class PerevalCreateView(CreateAPIView):
    serializer_class = PerevalSerializer

    def create(self, request, *args, **kwargs):
        user_data = request.data.pop('user', None)
        user_serializer = UserSerializer(data=user_data)

        if user_serializer.is_valid():
            user = user_serializer.save()
            request.data['user'] = user.id

        response = super().create(request, *args, **kwargs)
        response.data['message'] = 'Отправлено успешно'
        return response
