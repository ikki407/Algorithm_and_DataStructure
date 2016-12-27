class DoublyLinkedList:
    def __init__(self):
        self.nil = self.make_node(None)
        self.nil['next'] = self.nil
        self.nil['prev'] = self.nil
    def make_node(self, k):
        return {'key':k, 'next':None,'prev':None}

    def insert(self, key):
        x = self.make_node(key)
        x['next'] = self.nil['next']
        self.nil['next']['prev'] = x
        self.nil['next'] = x
        x['prev'] = self.nil

    def listSearch(self,key):
        cur = self.nil['next']
        while cur['key'] != None and cur['key'] != key:
            cur = cur['next']
        return cur

    def delete(self, k):
        self.delete_node(self.listSearch(k))

    def delete_node(self,x):
        if x['key'] == None: return
        x['prev']['next'] = x['next']
        x['next']['prev'] = x['prev']

    def deleteFirst(self):
        self.delete_node(self.nil['next'])

    def deleteLast(self):
        self.delete_node(self.nil['prev'])

    def printList(self):
        x = self.nil['next']
        while True:
            if x['key'] == None:
                break
            else:
                print x['key'],
                x = x['next']
        print

def main():
    N = int(raw_input())
    commands = []
    for i in xrange(N):
        commands.append(raw_input())
    d = DoublyLinkedList()
    for c in commands:
        a = c[0]
        if a == 'i':
            d.insert(int(c[7:]))
        else:
            if c[6] == 'F':
                d.deleteFirst()
            elif c[6] == 'L':
                d.deleteLast()
            else:
                d.delete(int(c[7:]))

    d.printList()
    return 0

main()


