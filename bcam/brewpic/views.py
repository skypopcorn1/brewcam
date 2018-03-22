import os
from django.conf import settings
from .models import Images
from rest_framework.views import APIView
from rest_framework.parsers import (FormParser, MultiPartParser)
from rest_framework.response import Response
from .serializers import ImageSerializer

class FileUploadView(APIView):
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = ImageSerializer

    def post(self, request, filename, format=None):
        serializers = ImageSerializer(data=request.data)
        file_obj = request.data['file']
        filepath = os.path.join(settings.MEDIA_ROOT, filename)
        with open(filepath, 'wb+') as temp_file:
            for chunk in file_obj.chunks():
                temp_file.write(chunk)

        return Response(status=204)
