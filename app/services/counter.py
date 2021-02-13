from loguru import logger


class CustomIPCounter(object):
    def __init__(self):
        self.ips = []

    def register(self, payload):
        ip = payload["ip"]
        logger.debug(f"Registering ip {ip}")
        self.ips.append(ip)
