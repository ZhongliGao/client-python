import engula.v1.database_pb2
import engula.v1.collection_pb2
import database as db
import client as cli
class universe:

    def connect(self, url):
        self.client = cli.Client.connect(url)

    def database(self, name):
        database = db.database(name, self.client)
        return database

    async def createdatabase(self, name):
        req = engula.v1.database_pb2.DatabaseDesc()
        req.name = name
        req_union = engula.v1.database_pb2.CreateDatabaseRequest()
        req_union.desc = req
        self.database_union_call(req_union)

    async def deletedatabase(self, name):
        req = engula.v1.database_pb2.DeleteDatabaseRequest()
        req.name = name
        self.database_union_call(req)



    async def database_union_call(self, database_request_union):
        return self.client.database_union(database_request_union)

