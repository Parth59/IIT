from Tkinter import *
from tkFileDialog import *
import time
import subprocess
import os
import signal

def browse():
    file_path=askdirectory()
    os.chdir(file_path)
    global pro
    pro = subprocess.Popen("python -m SimpleHTTPServer 9999", shell=True,preexec_fn=os.setsid) 
    
def close():
    print pro
    os.killpg(os.getpgid(pro.pid), signal.SIGKILL)

def cancel():
    app.quit()    
    os.killpg(os.getpgid(pro.pid), signal.SIGKILL)
    
  
	
app=Tk()
app.title("HOST FILES")
app.geometry('550x300+200+100')
l=Label(app,text="Select the Folder which you want to share",height=3)
l.pack()
b1=Button(app,text="Browse...",width=10,command=browse)
b1.pack(padx=10,pady=10)
app.protocol('WM_DELETE_WINDOW', cancel)

b2=Button(app,text="Close Sharing",width=10,command=close)
b2.pack(padx=10,pady=10)


out = subprocess.check_output(""" ip addr | awk '
/^[0-9]+:/ { 
  sub(/:/,"",$2); iface=$2 } 
/^[[:space:]]*inet / { 
  split($2, a, "/")
  print iface" : "a[1] 
}' """,shell=True)
lines=out.split('\n')
disp_ip=""
for i in xrange(0,len(lines)-1):
    s=lines[i]+":9999"
    disp_ip=disp_ip+s+"\n"
l2=Label(app,text="Use the Following in Browser to Access your Folder:\n"+disp_ip,height=3)
l2.pack(side="bottom", fill="both", expand=True, padx=20, pady=25)   



app.mainloop()
