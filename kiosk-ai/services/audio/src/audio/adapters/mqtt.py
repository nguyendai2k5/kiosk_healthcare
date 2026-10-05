class MqttAdapter:
    def __init__(self, broker_url: str = "mqtt://localhost:1883") -> None:
        self.broker_url = broker_url

    def connect(self) -> bool:
        return True
