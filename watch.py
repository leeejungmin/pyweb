from tkinter import *
from time import strftime

def set_time():
    time_var.set(strftime('%H:%M:%S'))
    root.after(1000, set_time)


if __name__=='__main__':
    root = Tk()
    time_var = StringVar()
    Label(root, bd=30, textvariable=time_var).pack()
    set_time()
    root.mainloop()

import time
while True:
    from datetime import datetime
    now = datetime.now()
    print ("%s/%s/%s %s:%s:%s" % (now.month,now.day,now.year,now.hour,now.minute,now.second))
    time.sleep(1)
