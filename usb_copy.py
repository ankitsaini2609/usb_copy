#!/usr/bin/python
import getpass,os,re,sys,shutil,subprocess
from time import sleep

def search(path,current_path):
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            #this logic is used to check name of directory starting from which name and it is case insenstive
            a = re.match(r'w[a-z A-Z]*ng',fname,re.I)
            b = re.match(r'r[a-z A-Z]*ng',fname,re.I)
            c = re.match(r'c[a-z A-Z]*ct',fname,re.I)
            p = str(type(a))
            q = str(type(b))
            r = str(type(c))
            d = None
            #print(p+" "+q+" "+r)
            if (p.find('None') == -1):
                d = a
            elif (q.find('None') == -1):
                d = b
            elif (r.find('None') == -1):
                d = c
            #print(str(type(d)).find('None'))
            if (str(type(d)).find('None') == -1):
                if (fname == d.group()):
                    files = os.listdir(path+"/"+fname)
                    user = getpass.getuser()
                    if (len(files) != 0):
                        shutil.copy2(path+"/"+fname+"/"+files[0],current_path+"/filename.c")
                    sys.exit()
            else :
                #print(path+"/"+fname)
                search(path+"/"+fname,current_path)


current_path = os.getcwd()
user = getpass.getuser()
path = '/media/'+user
while True:
    try:
        s = subprocess.check_output(["/bin/bash","-c","lsblk -o MOUNTPOINT,NAME |grep -i /media|grep -v sda"]) #this command will check pd is inserted or not.
    except:
        s = "None"
    if (len(s) != 4):
        #this block of code will truncate accurate path of pendrive and directly search into this. 
        #p = str(s)
        #f1 = p.find(' sd')
        #f2 = p.find('/')
        #path = p[f2:f1].strip(' ')
        #print(path)
        search(path,current_path)
    else:
        sleep(10)


