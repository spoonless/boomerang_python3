from concurrent.futures import ThreadPoolExecutor


def task(n):
    print(f"debut {n}")
    for a in range(10000000):
        pass
    print(f"fin {n}")


with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(task, range(100))
