import time
import threading

def showmultithread(numbers) :
    i=0
    while i<numbers :
        time.sleep(1)
        i=i+1
    print(i)

t = time.time()
arr=int(input("Enter Any Number : "))
t1=threading.Thread(target=showmultithread, args=(arr,))
t1.start()
t1.join()

print("done in : ", time.time()-t)