import tkinter as tk
from JRPC import getInformation
import requests
from tkinter import messagebox
from datetime import datetime
import threading


import sched
import time

click_count = 0
def on_button_click():
    global click_count
    click_count += 1


def schedule_request_wrapper():
    a=click_count
    on_button_click()
    if(click_count>a):
        t = threading.Thread(target=schedule_request)
        t.start()
def my_close():
    res = messagebox.askokcancel('Information', 'Close？')
    if res == True:
        myWindow.destroy()

def schedule_request():

    if not year.get() and not month.get() and not day.get() and not hour.get() and not minute.get() and not second.get():
        delay = 0
        myWindow.after(int(delay * 1000), send_request)
    else:
        current_datetime = datetime.now()
        date_time = datetime(int(year.get()), int(month.get()), int(day.get()), int(hour.get()), int(minute.get()),
                             int(second.get()))
        delay = (date_time - current_datetime).total_seconds()
        if delay < 0:
            messagebox.showerror("Error", "Please give a correct future time.")
            response_entry.config(state='normal')
            response_entry.delete("1.0", tk.END)
            response_entry.insert(tk.END, f"Error for planning  ")
            response_entry.config(state='disabled')
        else:
            schedule.config(state='normal')
            selectedtext=r1.cget("text")
            schedule.insert(tk.END, f"On {current_datetime}: planning of {date_time} for {selectedtext}")
            schedule.config(state='disabled')
            myWindow.after(int(delay * 1000), send_request)








def update_info():

    if v.get()==0:
        CID = '_sum'
        CHID = 'State'
    elif v.get()==1:
        CID = '_sum'
        CHID = 'ProductionActiveEnergy'

    elif v.get()==2 :
        CHID = 'ConsumptionActiveEnergy'
        CID = '_sum'
    elif v.get()==10 <=v.get()<=15:
        CID = 'ess0'
        CHID = 'Soc'
    elif v.get() == 11:
        CID = 'ess0'
        CHID = 'ActivePower'
    elif v.get()==12:
        CID = 'ess0'
        CHID = 'ActiveChargeEnergy'
    elif v.get() == 13:
        CID = 'ess0'
        CHID = 'ActiveDischargeEnergy'
    elif v.get() == 14:
        CID = 'ess0'
        CHID = 'MaxApparentPower'
    elif v.get() == 15:
        CID = 'ess0'
        CHID = 'Capacity'

    elif v.get()==20:
        CID = 'meter0'
        CHID = 'ActivePower'

    elif v.get()==21:
            CID = 'meter1'
            CHID = 'ActivePower'
    elif v.get() == 30:
        CID = 'ess0'
        CHID = 'SetActivePowerEquals'
      # Default as the choice
    else:
        CID= '_sum'
        CHID = 'State'

    if 31<=v.get()<=34:
        link="http://localhost:8084/jsonrpc"
        l4.config(text='127.0.0.1')
        l6.config(text='8084')
        l8.config(text='')
        l10.config(text='')
        l12.config(text=link)
    else:
        info = getInformation(ComponentID=CID, ChannelID=CHID)
        l4.config(text=info.IP)
        l6.config(text=info.Port)
        l8.config(text=info.componentid)
        l10.config(text=info.channelID)
        l12.config(text=info.link)

