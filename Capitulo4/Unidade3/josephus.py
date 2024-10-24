from fila import Queue
def josephus(n, k):
    sequence = []
    queue = Queue()
    for i in range(1, n + 1):
        queue.enqueue(i)
    cont = 1
    while queue.size() > 1:
        if cont == k:
            sequence.append(queue.dequeue())
            cont = 1
        else:
            queue.enqueue(queue.dequeue())
            cont += 1
    return sequence, queue.dequeue()

n = int(input("Number of people on the table(N): "))
k = int(input("Number to be skipped(K): "))
seq, last = josephus(n, k)
print(f"Sequence = {seq}\nLast alive = {last}")
