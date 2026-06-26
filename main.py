from src.checker import check_all_services
from src.reporter import generate_report
from src.metrics import record_result, start_metrics_server
import time

services = {
    "GitHub": "https://api.github.com",
    "JSONPlaceholder": "https://jsonplaceholder.typicode.com",
    "HTTPBin": "https://httpbin.org"
}

start_metrics_server(port=8000)

while True:
    results = list(check_all_services(services))
    
    for result in results:
        record_result(result)
    
    generate_report(results)
    
    print("\nWaiting 30 seconds...\n")
    time.sleep(30) 
    
    