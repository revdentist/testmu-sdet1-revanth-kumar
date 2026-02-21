import pytest
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"

# Using JSONPlaceholder — a free, reliable REST API
# Perfect for demonstrating CRUD, error handling, and schema validation
# without needing auth tokens for a demo assignment


class TestAPI:
    """
    REST API tests against jsonplaceholder.typicode.com
    Covers: CRUD operations, error handling (4xx),
    schema validation, and response structure
    """

    def test_get_all_posts(self):
        """GET /posts should return 100 posts with correct schema"""
        response = requests.get(f"{BASE_URL}/posts")

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 100

        # Schema validation
        first_post = data[0]
        assert "id" in first_post
        assert "title" in first_post
        assert "body" in first_post
        assert "userId" in first_post

    def test_get_single_post(self):
        """GET /posts/1 should return correct post schema"""
        response = requests.get(f"{BASE_URL}/posts/1")

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert isinstance(data["title"], str)
        assert isinstance(data["body"], str)

    def test_create_post(self):
        """POST /posts should create and return new post"""
        payload = {
            "title": "TestMu AI Test Post",
            "body": "Automated test post created by Playwright framework",
            "userId": 1
        }

        response = requests.post(f"{BASE_URL}/posts", json=payload)

        assert response.status_code == 201
        data = response.json()
        assert data["title"] == payload["title"]
        assert data["body"] == payload["body"]
        assert "id" in data

    def test_update_post(self):
        """PUT /posts/1 should update and return modified post"""
        payload = {
            "id": 1,
            "title": "Updated Title",
            "body": "Updated body content",
            "userId": 1
        }

        response = requests.put(f"{BASE_URL}/posts/1", json=payload)

        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Updated Title"

    def test_delete_post(self):
        """DELETE /posts/1 should return 200"""
        response = requests.delete(f"{BASE_URL}/posts/1")

        assert response.status_code == 200

    def test_get_nonexistent_post_returns_404(self):
        """GET /posts/99999 should return 404"""
        response = requests.get(f"{BASE_URL}/posts/99999")

        assert response.status_code == 404

    def test_get_comments_for_post(self):
        """GET /posts/1/comments should return comments with schema"""
        response = requests.get(f"{BASE_URL}/posts/1/comments")

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0

        first_comment = data[0]
        assert "id" in first_comment
        assert "email" in first_comment
        assert "body" in first_comment

    def test_response_content_type_is_json(self):
        """API response should return JSON content type"""
        response = requests.get(f"{BASE_URL}/posts/1")

        assert "application/json" in response.headers["Content-Type"]

    def test_response_time_under_threshold(self):
        """API response should be under 3 seconds"""
        response = requests.get(f"{BASE_URL}/posts")

        assert response.elapsed.total_seconds() < 3.0