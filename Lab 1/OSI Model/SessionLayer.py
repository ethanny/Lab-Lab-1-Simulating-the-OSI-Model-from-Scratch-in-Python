class SessionLayer:
    def __init__(self):
        # Initialize the SessionLayer with a disconnected state
        self.connected = False

    def establishConnection(self):
        # Establish a session connection by setting the state to connected
        self.connected = True
        print("[SessionLayer] Session established")

    def terminateConnection(self):
        # Terminate the session connection by setting the state to disconnected
        self.connected = False
        print("[SessionLayer] Session terminated")

    def send(self, data):
        # Send data only if the session is established
        if self.connected:
            print(f"[SessionLayer] Sending data: {data}")
            return data
        else:
            # Raise an error if the session is not established
            raise ValueError("Session not established")

    def receive(self, data):
        # Receive data only if the session is established
        if self.connected:
            print(f"[SessionLayer] Received data: {data}")
            return data
        else:
            # Raise an error if the session is not established
            raise ValueError("Session not established")
