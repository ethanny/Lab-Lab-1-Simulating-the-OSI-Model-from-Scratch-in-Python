import json
import socket

class NetworkLayer:
    def __init__(self):
        # Initialize the NetworkLayer with an IP address
        self.ipAddress = self.get_local_ip()

    def get_local_ip(self):
        """Retrieve the local network IP address."""
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # Connect to an external server (Google DNS) but don't actually send data
            s.connect(("8.8.8.8", 80))
            ip_address = s.getsockname()[0]
        finally:
            s.close()
        return ip_address

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