def send_request():

    if v.get() ==0:
        url = l12.cget("text")
        user = 'x'
        password = 'admin'
        session = requests.Session()
        session.auth = (user, password)
        response = session.get(url)
        if response.status_code == 200:
            json_data = response.json()
            response_entry.config(state='normal')
            response_entry.delete("1.0", tk.END)
            response_entry.insert(tk.END, l10.cget("text")+f": {json_data}")
            response_entry.config(state='disabled')


        else:
            response_entry.config(state='normal')
            response_entry.delete("1.0", tk.END)
            response_entry.insert(tk.END, f"Error:{response.status_code}")
            response_entry.config(state='disabled')



    elif 1<=v.get()<=2:
        url = l12.cget("text")
        user = 'x'
        password = 'admin'
        session = requests.Session()
        session.auth = (user, password)
        response = session.get(url)
        if response.status_code == 200:
                json_data = response.json()
                response_entry.config(state='normal')
                response_entry.delete("1.0", tk.END)
                response_entry.insert(tk.END,l10.cget("text")+f": {json_data['value']}{json_data['unit']}")
                response_entry.config(state='disabled')

        else:
                json_data = response.json()
                response_entry.config(state='normal')
                response_entry.delete("1.0", tk.END)
                response_entry.insert(tk.END, f"Error:{json_data}")
                response_entry.config(state='disabled')
    elif 10 <= v.get() <= 15:
        url = l12.cget("text")
        user = 'x'
        password = 'admin'
        session = requests.Session()
        session.auth = (user, password)
        response = session.get(url)
        if response.status_code == 200:
            json_data = response.json()
            response_entry.config(state='normal')
            response_entry.delete("1.0", tk.END)
            response_entry.insert(tk.END, l10.cget("text")+f": {json_data['value']}{json_data['unit']}")
            response_entry.config(state='disabled')
        else:
            response_entry.config(state='normal')
            response_entry.delete("1.0", tk.END)
            response_entry.insert(tk.END, f"Error:{response.status_code}")
            response_entry.config(state='disabled')

    elif 20 <= v.get() <= 21:
        url = l12.cget("text")
        user = 'x'
        password = 'admin'
        session = requests.Session()
        session.auth = (user, password)
        response = session.get(url)
        if response.status_code == 200:
            json_data = response.json()
            response_entry.config(state='normal')
            response_entry.delete("1.0", tk.END)
            response_entry.insert(tk.END, l10.cget("text")+f": {json_data['value']}{json_data['unit']}")
            response_entry.config(state='disabled')
        else:
            response_entry.config(state='normal')
            response_entry.delete("1.0", tk.END)
            response_entry.insert(tk.END, f"Error:{response.status_code}")
            response_entry.config(state='disabled')


    elif v.get()==30:
        url = l12.cget("text")
        user = 'x'
        password = 'admin'
        session = requests.Session()
        session.auth = (user, password)
        entry_text = entry.get()

        if not entry_text:
            messagebox.showerror("Error", "Value cannot be empty!")


        else:
            if -10000.0 <= float(entry_text) <= 10000.0:
                data = {"value": entry.get()}
                response = session.post(url, json=data)
                if response.status_code == 200:
                    response_entry.config(state='normal')
                    response_entry.delete("1.0", tk.END)
                    response_entry.insert(tk.END, f"OK:{response.status_code}")
                    response_entry.config(state='disabled')

                else:
                    response_entry.config(state='normal')
                    response_entry.delete("1.0", tk.END)
                    response_entry.insert(tk.END, f"Error:{response.status_code}")
                    response_entry.config(state='disabled')

            else :
                messagebox.showerror("Error", "Value cannot more than 10000 !")
    elif v.get()==31:
        url = l12.cget("text")
        user = 'x'
        password = 'admin'
        session = requests.Session()
        session.auth = (user, password)
        entry_text = entry.get()

        if not entry_text:
            messagebox.showerror("Error", "Value cannot be empty!")
        else:

            data = {"method": "updateComponentConfig",
                    "params": {
                        "componentId": "ctrlPeakShaving0",
                        "properties":
                            [
                                {
                                    "name": "rechargePower",
                                    "value": entry_text
                                }
                            ]
                    }
                    }
            response = session.post(url, json=data)
            if response.status_code == 200:
                response_entry.config(state='normal')
                response_entry.delete("1.0", tk.END)
                response_entry.insert(tk.END, f"OK:{response.status_code}")
                response_entry.config(state='disabled')
            else:
                response_entry.config(state='normal')
                response_entry.delete("1.0", tk.END)
                response_entry.insert(tk.END, f"Error:{response.status_code}")
                response_entry.config(state='disabled')


    elif v.get()==32:
        url = l12.cget("text")
        user = 'x'
        password = 'admin'
        session = requests.Session()
        session.auth = (user, password)
        entry_text = entry.get()

        if not entry_text:
            messagebox.showerror("Error", "Value cannot be empty!")
        else:

            data = {"method": "updateComponentConfig",
	                "params": {
		                        "componentId": "ctrlPeakShaving0",
		                        "properties":
                                            [
                                                {
 			                                    "name": "peakShavingPower",
			                                    "value":  entry_text
		                                        }
                                            ]
	                            }
                    }
            response = session.post(url, json=data)
            if response.status_code == 200:
                response_entry.config(state='normal')
                response_entry.delete("1.0", tk.END)
                response_entry.insert(tk.END, f"OK:{response.status_code}")
                response_entry.config(state='disabled')
            else:
                response_entry.config(state='normal')
                response_entry.delete("1.0", tk.END)
                response_entry.insert(tk.END, f"Error:{response.status_code}")
                response_entry.config(state='disabled')
    elif v.get() == 33:
        url = l12.cget("text")
        user = 'x'
        password = 'admin'
        session = requests.Session()
        session.auth = (user, password)
        data = {"method": "updateComponentConfig",
                "params": {
                    "componentId": "ess0",
                    "properties":
                        [
                            {
                                "name": "enabled",
                                "value": "false"
                            }
                        ]
                }
                }
        response = session.post(url, json=data)
        if response.status_code == 200:
            response_entry.config(state='normal')
            response_entry.delete("1.0", tk.END)
            response_entry.insert(tk.END, f"OK:{response.status_code}")
            response_entry.config(state='disabled')
        else:
            response_entry.config(state='normal')
            response_entry.delete("1.0", tk.END)
            response_entry.insert(tk.END, f"Error:{response.status_code}")
            response_entry.config(state='disabled')

    elif v.get() == 34:
        url = l12.cget("text")
        user = 'x'
        password = 'admin'
        session = requests.Session()
        session.auth = (user, password)
        data = {"method": "updateComponentConfig",
                "params": {
                    "componentId": "ess0",
                    "properties":
                        [
                            {
                                "name": "enabled",
                                "value": "true"
                            }
                        ]
                }
                }
        response = session.post(url, json=data)
        if response.status_code == 200:
            response_entry.config(state='normal')
            response_entry.delete("1.0", tk.END)
            response_entry.insert(tk.END, f"OK:{response.status_code}")
            response_entry.config(state='disabled')
        else:
            response_entry.config(state='normal')
            response_entry.delete("1.0", tk.END)
            response_entry.insert(tk.END, f"Error:{response.status_code}")
            response_entry.config(state='disabled')




