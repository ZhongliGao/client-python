import proto.universe_pb2
import proto.universe_pb2_grpc


class universe_client:
    def __init__(self, chan):
        client = proto.universe_pb2_grpc.UniverseStub(chan)
        self.universe_client = client

    async def database(self, databaseRequest):
        return self.universe_client.Database(databaseRequest)

    async def database_union(self, database_request_union):
        req = proto.universe_pb2.DatabaseRequest()
        req_union = proto.universe_pb2.DatabaseRequestUnion()
        req_union.request = database_request_union
        req.DatabaseRequestUnion.append(req_union)
        return self.database(req)

    async def collection(self, collectionRequest):
        return self.universe_client.Collection(collectionRequest)

    async def collection_union(self, collcetion_request_union):
        req = proto.universe_pb2.CollectionRequest()
        req_union = proto.universe_pb2.CollectionRequestUnion()
        req_union.request = collcetion_request_union
        req.CollectionResponseUnion.append(req_union)
        return self.collection(req)



