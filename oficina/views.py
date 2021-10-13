from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from rest_framework.status import HTTP_201_CREATED
from oficina.serializers import CarsSerializer, ClienteSerializer
from oficina.models import Cars, Cliente
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# class Views:
#     def get(model, request):
#         raise NotImplementedError
#     def post(model, item, request):
#         raise NotImplementedError
#     def delete(request):
#         raise NotImplementedError
#     def put(request):
#         raise NotImplementedError

# class CarsViewSet(Views):

#     @csrf_exempt
#     def get(request):
#         cars_views = Cars.objects.all()
#         serializer = CarsSerializer(cars_views, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     @csrf_exempt
#     def post(request):
#         convert_json = JSONParser().parse(request)
#         serializer = CarsSerializer(data=[convert_json], many=True)
#         if(serializer.is_valid()):
#             print(serializer.data)
#             serializer.save()
#             return HttpResponse('201')
#         return JsonResponse(serializer.errors, status=400)

#     @csrf_exempt
#     def delete(request):
#         print("Função delete")
#         convert_json = JSONParser().parse(request)
#         print(convert_json["id"])
#         try:
#             car_exists = Cars.objects.filter(id=convert_json["id"]).get()
#             car_exists.delete()
#             return HttpResponse('200')
#         except(Cars.DoesNotExist):
#             raise Http404('Carro não encontrado')


class MyViewSet:
    def __init__(self, model, serializerModel):
        self.model = model
        self.serializerModel = serializerModel

    @csrf_exempt
    def get(self, request):
        model = self.model
        serializerModel = self.serializerModel
        cars_views = model.objects.all()
        serializer = serializerModel(cars_views, many=True)
        return JsonResponse(serializer.data, safe=False)

    @csrf_exempt
    def post(self, request):
        serializerModel = self.serializerModel
        convert_json = JSONParser().parse(request)
        serializer = serializerModel(data=convert_json)
        if(serializer.is_valid()):
            serializer.save()
            return HttpResponse(status=201)
        return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def delete(self, request):
        model = self.model
        convert_json = JSONParser().parse(request)
        try:
            car_exists = model.objects.filter(id=convert_json["id"]).get()
            car_exists.delete()
            return HttpResponse(status=200)
        except(model.DoesNotExist):
            raise Http404('Carro não encontrado')

    @csrf_exempt
    def put(self, request):
        model = self.model
        convert_json = JSONParser().parse(request)
        try:
            model.objects.filter(id=convert_json["id"]).update(**convert_json)
            return HttpResponse(status=200)
        except(model.DoesNotExist):
            raise Http404('Carro não encontrado')

carViewSet = MyViewSet(Cars, CarsSerializer)
clienteViewSet = MyViewSet(Cliente, ClienteSerializer)
