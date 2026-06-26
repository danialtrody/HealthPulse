from prometheus_client import Counter, Gauge, start_http_server

CHECKS_TOTAL = Counter(
    'healthpulse_checks_total',
    'Total number of checks performed'
)

HEALTHY_TOTAL = Counter(
    'healthpulse_healthy_total',
    'Total number of healthy checks'
)

UNHEALTHY_TOTAL = Counter(
    'healthpulse_unhealthy_total',
    'Total number of unhealthy checks'
)

RESPONSE_TIME = Gauge(
    'healthpulse_response_time_seconds',
    'Response time of last check in seconds',
    ['service']
)


def record_result(result):
    CHECKS_TOTAL.inc()

    if result["status"] == "healthy":
        HEALTHY_TOTAL.inc()
        RESPONSE_TIME.labels(service=result["name"]).set(result["response_time"])
    else:
        UNHEALTHY_TOTAL.inc()
       
        
def start_metrics_server(port=8000):
    start_http_server(port)
    print(f"Metrics server running on http://localhost:{port}/metrics")
    


#  cd ~/Desktop/prometheus
# ./prometheus.exe
# http://localhost:9090



# cd ~/Desktop/grafana
# ./bin/grafana.exe server
# http://localhost:3000
