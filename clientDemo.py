import socket
import wmi
import threading

#获取本机进程列表
def getWinProList():
    ProList = []
    c = wmi.WMI()
    for process in c.Win32_Process():
        ProList.append(str(process.Name))
    return ProList
#获取本机服务列表
def getWinSerList():
    SerList = []
    c = wmi.WMI()
    for service in c.Win32_Service():
        SerList.append(str(service.Name))
    return SerList
#获取本机系统，CPU，内存信息
def getSystemInfo():
    c = wmi.WMI()
    systemInfo=''
    for sys in c.Win32_OperatingSystem():
        systemInfo+='Version:'+sys.Caption+' Vernum:'+sys.BuildNumber
        systemInfo+=' '+sys.OSArchitecture
    for processor in c.Win32_Processor():
        systemInfo+=" Process Name:"+processor.Name.strip()
        for Memory in c.Win32_PhysicalMemory():
            systemInfo+=" Memory Capacity:"+str(int(Memory.Capacity)/1024/1024/1024)+' GB'
    return systemInfo
#获取本机Mac,IP地址
def getIp():
    c = wmi.WMI()
    ipInfo=''
    for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled= True):
        ipInfo+="MAC:"+interface.MACAddress
        for ip_address in interface.IPAddress:
            ipInfo+=" ip:"+ip_address
    return ipInfo
#扫描本机
def scanSystem():
    resultInfo=''
    resultInfo+=getIp()+' '+getSystemInfo()
    systemCheck1=systemCheck2=systemCheck3='N'
    ProList=getWinProList()
    for pro in ProList:
        if pro == 'PccNTMon.exe':#XXX防毒软件的进程
            systemCheck1='Y'
    SerList=getWinSerList()
    for ser in SerList:
        if ser == 'TMBMServer':#XXX防毒软件的服务
            systemCheck2='Y'
        if ser == 'wuauserv':#windows update服务
            systemCheck3='Y'
    if systemCheck1 == 'Y':
        resultInfo+=' XXX软件进程已开启'
    else:
        resultInfo+=' XXX软件进程未开启'
    if systemCheck2 == 'Y':
        resultInfo+=' XXX服务已开启'
    else:
        resultInfo+=' XXX服务未开启'
    if systemCheck3 == 'Y':
        resultInfo+=' 系统已开启自动更新'
    else:
        resultInfo+=' 系统未开启自动更新'
    return resultInfo



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.getfqdn(socket.gethostname())
print("host_name")
print(socket.gethostname())
print(host_name)

remote_ip = socket.gethostbyname( host_name )
print(remote_ip)
s.connect((remote_ip, 9999))
print(s.recv(1024).decode('utf-8'))
s.send(bytes(scanSystem(),encoding='utf-8'))
s.close()