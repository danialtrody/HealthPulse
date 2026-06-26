import pytest
from src.reporter import get_summary


@pytest.fixture
def healthy_results():
    return [
        {"name": "GitHub", "status": "healthy", "response_time": 0.2},
        {"name": "JSONPlaceholder", "status": "healthy", "response_time": 0.5},
        {"name": "HTTPBin", "status": "healthy", "response_time": 0.7}
    ]

@pytest.fixture
def unhealthy_results():
    return [
        {"name": "GitHub", "status": "unhealthy", "reason": "timeout"},
        {"name": "JSONPlaceholder", "status": "unhealthy", "reason": "connection error"},
        {"name": "HTTPBin", "status": "unhealthy", "reason": "timeout"}
    ]

@pytest.fixture
def mixed_results():
    return [
        {"name": "GitHub", "status": "healthy", "response_time": 0.2},
        {"name": "JSONPlaceholder", "status": "unhealthy", "reason": "timeout"},
        {"name": "HTTPBin", "status": "healthy", "response_time": 0.7}
    ]
    

def test_summary_all_healthy(healthy_results):
    summary = get_summary(healthy_results)

    assert summary["total"] == 3
    assert summary["healthy"] == 3
    assert summary["unhealthy"] == 0

def test_summary_all_unhealthy(unhealthy_results):
    summary = get_summary(unhealthy_results)

    assert summary["total"] == 3
    assert summary["healthy"] == 0
    assert summary["unhealthy"] == 3

def test_summary_mixed(mixed_results):
    summary = get_summary(mixed_results)

    assert summary["total"] == 3
    assert summary["healthy"] == 2
    assert summary["unhealthy"] == 1