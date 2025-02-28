import json

class DataLinkLayer:
    def __init__(self, macAddress):
        # Initialize the DataLinkLayer with a MAC address
        self.macAddress = macAddress

    def send(self, data):
        # Create a JSON frame with the MAC address and the data
        frame = json.dumps({"macAddress": self.macAddress, "data": data})
        print(f"[DataLinkLayer] Sending frame: {frame}")
        return frame

    def receive(self, frame):
        print(f"[DataLinkLayer] Received frame: {frame}")
        try:
            # Parse the JSON frame
            frame = json.loads(frame)
            macAddress = frame["macAddress"]
            data = frame["data"]
            
            # Check if the received MAC address matches the expected MAC address
            if macAddress == self.macAddress:
                print("[DataLinkLayer] MAC address matches")
                return data
            else:
                # Raise an error if there is a MAC address mismatch
                raise ValueError(f"MAC address mismatch: expected {self.macAddress}, got {macAddress}")
        except ValueError as e:
            # Handle any ValueError exceptions
            print(f"[DataLinkLayer] Error: {e}")
            raise
