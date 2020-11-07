

import psutil
from win10toast import ToastNotifier
import time

def convert(sec):
    hrs = int(time.strftime("%H", time.gmtime(sec)))
    mins = int(time.strftime("%M", time.gmtime(sec)))

    if hrs == 0 and mins == 0 :
        return str(sec)+"seconds"
    elif hrs == 0 :
        return str(mins)+"minutes"
    elif hrs == 1 :
        return str(hrs)+"hour"
    else:
        return str(hrs)+"hours"
    

battery = psutil.sensors_battery()

power_percent = battery.percent
power_on = battery.power_plugged
power_left = convert(battery.secsleft)

if power_on == False and power_percent <= 30:
    toast = ToastNotifier()
    toast.show_toast(
        "Battery LOW !!!",
        "Power is at "+str(power_percent)+"\
        % only\n"+str(power_left)+"\
        left till shutdown\nPlease put on charge",
        icon_path = "icon.ico",
        duration = 10
    )



