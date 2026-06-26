from datetime import datetime
from src.logger import setup_logger


logger = setup_logger()

HEALTHY_ICON = "✅"
UNHEALTHY_ICON = "❌"
SEPARATOR = "=" * 42


def get_summary(results):
    total = len(results)
    healthy = sum(1 for r in results if r["status"] == "healthy")
    unhealthy = total - healthy

    return {
        "total": total,
        "healthy": healthy,
        "unhealthy": unhealthy
    }
    

def generate_report(results):
    logger.info("Generating report...")
    
    summary = get_summary(results)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(SEPARATOR)
    print(f"        HealthPulse Report")
    print(f"        {now}")
    print(SEPARATOR)
    print()

    for result in results:
        if result["status"] == "healthy":
            icon = HEALTHY_ICON
            detail = f"{result['response_time']}s"
        else:
            icon = UNHEALTHY_ICON
            detail = result["reason"]

        print(f"{icon} {result['name']:<20} | {result['status']:<10} | {detail}")

    print()
    print("-" * 42)
    print(f"Total:     {summary['total']} services")
    print(f"Healthy:   {summary['healthy']}")
    print(f"Unhealthy: {summary['unhealthy']}")
    print(SEPARATOR)

    logger.info(f"Report done | healthy={summary['healthy']} unhealthy={summary['unhealthy']}")