from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import *


class PerevalAPIView(viewsets.ViewSet):

    def serializer_error_response(self, errors):
        message = ''
        for k, v in errors.items():
            message += f'{k}: {str(*v)}'
        return Response({'message': message, 'id': None}, status=400)

    def submitData(self, request):

        try:
            data = request.data

            try:
                user = User.objects.get(email=data['user']['email'])
                serializer = UserSerializer(user, data=data['user'])
            except:
                serializer = UserSerializer(data=data['user'])

            if serializer.is_valid():
                user = serializer.save()
            else:
                return self.serializer_error_response(serializer.errors)

            serializer = CoordSerializer(data=data['coord'])
            if serializer.is_valid():
                coord_new = serializer.save()
            else:
                return self.serializer_error_response(serializer.errors)

            data['user'] = user.id
            data['coord'] = coord_new.id
            data['winter_level'] = data['level']['winter']
            data['summer_level'] = data['level']['summer']
            data['autumn_level'] = data['level']['autumn']
            data['spring_level'] = data['level']['spring']
            data.pop('coord')
            data.pop('level')

            serializer = PerevalSerializer(data=data)
            if serializer.is_valid():
                pereval_new = serializer.save()
            else:
                return self.serializer_error_response(serializer.errors)

            images = data['images']
            for image in images:
                image['pereval'] = pereval_new.id
                image['img'] = image['data']
                image.pop('data')
                serializer = ImagesSerializer(data=image)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return self.serializer_error_response(serializer.errors)

            return Response({'message': None, 'id': pereval_new.id}, status=200)

        except Exception as inst:
            return Response({'message': str(inst), 'id': None}, status=500)