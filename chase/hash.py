class ECHashTable:
    def __init__(self, size = 2003):
        self.data = list()
        self.size = size
        for i in range(size):
            self.data.append(list())
    def put(self,key,value=None):
        hashLocation = hash(key) % self.size
        for i in range(len(self.data[hashLocation])):
            kvpair = self.data[hashLocation][i]
            if kvpair[0] == key:
                self.data[hashLocation][i] = (key,value)
                return
        self.data[hashLocation].append((key,value))
    def has(self,key):
        hashLocation = hash(key) % self.size
        for kvpair in self.data[hashLocation]:
            if kvpair[0] == key: return True
        return False
    def get(self,key):
        hashLocation = hash(key) % self.size
        for kvpair in self.data[hashLocation]:
            if kvpair[0] == key: return kvpair[1]
        raise KeyError("Key not found.")
    def keys(self):
        rv = list()
        for i in range(self.size):
            for j in range(len(self.data[i])):
                rv.append(self.data[i][j][0])
        return rv

def main():
    inFile=open("key.txt", "r")
    encrypt=ECHashTable()
    with open("key.txt") as f:
        for line in f:
            (key, val) = line.split()
            encrypt.put(key, val)

    print("DONE!")


main()
