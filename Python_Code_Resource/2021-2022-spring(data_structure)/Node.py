from hashlib import new
from mimetypes import init


class Node():
    def __init__(self, initdata):
        self.data = initdata
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
