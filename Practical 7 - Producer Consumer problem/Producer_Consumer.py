import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def consumer(semaphore):
    with semaphore:
        logging.debug('Consumer waiting ...\n')
        semaphore.wait()
        logging.debug('Consumer consumed the resource\n')

def producer(semaphore):
    logging.debug('Producing resources...\n')
    with semaphore:
        logging.debug('Making resource available\n')
        logging.debug('Notifying all consumers\n')
        semaphore.notifyAll()

if __name__ == '__main__':
    condition = threading.Condition() # works as semaphore
    prod = threading.Thread(name='producer', target=producer, args=(condition,))
    con1 = threading.Thread(name='consumer1', target=consumer, args=(condition,))
    con2 = threading.Thread(name='consumer2', target=consumer, args=(condition,))

    con1.start()
    time.sleep(2)
    con2.start()
    time.sleep(2)
    prod.start()
