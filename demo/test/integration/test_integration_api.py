# test_api.py
import requests
import pytest
import time

def test_health_check():
  response = requests.get("http://localhost:8000/health")
  assert response.status_code == 200
  assert response.json() == {"status": "healthy"}

def test_hello_world():
  response = requests.get("http://localhost:8000/")
  assert response.status_code == 200
  assert response.json() == {"message": "Hello World"}
