# coding: utf-8
import csv
import traceback
import socket
import paramiko
import logging
from paramiko.ssh_exception import AuthenticationException

log = logging.getLogger()
remote_path = '/download/smartpay/settlements/'

class SFTPConnError(Exception):
    pass


class SFTPMaxRetryError(SFTPConnError):
    pass


class SFTPConn(object):

    def __init__(self, host, port, username, password):
        super(SFTPConn, self).__init__()
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.server = None
        self._login_to_sftp_server()

    def _login_to_sftp_server(self, max_retry=3):
        for current_retry in range(max_retry):
            try:
                self.transport = paramiko.Transport((self.host, self.port))
                self.transport.connect(username=self.username, password=self.password)
                server = paramiko.SFTPClient.from_transport(self.transport)
                self.server = server
                break
            except AuthenticationException as e:
                log.warn('Connect sftp server auth fail try(%s)' % current_retry)
            except socket.error as e:
                log.warn('Connect sftp server fail(%s)', e)
        else:
            log.warn('Login into SFTP server fail')
            raise SFTPMaxRetryError('Exceed max retry')

    def do(self, filename, max_retry=3, delimiter='|'):
        for current_retry in range(max_retry):
            try:
                log.debug('try to get filename: %s', filename)
                reader = self._get_file(filename=filename, delimiter=delimiter)
                if reader is None:
                    log.info('settlement file(%s) NOT exist, IGNORE.', filename)
                else:
                    log.info('get file: %s SUCCESS', filename)
                break
            except (IOError, EOFError) as e:
                log.info('try to get filename: %s, fail(%s), now retry(%d)',
                         filename, e, current_retry)
                self.relogin()
            except Exception as e:
                log.warn('try to get filename: %s, fail(%s), now retry(%d)',
                         filename, e, current_retry)
                log.warn(traceback.format_exc())
                self.relogin()
        else:
            log.warn('get filename fail: %s', filename)
            raise SFTPMaxRetryError('Exceed max retry get file')
        return reader

    def relogin(self):
        self._login_to_sftp_server()

    def _get_file(self, filename, delimiter):
        self.server.chdir(remote_path)
        try:
            csvfile = self.server.open(filename)
        except IOError as e:
            if e.errno == 2:
                return None
            else:
                raise
        log.debug('get_file delimiter:%s', delimiter)
        reader = csv.DictReader(csvfile, delimiter=str(delimiter))
        return reader

    def __del__(self):
        if self.server:
            self.server.close()
            self.transport.close()
