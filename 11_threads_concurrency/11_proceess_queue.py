from multiprocessing import Process, Queue

def prepare_chai(queue):
    queue.put("Masala chai is ready")

queue = Queue()




if __name__ == "__main__":
    p = Process(target=prepare_chai, args=(queue, ))
    p.start()
    p.join()
    print(queue.get())