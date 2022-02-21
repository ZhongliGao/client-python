import proto.txn_pb2
import proto.txn_pb2_grpc
class txn_client:
    def __init__(self,chan):
        client = proto.txn_pb2_grpc.TxnStub(chan)
        self.txn_client = client


    async def batch(self, batchTxnRequest):
        return self.txn_client.Batch(batchTxnRequest)

    async def database(self, databaseTxnRequest):
        req = proto.txn_pb2.BatchTxnRequest()
        req.BatchTxnRequest.append(databaseTxnRequest)
        return self.batch(req)

    async def collection(self, dbname, collectionTxnRequest):
        req = proto.txn_pb2.DatabaseTxnRequest()
        req.name = dbname
        req.DatabaseTxnRequest.append(collectionTxnRequest)
        return self.database(req)

    async def collection_exprs(self, dbname, coname, exprs):
        req = proto.txn_pb2.CollectionTxnRequest()
        req.name = coname
        req.exprs.append(exprs)
        return self.collection(dbname, req)

    async def collcetion_expr(self, dbname, coname, expr):
        exprs = []
        exprs.append(expr)
        self.collection_exprs(dbname, coname, exprs)
