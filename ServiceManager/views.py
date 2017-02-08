from django.shortcuts import render
from Monitor.models import *
from tools import *
from AOMCP.views import login_valid

@login_valid
def server_shell(request):
    host_info = HostInfo.objects.filter(os=u'Linux')
    if request.method == 'POST' and request.POST:
        host_ip = request.POST.get('host_ip')
        host_port = request.POST.get('host_port')
        user_code = request.POST.get('user_code')
        password = request.POST.get('password')
        command = request.POST.get('command')

        c = RomoteSSH(host_ip, user_code, password, int(host_port))
        result = [line.replace(' ', '&ensp;') for line in c.operationSSH(command)]
        return render(request, 'ServiceManager/server_shell.html', {'result': result, 'host_info': host_info})
    return render(request, 'ServiceManager/server_shell.html', {'host_info': host_info})
