import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """A test client for the FastAPI application."""
    return TestClient(app)