import proto.universe_pb2
import proto.universe_pb2_grpc
import grpc

class universe_client:
    def __init__(self, chan):
        client = proto.universe_pb2_grpc.UniverseStub(chan)
        self.universe_client = client



