#coding: utf-8

from ctypes import Structure, windll, POINTER, c_ubyte, c_long, wintypes

GetSystemPowerStatus = windll.kernel32.GetSystemPowerStatus


# See: https://msdn.microsoft.com/zh-tw/library/windows/desktop/aa373232(v=vs.85).aspx
class SYSTEM_POWER_STATUS(Structure):
    _fields_ = [
        ('ACLineStatus', c_ubyte),
        # The value is zero if the battery is not being charged and the battery capacity is between low and high.
        ('BatteryFlag', c_ubyte),
        # The percentage of full battery charge remaining. This member can be a value in the range 0 to 100, or 255 if status is unknown.
        ('BatteryLifePercent', c_ubyte),
        ('SystemStatusFlag', c_ubyte),
        # The number of seconds of battery life remaining, or –1 if remaining seconds are unknown or if the device is connected to AC power.
        ('BatteryLifeTime', c_long),
        # The number of seconds of battery life when at full charge, or –1 if full battery lifetime is unknown or if the device is connected to AC power.
        ('BatteryFullLifeTime', c_long)
    ]

GetSystemPowerStatus.argtypes = [POINTER(SYSTEM_POWER_STATUS)]
GetSystemPowerStatus.restype = wintypes.BOOL

# The AC power status. This member can be one of the following values.
mapping_ACLineStatus = {
    0: 'Offline',
    1: 'Online',
    255: 'Unknown status'
}

# The battery charge status. This member can contain one or more of the following flags.
mapping_BatteryFlag = {
    1: 'High - the battery capacity is at more than 66 percent',
    2: 'Low - the battery capacity is at less than 33 percent',
    4: 'Critical - the battery capacity is at less than five percent',
    8: 'Charging',
    128: 'No system battery',
    255: 'Unknown status - unable to read the battery falg information'
}

mapping_SystemStatusFlag = {
    0: 'Battery saver is off',
    1: 'Battery saver on. Save energy where possible'
}

if __name__ == '__main__':
    power_status = SYSTEM_POWER_STATUS()
    GetSystemPowerStatus(power_status)
    print(power_status.ACLineStatus)
    print(power_status.BatteryFlag)
    print(power_status.BatteryLifePercent)
    print(power_status.SystemStatusFlag)
    print(power_status.BatteryLifeTime)
    print(power_status.BatteryFullLifeTime)