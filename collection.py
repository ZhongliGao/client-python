import engula.v1.collection_pb2

class collection:
    def __init__(self, coname, dbname, client):
        self.coname = coname
        self.dbname = dbname
        self.client = client

    def name(self):
        return self.coname

    async def desc(self):
        req = engula.v1.collection_pb2.DescribeCollectionRequest()
        req.name = self.coname
        res = self.collection_union_call(req)
        return res.CollectionDesc()


    def begin(self):
        #todo
        return

    def begin_with(self, databaseTxn):
        #todo
        return

    def object(self, object_id):
        #todo
        return



    async def collection_union_call(self, collection_request_union):
        return self.client.collection_union(collection_request_union)