#Dictionary
LANGS = [ ("Status of Edge System", 0),
          ("Total Production Energy of generator", 1),
          ("Total Energy of consumer", 2),
    ("Status of Energy Storage System", 10),
    ("Active Power of Energy Storage System", 11),
    ("Active Charge Energy of Energy Storage System", 12),
    ("Active Discharge Energy of Energy Storage System", 13),
    ("Max Apparent Power of Energy Storage System", 14),
    ("Capacity of Energy Storage System", 15),
    ("Active power at the grid connection point ",20),
    ("Active Power of photovoltaic arrays Grid Meter Grid Meter ",21),



    ("Setting  Active power specification of Energy Storage System ", 30),
    ("Setting  Recharge power of Energy Storage System  ", 31),
    ("Setting  Peak-Shaving power ", 32),
    ("Setting  turn off the Energy Storage System ", 33),
    ("Setting  turn on the Energy Storage System ", 34)
]





myWindow = tk.Tk()
myWindow.title('iController')
width = 960
height =800
screenwidth = myWindow.winfo_screenwidth()
screenheight = myWindow.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
myWindow.geometry(alignstr)

response_frame=tk.Frame(myWindow)
calander_frame= tk.Frame(myWindow)
input_display_frame=tk.Frame(myWindow)
frame=tk.Frame(myWindow)

