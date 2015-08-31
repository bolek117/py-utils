__author__ = "bolek117"


class socketwrapper:
    """
    :type response: str
    :type _buffer_size: int
    """

    def __init__(self, ip, port, buffer_size, timeout=10):
        self.response = ''
        self._buffer_size = buffer_size
        self.no_response = '[No response]'

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(timeout)
        self.s.connect((ip, port))

    def __del__(self):
        self.s.close()

    def req(self, content):
        c = '{}\n'.format(content)
        self.s.send(c)

    def recv(self):
        """

        :return: str
        """
        try:
            self.response = self.s.recv(self._buffer_size)
        except socket.timeout:
            self.response = self.no_response

        return self.response


