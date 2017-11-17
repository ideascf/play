# coding=utf-8
import logging
import contextlib
import threading
from Queue import LifoQueue, Empty, Full


log = logging.getLogger()


class ClientPoolError(Exception):
    pass


class BaseClient(object):
    pass


class ClientPool(object):

    def __init__(self, client_class, max_clients=100, *client_args, **client_kwargs):
        super(ClientPool, self).__init__()

        self.max_clients = max_clients

        self.client_class = client_class
        self.client_args = client_args
        self.client_kwargs = client_kwargs

        self.reset()

    def reset(self):
        self._index = 0  # record client's index
        self._created_clients = 0
        self._available_clients = []
        self._in_use_clients = set()
        self._check_lock = threading.Lock()

    def get_client(self):
        try:
            client = self._available_clients.pop()
        except IndexError:
            client = self.make_client()

        self._in_use_clients.add(client)
        log.info('Get client<index:%s, obj:%s>', client.__index, client)

        return client

    def make_client(self):
        """

        :return:
        :rtype: BaseClient
        """

        if self._created_clients >= self.max_clients:
            raise ClientPoolError('Too many connections')
        self._created_clients += 1

        client = self.client_class(*self.client_args, **self.client_kwargs)
        client.__index = self._gen_client_index()

        return client

    def release_client(self, client):
        """

        :param client:
        :type client: BaseClient
        :return:
        """

        log.info('Release client<index:%s, obj:%s>', client.__index, client)

        self._in_use_clients.remove(client)
        self._available_clients.append(client)

    def _gen_client_index(self):
        """
        生成client的index,用于标记client
        :return:
        :rtype: int
        """

        index = self._index
        self._index += 1

        return index


class BlockingClientPool(ClientPool):

    def __init__(self, client_class, max_clients=100, timeout=None, queue_class=LifoQueue,
                 *client_args, **client_kwargs):

        self.queue_class = queue_class
        self.timeout = timeout

        super(BlockingClientPool, self).__init__(
            client_class=client_class,
            max_clients=max_clients,
            *client_args,
            **client_kwargs
        )

    def reset(self):
        self.pool = self.queue_class(self.max_clients)
        try:
            while True:
                self.pool.put_nowait(None)
        except Full:
            pass

        self._clients = []
        self._index = 0  # record client's index

    def make_client(self):
        client = self.client_class(*self.client_args, **self.client_kwargs)
        client.__index = self._gen_client_index()
        self._clients.append(client)

        return client

    def get_client(self):
        try:
            client = self.pool.get(block=True, timeout=self.timeout)
        except Empty:
            raise ClientPoolError('No client available.')

        if client is None:
            client = self.make_client()
        log.info('Get client<index:%s, obj:%s>', client.__index, client)

        return client

    def release_client(self, client):
        log.info('Release client<index:%s, obj:%s>', client.__index, client)

        try:
            self.pool.put_nowait(client)
        except Full:
            pass


@contextlib.contextmanager
def get_client(pool):
    """

    :param pool:
    :type pool: ClientPool
    :return:
    :rtype: BaseClient
    """

    client = pool.get_client()
    try:
        yield client
    finally:
        pool.release_client(client)
