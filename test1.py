# import wmi
# import win32com
# c = wmi.WMI (moniker="winmgmts:{impersonationLevel=Delegate}//192.168.1.2")
# # loc = win32com.client.Dispatch("WbemScripting.SWbemLocator")
# # svc = loc.ConnectServer('192.168.0.68')
# # c = wmi.WMI(wmi=svc)
# # c=wmi.WMI()
# # 遍历进程
# for process in c.Win32_Process():
#     print(process.ProcessId, process.Name)
# # 遍历服务
# for service in c.Win32_Service():
#     print(service.ProcessId, service.Name)

import wmi





def sys_version(ipaddress, user, password):
    # loc = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    # svc = loc.ConnectServer(ipaddress)
    # conn = wmi.WMI(wmi=svc)
    # connection = wmi.connect_server(
    #     server=ipaddress,
    #     user=user,
    #     password=password
    # )
    conn = wmi.WMI()
    # conn = wmi.WMI()
    # conn = wmi.WMI(computer=ipaddress, user=user, password=password)
    # conn = wmi.WMI(computer="192.168.1.2", privileges=["!RemoteShutdown", "Security"])
    # zcpkj = dict()
    # for disk in conn.Win32_LogicalDisk(DriveType=3):
    #     zcpkj[disk.Caption] = round((100.0 * int(disk.FreeSpace) / int(disk.Size)),2)
    #
    # print( zcpkj)
    ProList = []
    ProListStatus = []
    key_process_name = {"chrome.exe":"N","cmd.exe":"N","qqq.exe":"N"}
    for key_process in key_process_name.keys():
        for process in conn.Win32_Process():
            if key_process == str(process.Name):
                key_process_name[key_process] ="Y"

    for k,v in key_process_name.items():
        if(v=="Y"):
            ProListStatus.append("正常")
        else:
            ProListStatus.append("失败")
        ProList.append(k)
    print(ProList)
    print(ProListStatus)




if __name__ == '__main__':
    # sys_version(ipaddress="192.168.1.7", user="administrator", password="123456")
    sys_version(ipaddress="192.168.0.45", user="Eric", password="eric")

# import wmi
# c = wmi.WMI ()
#
# for share in c.Win32_Share ():
#   print (share.Name, share.Path)