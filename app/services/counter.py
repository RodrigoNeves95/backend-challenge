import os
from loguru import logger
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY


class CustomIPCounter(object):
    def __init__(self):
        logger.debug("Counter being initialized")
        self.ips = []

    def register(self, payload):
        ip = payload["ip"]
        logger.debug(os.getpid())
        logger.debug(f"Registering ip {ip}")
        self.ips.append(ip)

    def collect(self):
        counter_metric = CounterMetricFamily(
            "unique_ip_counter", "Prometheus counter custom collector", labels=["app"]
        )
        logger.debug(os.getpid())
        counter_metric.add_metric(["ips"], len(self.ips))
        logger.debug("---------------" * 3)
        yield counter_metric
