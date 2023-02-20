import prometheus_client as prom

# These two packages are used for creating the extra metrics in the sample
from random import randrange
import time

# Variables definition
my_counter = prom.Counter('my_counter', 'Random number between 1 - 100')
my_gauge = prom.Gauge('my_gauge', 'Random number between 1 - 100')
my_summary = prom.Summary('my_summary', 'Random number between 1 - 100')
my_histogram = prom.Histogram(
    'my_histogram', 'Random number between 1 - 100')


def generate_random_metrics():
    """Generate random metrics.

    Creates random numbers and assign them to the variables.
    """
    while True:
        random_number = randrange(10)
        my_counter.inc(random_number)
        my_gauge.set(random_number)
        my_summary.observe(random_number)
        my_histogram.observe(random_number)
        time.sleep(5)


if __name__ == '__main__':
    """Create HTTP server that's gonna watch for the Prometheus."""
    prom.start_http_server(8000)
    generate_random_metrics()
