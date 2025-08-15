import asyncio
import time
from concurrent.futures import ThreadPoolExecutor
import random


def check_stock(item):
    print(f"Checking {item} in store...")
    time.sleep(3) # Blocking operation
    return f"{item} stock: {random.randint(0, 100)}"

async def  main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "Masala chai")
        print(result)
        
        
        
asyncio.run(main())