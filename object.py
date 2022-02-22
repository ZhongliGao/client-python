class ObjcetTxn:
    def __init__(self, CollectionTxn, MethodCallExpr):
        self.txn = CollectionTxn
        self.expr = MethodCallExpr

    def new(self,CollectionTxn, object_id):
        expr = expr_pb2.MethodExpr(object_id)
        return self.__init__(CollectionTxn,expr)