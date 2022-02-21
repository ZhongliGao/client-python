import proto.universe_pb2
import proto.universe_pb2_grpc
import collection as co

class database:
    def __init__(self,name, txn_client, universe_client):
        self.name = name
        self.txn_client = txn_client
        self.universe_client = universe_client

    async def desc(self):

        req = proto.universe_pb2.DescribeDatabaseRequest()
        req.name = self.name
        res = self.database_union_call(req)
        return res.desc




    def begin(self):
        database_txn = []
        database_txn.append(self.name)
        database_txn.append(self.txn_client)


    def collection(self, name):
        collection = co(name, self.name, self.txn_client, self.universe_client)
        return collection


    async def create_collection(self, name):
        desc = proto.universe_pb2.CollectionDesc()
        desc.name = name
        req = proto.universe_pb2.CreateCollectionRequest()
        req.desc = desc
        self.collection_union_call(req)


    async def delete_collection(self, name):
        desc = proto.universe_pb2.CollectionDesc
        desc.name = name
        req = proto.universe_pb2.DeleteCollectionRequest()
        req.desc = desc
        self.collection_union_call(req)




    async def database_union_call(self, database_request_union):
        return self.universe_client.database_union(database_request_union)


    async def collection_union_call(self, collection_request_union):
        return self.universe_client.collection_union(collection_request_union)
