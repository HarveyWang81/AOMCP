# coding:utf-8

import paramiko


class RomoteSSH(object):
    def __init__(self, host_ip, user_code, password, host_port=22):
        self.host_ip = host_ip
        self.host_port = host_port
        self.user_code = user_code
        self.password = password

    def operationSSH(self, command):
        self.command = command
        transport = paramiko.Transport((self.host_ip, self.host_port))
        transport.connect(username=self.user_code, password=self.password)

        myssh = paramiko.SSHClient()
        myssh._transport = transport


        stdin, stdout, stderr = myssh.exec_command(self.command)
        result = stdout.readlines()
        transport.close()
        return result

if __name__ == '__main__':
    a = RomoteSSH