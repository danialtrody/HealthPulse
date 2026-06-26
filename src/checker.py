import requests
import time
from src.logger import setup_logger

logger = setup_logger()

TIMEOUT = 5

def check_service(name, url):
    logger.info(f"Checking {name}...")
    
    try:
        start = time.time()
        response = requests.get(url, timeout=TIMEOUT)
        end = time.time()

        result = {
            "name": name,
            "url": url,
            "status": "healthy",
            "status_code": response.status_code,
            "response_time": round(end - start, 2)
        }

        logger.info(f"{name} is healthy | status_code={result['status_code']} | response_time={result['response_time']}s")
        return result

    except requests.exceptions.Timeout:
        logger.warning(f"{name} timed out after {TIMEOUT}s")
        return {
            "name": name,
            "url": url,
            "status": "unhealthy",
            "reason": "timeout"
        }

    except requests.exceptions.ConnectionError:
        logger.error(f"{name} connection failed")
        return {
            "name": name,
            "url": url,
            "status": "unhealthy",
            "reason": "connection error"
        }

def check_all_services(services):
    for name, url in services.items():
        yield check_service(name, url)