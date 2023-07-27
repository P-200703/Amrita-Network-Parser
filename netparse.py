import csv
import sys
import operator
import datetime
import re
import time
import sys
import itertools 
import colorama
from colorama import Fore,Back

H=0
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if H:
            break
        sys.stdout.write('\rAnalysing... ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rHere You Go ....!')

print('''          __  __ _____  _____ ______  _       _   _ ______   _______ _____        _____   _____ ______ _____  
    /\   |  \/  |  __ \|_   _|__   __|/\       | \ | |  ____|__   __  |  __ \ /\   |  __ \ / ____|  ____|  __ \ 
   /  \  | \  / | |__) | | |    | |  /  \      |  \| | |__     | |    | |__) /  \  | |__) | (___ | |__  | |__) |
  / /\ \ | |\/| |  _  /  | |    | | / /\ \     | . ` |  __|    | |    |  ___/ /\ \ |  _  / \___ \|  __| |  _  / 
 / ____ \| |  | | | \ \ _| |_   | |/ ____ \    | |\  | |____   | |    | |  / ____ \| | \ \ ____) | |____| | \ \ 
/_/    \_\_|  |_|_|  \_\_____|  |_/_/    \_\    _| \_|______|  |_|    |_| /_/    \_\_|  \_\_____/|______|_|  \_\
                                                                                                          ''')
MONTH_DICT = { '01': "Jan", '02': "Feb", '03': "Mar", '04': "Apr" , '05': "May",  '06': "Jun",  '07': "Jul", '08': "Aug" , '09': "Sep", '10': "Oct", '11': "Nov", '12': "Dec"}
if (len(sys.argv) < 2 or len(sys.argv) > 2):
		print("Error! - No Log File Specified!")
elif (len(sys.argv)==2):
	

    with open(sys.argv[1]) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        ipdict={}
        iplist=[]
        plist=[]
        flist=[]
        slist=[]
        conn=0
        print("Source File:",sys.argv[1])

        animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
        for i in range(10):
            time.sleep(0.9)
            sys.stdout.write(Fore.GREEN+"\rAnalysing.... " + animation[i % len(animation)])
            sys.stdout.flush()
        for row in reader:
            if(row[4] in ['21', '22', '23', '25']):
                if (row[1] not in iplist):
                    iplist.append(row[1])
                if (row[2] not in slist and row[1] in iplist):
                    slist.append(row[2])
                if(conn==0):
                    conn=row[0]
        for i in iplist:
            plist.append(i.split("."))
        #print('ip list is :',plist)
        plist.sort(key= lambda plist: int(plist[3]))
        #print('sorted list is :',plist)
        for i in plist:
            s="."
            s = s.join(i)
            flist.append(s)
        #print('final ip list is :',plist)
        #print("Systems Infected:",len(flist))
        #print("Infected System IPs:\n",flist, sep='')
        #print("C2 Servers:",len(slist))
        plist.clear()
        flist.clear()
        for i in slist:
            plist.append(i.split("."))
        plist.sort(key=operator.itemgetter(1,2,3))
        #print(plist)
        for i in plist:
            s="."
            s = s.join(i)
            flist.append(s)
        #print("C2 Server IPs:\n",flist, sep='')
        ans = datetime.datetime.utcfromtimestamp(float(conn)).strftime('%Y-%m-%d %H:%M:%S')
        #print(ans)	
        lis2 = re.split("[- ]", ans)
        #print(lis2)
        if (lis2[1] in MONTH_DICT):
            month = MONTH_DICT[lis2[1]]
        #print("First C2 Connection: ", lis2[0],"-",month,"-",lis2[2]," ", lis2[3]," UTC", sep='' )
        csv_file.seek(0)
        for row in reader:
            if(row[2] in flist and (row[2] not in ipdict.keys())):
                ipdict[row[2]] = int(row[5])
            elif(row[2] in flist and (row[2] in ipdict.keys())):
                ipdict[row[2]] +=int(row[5])
        fdict = sorted(ipdict.items(), key=operator.itemgetter(1),reverse=True)
        #print("C2 Data Totals:",fdict)
def clear():
    print("analysis completeeed")
    print("===========================================")
    print(" Select an option ")
    print(Fore.BLUE+'''1. Number of systems infected
2. IP addresses of infected devices 
3. Number of servers effected communicating with
4. IP Addresses of infected servers
5. Date and time of 1st connection with server
6. Number of bytes of data exchanged
7. Exit
        ''')
    print(Fore.RED+'Enter Your Choice:',end=" ")
    choice=int(input())
    if(choice==1):
        print(Fore.YELLOW+"number of devices infected:",len(flist))
        clear()
    elif(choice==2):
            print(Fore.YELLOW+"IPs of devices infected are:")
            for i in range(len(flist)):
                print(Fore.YELLOW+" Device", i+1, ":", flist[i])
            clear()
    elif(choice==3):
            print(Fore.YELLOW+"number of servers infected:",len(slist))
            clear()
    elif(choice==4):
            print(Fore.YELLOW+"IPs of servers infected are:")
            for i in range(len(slist)):
                print(Fore.YELLOW+" Server", i+1, ":", slist[i])
            clear()
    elif(choice==5):
            print(Fore.YELLOW+"First server Connection: ", lis2[0],"-",month,"-",lis2[2]," ", lis2[3]," UTC", sep='' )
            clear()

    elif(choice==6):
        print(Fore.YELLOW+"Server Data Totals:",fdict)
        clear()
    elif(choice==7):
        exit()

    else:
        print(Fore.YELLOW+"Please choose correct Option")
        clear()
             


clear()


	#except:
	#    print("Error! - File Not Found!")
		