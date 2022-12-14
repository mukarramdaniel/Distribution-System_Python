
class my_Queue:
    def __init__(self):
        self.length = 0
        self.tail= 0
        self.head= 0

class Order_Stock_DL:
    self.queue = my_Queue()
    def enqueue (x) :
        queue.tail = x
        if (queue.tail == queue.length) :
            queue.tail = 1
        else:
            queue.tail = queue.tail+1
    def dequeue():
        x = queue.head
        if (queue.head == queue.length):
           queue.head = 1
        else: 
            queue.head = queue.head + 1
        return x


    