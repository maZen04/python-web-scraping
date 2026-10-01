from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter import messagebox

country = "spain"
countries1 = [] # with html code
countries = [] # just names

page = requests.get("https://visaindex.com/")
src = page.content
soup = BeautifulSoup(src,"lxml")
countries1 = soup.find_all("span",{"class":"country-name"})
for country in countries1:
    countries.append(country.text.strip().lower())

# FUNCTIONS
def submit():
    country=entry.get().strip().lower()
    visa_free_access_list = []
    visa_on_arrival_list = []
    eta_list = []

    visa_free_access = []
    visa_on_arrival = []
    eta = []

    if country not in countries:
        entry.delete(0,END)
        messagebox.showerror(title="Error",message="This country doesn't exist.")

    else:
        page = requests.get(f"https://visaindex.com/country/{country}-passport-ranking/")
        entry.delete(0,END)
        src = page.content
        soup = BeautifulSoup(src,'lxml')

        group1 = soup.find("div",{"class":"col-md-6 px-lg-3 col-vfa countries-col"})
        group2 = soup.find("div",{"class":"col-md-6 px-lg-3 col-voa countries-col"})
        group3 = soup.find("div",{"class":"col-md-6 px-lg-3 col-eta countries-col"})

        visa_free_access_list = group1.find_all("span",{"class":"country-name"})
        visa_on_arrival_list = group2.find_all("span",{"class":"country-name"})
        eta_list = group3.find_all("span",{"class":"country-name"})

        for vfa in visa_free_access_list:
            visa_free_access.append(vfa.text.strip())

        for voa in visa_on_arrival_list:
            visa_on_arrival.append(voa.text.strip())

        for e in eta_list:
            eta.append(e.text.strip())
        

        window2 = Toplevel()
        window2.title(country.upper()+"'s Visa")
        window2.geometry('1500x720')

        label1 = Label(window2,text=country.upper(),font=("Ink Free",40,"bold"),bg="black",fg="green",width=20,padx=20,pady=20,bd=5,relief=SUNKEN)
        label1.pack()

        frame2 = Frame(window2,bg="black",bd=5,relief=SUNKEN)
        frame2.place(x=10,y=120)

        label2 = Label(frame2,text="Visa Access Free",font=("Ink Free",20,"bold"),width=20,bg="#f7ffde")
        label2.pack()

        listbox = Listbox(frame2,bg="#f7ffde",font=('Constantia',30),width=20,selectmode=MULTIPLE)
        listbox.pack()
        for i in range(len(visa_free_access)):
            listbox.insert(i+1,visa_free_access[i])

        frame3 = Frame(window2,bg="black",bd=5,relief=SUNKEN)
        frame3.place(x=500,y=120)

        label3 = Label(frame3,text="Visa On Arrival",font=("Ink Free",20,"bold"),width=20,bg="#f7ffde")
        label3.pack()

        listbox = Listbox(frame3,bg="#f7ffde",font=('Constantia',30),width=20,selectmode=MULTIPLE)
        listbox.pack()
        for i in range(len(visa_on_arrival)):
            listbox.insert(i+1,visa_on_arrival[i])

        frame4 = Frame(window2,bg="black",bd=5,relief=SUNKEN)
        frame4.place(x=1000,y=120)

        label4 = Label(frame4,text="ETA",font=("Ink Free",20,"bold"),width=20,bg="#f7ffde")
        label4.pack()

        listbox = Listbox(frame4,bg="#f7ffde",font=('Constantia',30),width=20,selectmode=MULTIPLE)
        listbox.pack()
        for i in range(len(eta)):
            listbox.insert(i+1,eta[i])



def delete():

    entry.delete(0,END)



window = Tk()

window.title("Passports App")
# window.iconphoto(True,passport_icon)
label = Label(window,text="Enter a Country: ",font=("Ink Free",15,"bold"),bg="black",fg="green")
label.pack()

entry = Entry(window,bg="black",fg="green",font=("Ink Free",40),width=15)
entry.pack()

frame = Frame(window,bd=5,relief=RAISED)
frame.pack()

submit_button = Button(frame,font=("Ink Free",15,"bold"),bg="black",fg="green",
                       text="Submit",activebackground="black",activeforeground="green",command=submit)
submit_button.pack(side=LEFT)
delete_button = Button(frame,font=("Ink Free",15,"bold"),bg="black",fg="green",
                       text="Delete",activebackground="black",activeforeground="green",command=delete)
delete_button.pack(side=RIGHT)



window.mainloop()