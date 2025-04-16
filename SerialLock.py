import threading


from shared import lock_singleton
class SerialLock():
    #探针位移的全局锁，为了保证同一时刻只有一个线程能进行探针信息的获取
    serial_lock = lock_singleton.serial_lock
