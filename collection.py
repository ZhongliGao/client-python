import proto.universe_pb2_grpc
import proto.universe_pb2

class collection:
    def __init__(self, coname, dbname, txn_client, universe_client):
        self.coname = coname
        self.dbname = dbname
        self.TxnClient = txn_client
        self.UniverseClient = universe_client


    async def desc(self):
        req = proto.universe_pb2.DescribeCollectionRequest()
        req.name = self.coname
        res = self.collection_union_call(req)
        return res.desc


    def begin(self):
        collectionTxn = CollectionTxn(None,self.TxnClient,self.CollectionDesc.database_id,self.CollectionDesc.id)
        return collectionTxn

    def begin_with(self, databaseTxn):
        collectionTxn = CollectionTxn(databaseTxn,self.TxnClient,self.CollectionDesc.database_id,self.CollectionDesc.id)
        return collectionTxn

    def object(self, object_id):
        Object = []
        Object.append(self.TxnClient)
        Object.append(object_id)
        Object.append(self.CollectionDesc.id)
        Object.append(self.CollectionDesc.database_id)
        return

    async def collection_expr_call(self, expr):
        return self.TxnClient.collcetion_expr(self.dbname, self.coname, expr)


    async def collection_union_call(self, collection_request_union):
        return self.UniverseClient.collection_union(collection_request_union)

class CollectionTxn:
    def __init__(self, DatabaseTxn, TxnClient,database_id, collection_id):
        self.DatabaseTxn = DatabaseTxn
        self.TxnClient = TxnClient
        self.database_id = database_id
        self.collection_id = collection_id
        self.exprs = []

    def add(self, MethodCallExpr):
        self.exprs.append(MethodCallExpr)


