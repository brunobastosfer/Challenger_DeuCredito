from rest_framework.test import APITestCase
from rest_framework.utils.json import dump
from oficina.models import Cars, Cliente
from django.urls import reverse
from rest_framework import status
import json

class CarsTestCase(APITestCase):

    def  setUp(self):
        # self.list_url = reverse('cars/')
        self.cars_1 = Cars.objects.create(
            name="CarroTeste", model = '1'
        )
        self.cars_2 = Cars.objects.create(
            name="CarroTeste2", model = '2'
        )

    def test_req_get_cars(self):
        """Teste a requisição GET para listar carros"""
        response = self.client.get('http://127.0.0.1:8000/cars/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_req_get_clientes(self):
        """Teste a requisição GET para listar clientes"""
        response = self.client.get('http://127.0.0.1:8000/clientes/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_req_post_car(self):
        """"Teste a requisição POST para criar um carro"""
        data = {
            "name":"Malveri",
            "model": '2'
        }
        response = self.client.post('http://127.0.0.1:8000/cars/post', data=json.dumps(data), content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_req_post_cliente(self):
        """Testa a requisição POST para criar um cliente"""
        data = {
            "name": "Bruno",
            "address": "Rua Dourada",
            "car_model": 2
        }
        response = self.client.post('http://127.0.0.1:8000/clientes/post', data=json.dumps(data), content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_req_put_car(self):
        """Teste para verificar a requisição PUT para atualizar um carro."""
        data = {
            "id": 1,
            "name": "Doblô",
            "model": "2"
        }
        response = self.client.put('http://127.0.0.1:8000/cars/put', data=json.dumps(data), content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_req_put_client(self):
        """Teste para verificar a requisição PUT para atualizar um cliente."""
        data = {
            "id": 1,
            "name": "Bastos",
            "address": "Dourada",
            "car_model": 2
        }
        response = self.client.put('http://127.0.0.1:8000/clientes/put', data=json.dumps(data), content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_req_delete_car(self):
        """Testa a requisição DELETE para deletar um carro"""
        data = {
            "id": 1,
        }
        response = self.client.delete('http://127.0.0.1:8000/cars/delete', data=json.dumps(data), content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)