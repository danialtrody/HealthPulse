from src.checker import check_all_services
from src.reporter import generate_report

services = {
    "GitHub": "https://api.github.com",
    "JSONPlaceholder": "https://jsonplaceholder.typicode.com",
    "HTTPBin": "https://httpbin.org"
}

results = list(check_all_services(services))
generate_report(results)