import threading
import time
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

# time1=time.perf_counter()
# func(10)
# func(8)
# func(5)

# time2=time.perf_counter()
# print(time2-time1)


# time1=time.perf_counter()

# t1=threading.Thread(target=func,args=(10,))
# t2=threading.Thread(target=func,args=(8,))
# t3=threading.Thread(target=func,args=(5,))

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()
# time2=time.perf_counter()
# print(time2-time1)



# import time
# from concurrent.futures import ThreadPoolExecutor

# def func(seconds):
#     print(f"Sleeping for {seconds} seconds")
#     time.sleep(seconds)

# def poolingDemo():
#     with ThreadPoolExecutor() as executor:
#         future1 = executor.submit(func, 10)
#         future2 = executor.submit(func, 8)
#         future3 = executor.submit(func, 5)

#         future1.result()
#         future2.result()
#         future3.result()

# time1 = time.perf_counter()

# poolingDemo()
# time2 = time.perf_counter()
# print(time2 - time1)


# import time
# from concurrent.futures import ThreadPoolExecutor

# def func(seconds):
#     print(f"Sleeping for {seconds} seconds")
#     time.sleep(seconds)

# def poolingDemoMap():
#     list_timer = [10, 8, 5]
#     with ThreadPoolExecutor() as executor:
#         results = executor.map(func, list_timer)
#         for r in results:
#             print(r)

# time1 = time.perf_counter()
# poolingDemoMap()
# time2 = time.perf_counter()
# print(time2 - time1)

# import time
# import math

# start = time.perf_counter()
# results1 = [math.factorial(x) for x in range(25)]
# end = time.perf_counter()

# print(end - start)




import time
import math
from multiprocessing import Pool

if __name__ == '__main__':
    start = time.perf_counter()
    with Pool(4) as p:
        results2 = p.map(math.factorial, range(25000))
    end = time.perf_counter()

    print(end - start)
     





