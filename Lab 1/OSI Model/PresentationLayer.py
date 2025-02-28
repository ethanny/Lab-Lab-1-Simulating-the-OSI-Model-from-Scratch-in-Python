import base64

class PresentationLayer:
    def send(self, data):
        # Encode the data to Base64 and then decode it to a string
        encodedData = base64.b64encode(data.encode()).decode()
        print(f"[PresentationLayer] Encoded data: {encodedData}")
        return encodedData

    def receive(self, encodedData):
        # Decode the Base64 encoded data to its original string format
        data = base64.b64decode(encodedData.encode()).decode()
        print(f"[PresentationLayer] Decoded data: {data}")
        return data
