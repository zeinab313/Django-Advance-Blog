from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from datetime import datetime
from accounts.models import User

#ساخت یک فیکچر برای کلاینت
@pytest.fixture
def api_client():
    client = APIClient()
    return client

#ساخت یک فیکچر برای ساخت یک کاربر
@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="admin@admin.com", password="a/@1234567", is_verified=True
    )
    return user

#تست گرفتن ریسپانس درست هنگام گت کرن
@pytest.mark.django_db
class TestPostApi:
    def test_get_post_response_200_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 200

#تست انجام عملیات ثبت اگر لاگین نبود
    def test_create_post_response_401_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 401
#تست انجام عملیات ثبت اگر لاگین بود
    def test_create_post_response_201_status(self, api_client, common_user):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": datetime.now(),
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201

#تست انجام عملیات ثبت با انجام عملیات ولیدیشن
    def test_create_post_invalid_data_response_400_status(
        self, api_client, common_user
    ):
        url = reverse("blog:api-v1:post-list")
        data = {"title": "test", "content": "description"}
        user = common_user

        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400