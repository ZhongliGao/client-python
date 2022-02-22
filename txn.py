import engula.v1.txn_pb2
import engula.v1.expr_pb2
class DatabaseTxn:
    def __init__(self, databaseTxnInner):
        self.inner = databaseTxnInner


    def new(self, dbname, client):
        handle = DatabaseTxnHandle(dbname,client)
        requests = []
        self.inner = DatabaseTxnInner(handle,requests)
        return self.inner

    def collection(self, coname):
        return

    def commit(self):
        handle = self.inner.handle
        req = engula.v1.txn_pb2.DatabaseTxnRequest()
        req.name = handle.dbname
        for request in self.inner.requests:
            req.requests.append(request)
        handle.client.database_txn(req)

class DatabaseTxnInner:
    def __init__(self,databaseTxnHandle, CollectionTxnRequest):
        self.handle = databaseTxnHandle
        if len(CollectionTxnRequest) == 0:
            self.requests = []
        else:
            self.requests = CollectionTxnRequest


class DatabaseTxnHandle:
    def __init__(self, dbname, client):
        self.dbname = dbname
        self.client = client



class CollectionTxn:
    def __init__(self, collectionTxnInner,txn):
        self.inner = collectionTxnInner
        self.subtxn = txn

    def new(self, dbname, coname, client):
        handle = CollectionTxnHandle(dbname,coname,client)
        self.new_inner(coname,handle,None)

    def new_inner(self, coname, handle, parent):
        inner = CollectionTxnInner(coname,handle,parent,[])
        self.inner = inner
        self.subtxn = None
        return self

    def object(self):
        return

    async def commit(self):
        req = engula.v1.CollectionTxnRequest()
        req.name = self.inner.coname
        for expr in self.inner.exprs:
            req.exprs.append(expr)
        handle = self.inner.handle
        if handle is not None:
            handle.client.collection_txn(handle.dbname,req)
        else:
            parent = self.inner.parent
            parent.requests.append(req)


    def object_txn(self):
        return

    def object_set(self):
        return

    def object_delete(self):
        return

class CollectionTxnInner:
    def __init__(self, coname, databaseTxnHandle,databaseTxnInner, expr):
        self.coname = coname
        self.handle = databaseTxnHandle
        self.parent = databaseTxnInner
        if len(expr) == 0:
            self.exprs = []
        else:
            self.exprs = expr

class CollectionTxnHandle:
    def __init__(self,dbname,coname,client):
        self.dbname = dbname
        self.coname = coname
        self.client = client






class Txn:
    def __init__(self,collectionTxnInner,collectionTxnHandle,expr):
        self.handle = collectionTxnHandle
        self.parent = collectionTxnInner
        self.expr = expr


    def new(self, id, dbname, coname, client):
        handle = CollectionTxnHandle(dbname, coname, client)
        self.new_inner(id,handle,None)
        return self

    def new_with(self, id, collectionTxnInner):
        self.new_inner(id,None,collectionTxnInner)
        return

    def new_inner(self,id,CollectionTxnHandle,CollectionTxnInner):
        self.handle = CollectionTxnHandle
        self.parent = CollectionTxnInner
        expr = engula.v1.expr_pb2.from()
        expr.id = id
        self.expr =expr
        return self
