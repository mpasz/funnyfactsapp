from rest_framework import status
from rest_framework.test import APIClient

class TestPostFunnyFact:
    def test_if_day_is_valid(self):

        client = APIClient()
        response = client.post('/dates', {'month': 12, 'day' : 20})

        assert response.status_code == status.HTTP_301_MOVED_PERMANENTLY
    
    def test_if_day_is_invalid(self):
        client = APIClient()
        response = client.post('/dates/', {'month': 12, 'day' : -1})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_if_month_is_valid(self):
        client = APIClient()
        response = client.post('/dates', {'month': 12, 'day' : 3})

        assert response.status_code == status.HTTP_301_MOVED_PERMANENTLY

    def test_if_month_is_invalid(self):
        client = APIClient()
        response = client.post('/dates/', {'month': 13, 'day' : 2})

        assert response.status_code == status.HTTP_400_BAD_REQUEST