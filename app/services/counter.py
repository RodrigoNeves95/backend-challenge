from loguru import logger


class CustomIPCounter(object):
    def __init__(self):
        self.ips = []

    def register(self, payload):
        logger.debug(f"Registering ip {ip}")
        ip = payload["ip"]
        self.ips.append(ip)
