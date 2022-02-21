import proto.universe_pb2
import proto.universe_pb2_grpc
import grpc
import database as db
import txn_client
import universe_client
class universe:
    def __init__(self, url):
        chan = grpc.insecure_channel(url)
        self.txn_client = txn_client(chan)
        self.universe_client = universe_client(chan)

    def database(self, name):
        database = db.database(name, self.txn_client, self.universe_client)
        return database

    async def createdatabase(self, name):
        req = proto.universe_pb2.DatabaseDesc()
        req.name = name
        req_union = proto.universe_pb2.CreateDatabaseRequest()
        req_union.desc = req
        self.database_union_call(req_union)

    async def deletedatabase(self, name):
        req = proto.universe_pb2.DeleteDatabaseRequest()
        req.name = name
        req_union = proto.universe_pb2.DeleteCollectionResponse()
        req_union.desc = req
        self.database_union_call(req_union)



    async def database_union_call(self, database_request_union):
        return self.universe_client.database_union(database_request_union)


