import engula.v1.engula_pb2
import engula.v1.engula_pb2_grpc
import engula.v1.database_pb2
import engula.v1.collection_pb2
import engula.v1.txn_pb2
import grpc


class Client:


    def connect(self, url):
        chan = grpc.insecure_channel(url)
        self.client =engula.v1.engula_pb2_grpc.EngulaStub(chan)
        return self.client

    async def txn(self,txnRequest):
        return self.client.Txn(txnRequest)

    async def database_txn(self, databaseTxnRequest):
        req = engula.v1.txn_pb2.TxnRequest()
        req.requests.append(databaseTxnRequest)
        return self.txn(req)

    async def collection_txn(self, dbname, collectionTxnRequest):
        req = engula.v1.txn_pb2.DatabaseTxnRequest()
        req.name = dbname
        req.requests.append(collectionTxnRequest)
        return self.database_txn(req)

    async def collection_exprs(self, dbname, coname, exprs):
        req = engula.v1.txn_pb2.CollectionTxnRequest()
        req.name = coname
        for expr in exprs:
            req.exprs.append(expr)
        return self.collection_txn(dbname, req)

    # async def collcetion_expr(self, dbname, coname, expr):
    #     exprs = []
    #     exprs.append(expr)
    #     self.collection_exprs(dbname, coname, exprs)



    async def database(self, databaseRequest):
        return self.client.Database(databaseRequest)

    async def database_union(self, database_request_union):
        req = engula.v1.database_pb2.DatabaseRequest()
        req_union = engula.v1.database_pb2.DatabaseRequestUnion()
        req_union.request = database_request_union
        req.requests.append(req_union)
        return self.database(req)

    async def collection(self, collectionRequest):
        return self.client.Collection(collectionRequest)

    async def collection_union(self, collcetion_request_union):
        req = engula.v1.collection_pb2.CollectionRequest()
        req_union = engula.v1.collection_pb2.CollectionRequestUnion()
        req_union.request = collcetion_request_union
        req.requests.append(req_union)
        return self.collection(req)



