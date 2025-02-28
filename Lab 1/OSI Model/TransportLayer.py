import json

class TransportLayer:
    def send(self, data):
        # Split the data into segments of 10 characters each
        segments = [data[i:i+10] for i in range(0, len(data), 10)]
        print(f"[TransportLayer] Sending segments: {segments}")
        # Convert the segments list to a JSON string
        return json.dumps(segments)

    def receive(self, segments):
        # Convert the JSON string back to a list of segments
        segments = json.loads(segments)
        # Reconstruct the original data by joining the segments
        data = ''.join(segments)
        print(f"[TransportLayer] Reconstructed data: {data}")
        return data
