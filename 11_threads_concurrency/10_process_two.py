from multiprocessing import Process
import time


def cpu_heavy():
    print(f"Crunching some numbers...")
    total = 0
    for i in range(10**7):
        total += i
    print("DONE")
    
    
if __name__ == "__main__":    
    start = time.time()
    processes = [Process(target=cpu_heavy) for _ in range(2)]
    [t.start() for t in processes]
    [t.join() for t in processes]
    end = time.time()

    print(f"Time Taken: {end - start:.2f} seconds")