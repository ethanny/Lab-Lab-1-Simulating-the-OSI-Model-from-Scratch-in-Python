import json
from PhysicalLayer import PhysicalLayer
from DataLinkLayer import DataLinkLayer
from NetworkLayer import NetworkLayer
from TransportLayer import TransportLayer
from SessionLayer import SessionLayer
from PresentationLayer import PresentationLayer
from ApplicationLayer import ApplicationLayer

#OSI Model Simulation
def main():
    # Initialize each layer of the OSI model
    physical = PhysicalLayer()
    physical.startServer()

    datalink = DataLinkLayer()
    network = NetworkLayer()
    transport = TransportLayer()
    session = SessionLayer()
    presentation = PresentationLayer()
    application = ApplicationLayer()

    # Establish a session connection
    session.establishConnection()

    # Data to be sent through the OSI layers
    data = "Hello, World!"
    
    # Application layer processing
    appData = application.send(data)
    
    # Presentation layer processing
    presentationData = presentation.send(appData)
    
    # Session layer processing
    sessionData = session.send(presentationData)
    
    # Transport layer processing
    transportSegments = transport.send(sessionData)
    
    # Network layer processing
    networkPackets = [network.send(segment) for segment in json.loads(transportSegments)]
    
    # Data link layer processing
    datalinkFrames = [datalink.send(packet) for packet in networkPackets]
    
    # Physical layer processing
    physicalData = '\n'.join(datalinkFrames)
    physical.send(physicalData)

    # Receiving data back through the OSI layers
    receivedPhysicalData = physical.receive()
    receivedDatalinkFrames = receivedPhysicalData.split('\n')
    receivedNetworkPackets = [datalink.receive(frame) for frame in receivedDatalinkFrames]
    receivedTransportSegments = json.dumps([network.receive(packet) for packet in receivedNetworkPackets])
    receivedSessionData = transport.receive(receivedTransportSegments)
    receivedPresentationData = session.receive(receivedSessionData)
    receivedAppData = presentation.receive(receivedPresentationData)
    receivedData = application.receive(receivedAppData)

    # Print the final received data
    print("[Main] Final received data: ", receivedData)

if __name__ == "__main__":
    main()