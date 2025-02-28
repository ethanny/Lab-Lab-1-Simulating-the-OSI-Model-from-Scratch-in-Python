import socket
import threading
import pickle

class PhysicalLayer:
    def __init__(self, host='localhost', port=8080):
        # Initialize the PhysicalLayer with the host and port
        self.host = host
        self.port = port
        self.sock = None
        self.receivedData = None

    def startServer(self):
        def serverThread():
            # Create a server socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSock:
                serverSock.bind((self.host, self.port))
                serverSock.listen(1)
                print("[PhysicalLayer] Server listening...")
                # Accept a connection from a client
                conn, addr = serverSock.accept()
                with conn:
                    print(f"[PhysicalLayer] Connection established with {addr}")
                    # Receive data from the client
                    data = conn.recv(1024)
                    # Deserialize the received data using pickle
                    self.receivedData = pickle.loads(data)

        # Create and start a server thread
        self.serverThread = threading.Thread(target=serverThread)
        self.serverThread.start()

    def send(self, data):
        print(f"[PhysicalLayer] Sending data: {data}")
        # Create a client socket and connect to the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
            clientSocket.connect((self.host, self.port))
            # Serialize the data using pickle and send it to the server
            clientSocket.sendall(pickle.dumps(data))

    def receive(self):
        # Wait for the server thread to finish
        self.serverThread.join()
        print(f"[PhysicalLayer] Data received: {self.receivedData}")
        # Return the received data
        return self.receivedData
