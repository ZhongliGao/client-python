import proto.universe_pb2
import proto.universe_pb2_grpc
import collection as co

class database:
    def __init__(self,name, txn_client, universe_client):
        self.name = name
        self.txn_client = txn_client
        self.universe_client = universe_client

    async def desc(self):

        req = proto.universe_pb2.DescribeDatabaseRequest(self.name)
        #database_union_call
        res = proto.universe_pb2.DescribeDatabaseResponse(req)
        return res


    def begin(self):
        database_txn = []
        database_txn.append(self.name)
        database_txn.append(self.txn_client)


    def collection(self,name):
        collection = co(name,self.name,self.txn_client,self.universe_client)
        return collection


    async def create_collection(self, name):
        desc = proto.universe_pb2.CollectionDesc
        desc.name = name
        req = proto.universe_pb2.CreateCollectionRequest(desc)
        #collection_union_call()


    async def delete_collection(self, name):
        desc = proto.universe_pb2.CollectionDesc
        desc.name = name
        req = proto.universe_pb2.DeleteCollectionRequest(name)
        #collection_union_call()




    async def database_union_call(self):
        return

    async def collection_union_call(self):
        return