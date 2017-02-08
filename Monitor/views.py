#coding:utf-8

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from models import *
from AOMCP.views import login_valid

@login_valid
def index(request):
    return render(request, 'monitor/index.html', locals())

@login_valid
def hostlist(request):
    table_list = HostInfo.objects.all()
    return  render(request, 'monitor/hostlist.html', locals())

@csrf_exempt
def savedata(request):
    result = {}
    if request.method == "POST" and request.POST:
        req_data = request.POST
        monitor_type = req_data.get('monitor_type')
        if monitor_type == 'static': # 处理服务器基础信息
            # 如果数据库中没有对应的 UID ，则新增一条记录；若已经存在对应的 UID，则对原记录进行更新
            if HostInfo.objects.filter(host_uid=req_data.get('host_uid')).count() == 0:
                host_info = HostInfo()
            else:
                host_info = HostInfo.objects.get(host_uid=req_data.get('host_uid'))

            host_info.host_uid = req_data.get('host_uid')
            host_info.host_ip = req_data.get('host_ip')
            host_info.host_mac = req_data.get('host_mac')
            host_info.host_name = req_data.get('host_name')
            host_info.os = req_data.get('os')
            host_info.memory_total = req_data.get('memory_total')
            host_info.disk_total = req_data.get('disk_total')
            host_info.save()
        elif monitor_type == 'cpu':
            cpu_info = CPUInfo()

            cpu_info.host_uid = req_data.get('host_uid')
            cpu_info.insert_datetime = req_data.get('insert_datetime')
            cpu_info.cpu_count = req_data.get('cpu_count')
            cpu_info.cpu_per_user = req_data.get('cpu_per_user')
            cpu_info.cpu_per_system = req_data.get('cpu_per_system')
            cpu_info.cpu_per_idle = req_data.get('cpu_per_idle')
            cpu_info.cpu_percent = 100.0 - float(cpu_info.cpu_per_idle)
            cpu_info.save()

        elif monitor_type == 'memory':
            memory_info = MemoryInfo()

            memory_info.host_uid = req_data.get('host_uid')
            memory_info.insert_datetime = req_data.get('insert_datetime')
            memory_info.memory_total = req_data.get('memory_total')
            memory_info.memory_available = req_data.get('memory_available')
            memory_info.memory_percent = req_data.get('memory_percent')
            memory_info.memory_used = req_data.get('memory_used')
            memory_info.memory_free = req_data.get('memory_free')
            memory_info.swap_total = req_data.get('swap_total')
            memory_info.swap_used = req_data.get('swap_used')
            memory_info.swap_free = req_data.get('swap_free')
            memory_info.swap_percent = req_data.get('swap_percent')
            memory_info.save()

        elif monitor_type == 'network':
            pass
        elif monitor_type == 'disk':
            pass
        else:
            result["statue"] = "error"
            return JsonResponse(result)
        result["statue"] = "success"
    else:
        result["statue"] = "error"
    return JsonResponse(result)

@login_valid
def details(request, host_uid):
    # 提取主机静态信息
    host_info = HostInfo.objects.get(host_uid=host_uid)

    # 提取主机动态信息
    # 提取 CPU 动态信息
    cpu_percent_view = []
    cpu_info = CPUInfo.objects.filter(host_uid=host_uid).order_by('insert_datetime')[0:40]

    for num, info in enumerate(cpu_info):
        cpu_percent_view.append([num + 1, float(info.cpu_percent)])

    # 提取 内存 动态信息
    memory_percent_view = []
    swap_percent_view = []
    memory_info = MemoryInfo.objects.filter(host_uid=host_uid).order_by('insert_datetime')[0:40]

    for num, info in enumerate(memory_info):
        memory_percent_view.append([num + 1, float(info.memory_percent)])
        swap_percent_view.append([num + 1, float(info.swap_percent)])


    return render(request, 'monitor/details.html', locals())