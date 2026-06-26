import pytest
from unittest.mock import patch, Mock
from src.checker import check_service
import requests



def test_service_healthy():
    mock_response = Mock()
    mock_response.status_code = 200

    with patch("src.checker.requests.get", return_value=mock_response):
        result = check_service("GitHub", "https://api.github.com")

    assert result["status"] == "healthy"
    assert result["status_code"] == 200
    assert result["name"] == "GitHub"
    assert result["response_time"] >= 0
    

def test_service_timeout():
    with patch("src.checker.requests.get", side_effect=requests.exceptions.Timeout):
        result = check_service("GitHub", "https://api.github.com")

    assert result["status"] == "unhealthy"
    assert result["reason"] == "timeout"
    assert result["name"] == "GitHub"
    
    
def test_service_connection_error():
    with patch("src.checker.requests.get", side_effect=requests.exceptions.ConnectionError):
        result = check_service("GitHub", "https://api.github.com")

    assert result["status"] == "unhealthy"
    assert result["reason"] == "connection error"
    assert result["name"] == "GitHub"