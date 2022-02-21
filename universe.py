import proto.universe_pb2
import proto.universe_pb2_grpc
import grpc
import database as db
import txn_client
import universe_client
class universe:
    def __init__(self,url):
        chan = grpc.insecure_channel(url)
        self.txn_client = txn_clietn(chan)
        self.universe_client = universe_client(chan)




    def database(self, name):
        database = db.database(name, self.txn_client, self.universe_client)
        return database


    async def createdatabase(self, name):
        req = proto.universe_pb2.CreateDatabaseRequest(name)

        res = proto.universe_pb2.CreateDatabaseResponse(req)
        # database_union_call()
        return res


    async def deletedatabase(self, name):
        req = proto.universe_pb2.DeleteDatabaseRequest(name)
        #database_union_call()
        res = proto.universe_pb2.DeleteCollectionResponse(req)
        return res


    async def database_union_call(self):
        return

