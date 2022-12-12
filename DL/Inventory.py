class Inventory:
  
    def __init__(self):
        self.size = 13
        self.hashTable = self.createHashTable()
  
    def createHashTable(self):
        return [[] for _ in range(self.size)]
    def update(self,key,value):
        keyFound = False
        hashedKey = hash(key) % self.size
        bucket = self.hashTable[hashedKey]
        for index, record in enumerate(bucket):
            recordKey, recordValue = record
            if recordKey == key and recordValue==value:
                keyFound = True
                break
  
        if keyFound:
            bucket[index] = (key,value)
        else:
            bucket.append((key,value))
    @staticmethod
    def getItem(self, key,value):
        
        hashed_key = hash(key) % self.size
          
        bucket = self.hashTable[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            if record_key == key and record_val==value:
                found_key = True
                break
  
        if found_key:
            return record_val
        else:
            return None
    @staticmethod
    def deleteItem(self, key, value):
        
        hashed_key = hash(key) % self.size
          
        bucket = self.hash_table[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            if record_key == key and record_val==value:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return

