import engula.v1.database_pb2
import engula.v1.collection_pb2
import collection as co

class database:
    def __init__(self, name, client):
        self.name = name
        self.client = client


    async def desc(self):
        req = engula.v1.database_pb2.DescribeDatabaseRequest()
        req.name = self.name
        res = self.database_union_call(req)
        return res.DatabaseDesc()




    def begin(self):
        #todo
        database_txn = []
        database_txn.append(self.name)
        database_txn.append(self.client)


    def collection(self, name):
        collection = co(name, self.name, self.client)
        return collection


    async def create_collection(self, name):
        desc = engula.v1.collection_pb2.CollectionDesc()
        desc.name = name
        req = engula.v1.collection_pb2.CreateCollectionRequest()
        req.desc = desc
        self.collection_union_call(req)


    async def delete_collection(self, name):
        desc = engula.v1.collection_pb2.CollectionDesc()
        desc.name = name
        req = engula.v1.collection_pb2.DeleteCollectionRequest()
        req.desc = desc
        self.collection_union_call(req)




    async def database_union_call(self, database_request_union):
        return self.client.database_union(database_request_union)


    async def collection_union_call(self, collection_request_union):
        return self.client.collection_union(collection_request_union)
