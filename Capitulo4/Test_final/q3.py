from fila import Queue
queue = Queue()
items = [10 * i for i in range(1, 11)]
for item in items:
    queue.enqueue(item)
    if (item // 10) % 2 == 0:
        queue.dequeue()
print(queue.queue)