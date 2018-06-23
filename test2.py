import wmi
myWmi= wmi.WMI()
# import win32com.client as client
# #Win32_POTSModemToSerialPort  Win32_SerialPortConfiguration  Win32_ParallelPort Win32_SerialPortSetting Win32_PortConnector Win32_PortResource  Win32_SerialPort
# # for cls in myWmi.classes:
# #     print(cls)
# # physicalMemos = myWmi.Win32_PhysicalMemory()
# # for temp in physicalMemos:
# #     print(temp.Capacity)#物理总内存
# # avaiable = myWmi.Win32_PerfFormattedData_PerfOS_Memory()
# # for temp in avaiable:
# #     print(temp.AvailableMBytes)#可用物理内存
# #
# #
# # virtualMem = myWmi. Win32_PageFileUsage()
# # for temp in virtualMem:
# #
# #     print(temp.AllocatedBaseSize)#可用虚拟内存 = 可用分页内存+可用物理内存
#
#
#
# # free_mem = myWmi.Win32_PageFileSetting()#如果为空需要设置虚拟环境  虚拟内存总量 = 物理内存+分页内存
# # # print(free_mem)
# # for temp in free_mem:
# #     print(temp)
#
processes = myWmi.Win32_Process()
print(len(processes))
for temp in processes:

    print(temp)
# #     # print(temp.VirtualSize)
# #
# pmem = myWmi.Win32_PerfFormattedData_PerfProc_Process()
# # com = client.Dispatch("WbemScripting.SWbemRefresher")
# # obj = client.GetObject("winmgmts:root\cimv2")
# # cpuitems = com.AddEnum(obj, "Win32_PerfFormattedData_PerfProc_Process").objectSet
# #
# # com.Refresh()
#
# # pmem = myWmi.Win32_PerfRawData_PerfProc_Process()
# for temp in pmem:
#     print(temp.Name,temp.PercentPrivilegedTime)
#
# # pmem = myWmi.Win32_PerfFormattedData_PerfOS_Memory()
# # for temp in pmem:
# #     print(temp.PoolNonpagedBytes)
#
# # service = myWmi.Win32_Service()
# # for temp in service:
# #     print(temp)
#
# # logs = myWmi.Win32_NTLogEvent()
# # print(logs)
# # for temp in logs:
# #     print(temp)


# import wmi
# from win32com.client import GetObject
# import win32gui, time
#
# mywmi = GetObject("winmgmts:")
# allProcess = mywmi.ExecQuery("select * from Win32_Process")
# for i in allProcess:
#     pid = i.Properties_("ProcessID")
#     print pid

# network = mywmi.ExecQuery("select Processor, _Total, Processor Time from PerformanceCounter")
# print network
# for i in network:
#     print i.Properties_("Processor")



