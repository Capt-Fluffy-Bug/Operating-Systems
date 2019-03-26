import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def consumer(cv):
    with cv:
        logging.debug('Consumer waiting ...\n')
        cv.wait()
        logging.debug('Consumer consumed the resource\n')

def producer(cv):
    logging.debug('Producing resources...\n')
    with cv:
        logging.debug('Making resource available\n')
        logging.debug('Notifying all consumers\n')
        cv.notifyAll()

if __name__ == '__main__':
    condition = threading.Condition()
    pd = threading.Thread(name='producer', target=producer, args=(condition,))
    cs1 = threading.Thread(name='consumer1', target=consumer, args=(condition,))
    cs2 = threading.Thread(name='consumer2', target=consumer, args=(condition,))

    cs1.start()
    time.sleep(2)
    cs2.start()
    time.sleep(2)
    pd.start()