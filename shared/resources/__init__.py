from flask_resources import ResponseHandler
from .serializers.iso19139 import ISO19139Serializer

lter_serializers = {"text/xml": ResponseHandler(
    ISO19139Serializer()
)}
