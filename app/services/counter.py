from loguru import logger
import os
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY


class CustomIPCounter(object):
    def __init__(self):
        self.ips = []

    def register(self, payload):
        ip = payload["ip"]
        logger.debug(f"Registering ip {ip}")
        self.ips.append(ip)

    def collect(self):
        counter_metric = CounterMetricFamily(
            "unique_ip_counter", "Prometheus counter custom collector", labels=["app"]
        )
        counter_metric.add_metric(["ips"], len(list(set(self.ips))))
        yield counter_metric
