import json

class NetworkLayer:
    def __init__(self, ipAddress):
        # Initialize the NetworkLayer with an IP address
        self.ipAddress = ipAddress

    def send(self, data):
        # Create a JSON packet with the IP address and the data
        packet = json.dumps({"ipAddress": self.ipAddress, "data": data})
        print(f"[NetworkLayer] Sending packet: {packet}")
        return packet

    def receive(self, packet):
        print(f"[NetworkLayer] Received packet: {packet}")
        # Parse the JSON packet
        packet = json.loads(packet)
        ipAddress = packet["ipAddress"]
        data = packet["data"]
        
        # Check if the received IP address matches the expected IP address
        if ipAddress == self.ipAddress:
            print("[NetworkLayer] IP address matches")
            return data
        else:
            # Raise an error if there is an IP address mismatch
            raise ValueError("IP address mismatch")