input_display_frame.grid(row=0,column=0,sticky='nw')
frame.grid(row=1,column=0,sticky='nw')
response_frame.grid(row=1,column=1,sticky='nw')
calander_frame.grid(row=2,column=0,sticky='nw')



v = tk.IntVar()
v.set(0)
for idx, (lang, val) in enumerate(LANGS):
    r1 = tk.Radiobutton(frame, text=lang, variable=v, value=val, command=update_info)
    r1.grid(row=idx+6, column=1, sticky='w')


#The input data display


l1 = tk.Label(input_display_frame, text="user:")
l2 = tk.Label(input_display_frame, text="Gast")
l3 = tk.Label(input_display_frame, text="IP:")
l4 = tk.Label(input_display_frame, text="")
l5 = tk.Label(input_display_frame, text="Port:")
l6 = tk.Label(input_display_frame, text="")
l7 = tk.Label(input_display_frame, text='Component ID:')
l8 = tk.Label(input_display_frame, text="")
l9 = tk.Label(input_display_frame, text='Channel ID:')
l10 = tk.Label(input_display_frame, text="")
l11 = tk.Label(input_display_frame, text="URL:")
l12 = tk.Label(input_display_frame, text="")
entryLabel=tk.Label(response_frame, text="Value Input:")
entry=tk.Entry(response_frame,width=5)
response_entry_l=tk.Label(response_frame, text="Response:")
response_entry=tk.Text(response_frame,state='disabled', width=30,height=4, wrap='word')
send_button = tk.Button(response_frame, text="submit", command=schedule_request_wrapper)
label_datetime = tk.Label(calander_frame, text="Input datetime (YYYY-MM-DD HH:MM:SS):")
year = tk.Entry(calander_frame,width=5)
month=tk.Entry(calander_frame,width=5)
day=tk.Entry(calander_frame,width=5)
hour=tk.Entry(calander_frame,width=5)
hl= tk.Label(calander_frame, text=':')
minute=tk.Entry(calander_frame,width=5)
ml=tk.Label(calander_frame, text=':')
second=tk.Entry(calander_frame,width=5)

schedule=tk.Text(calander_frame,state='disabled', width=40,height=5, wrap='word')

#Position of labels,button, text and entry
l1.grid(row=0, column=0, sticky='nw')
l2.grid(row=0, column=1, sticky='w')
l3.grid(row=1, column=0, sticky='nw')
l4.grid(row=1, column=1, sticky='w')
l5.grid(row=2, column=0, sticky='nw')
l6.grid(row=2, column=1, sticky='w')
l7.grid(row=3, column=0, sticky='nw')
l8.grid(row=3, column=1, sticky='w')
l9.grid(row=4, column=0, sticky='nw')
l10.grid(row=4, column=1, sticky='w')
l11.grid(row=5, column=0, sticky='nw')
l12.grid(row=5, column=1, sticky='w')
entryLabel.grid(row=0, column=0, sticky='nw')
entry.grid(row=1, column=0, sticky='nw')
send_button.grid(row=4, column=0, sticky='nw')
response_entry_l.grid(row=2, column=0, sticky='NW')
response_entry.grid(row=3, column=0, sticky='NW')
label_datetime.grid(row=0, column=0,sticky='nw')
year.grid(row=0, column=1,sticky='nw')
month.grid(row=0, column=2,sticky='nw')
day.grid(row=0, column=3,sticky='nw')
hour.grid(row=0, column=4,sticky='nw')
hl.grid(row=0, column=5,sticky='nw')
minute.grid(row=0, column=6,sticky='nw')
ml.grid(row=0, column=7,sticky='nw')
second.grid(row=0, column=8,sticky='nw')
schedule.grid(row=1, column=0,sticky='nw')



myWindow.protocol('WM_DELETE_WINDOW', my_close)
myWindow.mainloop()