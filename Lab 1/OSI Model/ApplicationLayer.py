class ApplicationLayer:
    def send(self, data):
        # Construct a request string with the data
        request = f"REQUEST:{data}"
        print(f"[ApplicationLayer] Sending request: {request}")
        return request

    def receive(self, request):
        # Check if the request string starts with "REQUEST:"
        if request.startswith("REQUEST:"):
            # Extract the actual data from the request string
            data = request[len("REQUEST:") :]
            # Construct a response string with the extracted data
            response = f"RESPONSE:{data}"
            print(f"[ApplicationLayer] Sending response: {response}")
            return response
        else:
            # Raise an error if the request format is invalid
            raise ValueError("Invalid request")
