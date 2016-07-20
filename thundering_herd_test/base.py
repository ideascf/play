# coding=utf-8
import socket
import multiprocessing

def create_listener():
    """

    :return:
    :rtype: socket.socket
    """

    listener = socket.socket()
    listener.bind(('', 59999))
    listener.listen(10)

    return listener



def bootstrap(worker, before_fork_callback=None):
    process_num = 10
    listener = create_listener()
    if before_fork_callback is not None:
        listener = before_fork_callback(listener)

    process_list = [
        multiprocessing.Process(target=worker, args=(listener,))
        for _ in range(process_num)
    ]

    map(
        lambda process: process.start(),
        process_list
    )

    map(
        lambda process: process.join(),
        process_list
    )

    listener.close()

