import proto.txn_pb2
import proto.txn_pb2_grpc
class txn_client:
    def __init__(self,chan):
        client = proto.txn_pb2_grpc.TxnStub(chan)
        self.txn_client = client
    