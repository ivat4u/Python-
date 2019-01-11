import thread
from time import sleep,ctime
loops=[4,2]

def loop(nloop,nsec,lock):
    print'start loop',nloop,'at:',ctime()
    sleep(nsec)
    print'loop',nloop,'done at:',ctime()
    lock.release()

def main():
    print'starting at',ctime()
    locks=[]
    nloops=range(len(loops))

    for i in nloops:
        lock=thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop,(i,loops[i],locks[i]))

    for i in nloops:
        while locks[i].locked():pass
        #会按顺序等待所有锁释放，往往是前面的线程导致主进程的阻塞

    print'all DONE at:',ctime()

if __name__ == '__main__':
    main()