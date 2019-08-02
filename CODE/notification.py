import tkinter
from tkinter import ttk

#used Tkinter package of python
window = tkinter.Tk()

#window title
window.title("INFRAMIND")

#geometry of the window that will open
window.geometry("300x250")

#Form data - Firt name field
labelOne = ttk.Label(window, text="First Name")
labelOne.grid(row=0, column=0)

#Form data - last name field
labelTwo = ttk.Label(window, text="Last Name")
labelTwo.grid(row=1, column=0)

#Form data - Favorite sports field
labelThree = ttk.Label(window, text="FavSport")
labelThree.grid(row=2, column=0)

labelFour = ttk.Label(window, text="Stock Update")
labelFour.grid(row=3, column=0)

labelFive = ttk.Label(window, text="Gender")
labelFive.grid(row=4, column=0)

labelSix = ttk.Label(window, text="Age")
labelSix.grid(row=5, column=0)

labelSeven = ttk.Label(window, text="Notification time")
labelSeven.grid(row=6, column=0)

labelEight = ttk.Label(window, text="Interval time")
labelEight.grid(row=7, column=0)

#getting the user data
userFName = tkinter.StringVar()
userLName = tkinter.StringVar()
sport = tkinter.StringVar()
company = tkinter.StringVar()
gender = tkinter.StringVar()
age = tkinter.StringVar()
Notf_t = tkinter.StringVar()
Int_t = tkinter.StringVar()

#storing the entered data of the user
userEntry = ttk.Entry(window, width=26, textvariable=userFName)
userEntry.grid(row=0, column=1)

userEntry = ttk.Entry(window, width=26, textvariable=userLName)
userEntry.grid(row=1, column=1)

set1 = tkinter.OptionMenu(window, sport, "baseball", "basketball", "cricket", "football", "handball", "hockey", "rugby-league", "rugby-union", "soccer", "tennis", "volleyball")
set1.grid(row=2, column=1)

set2 = tkinter.OptionMenu(window, company, "ADANIPORTS", "HINDALCO", "ONGC", "SBIN")
set2.grid(row=3, column=1)

userEntry = ttk.Entry(window, width=26, textvariable=gender)
userEntry.grid(row=4, column=1)

userEntry = ttk.Entry(window, width=26, textvariable=age)
userEntry.grid(row=5, column=1)

userEntry = ttk.Entry(window, width=26, textvariable=Notf_t)
userEntry.grid(row=6, column=1)

userEntry = ttk.Entry(window, width=26, textvariable=Int_t)
userEntry.grid(row=7, column=1)

labela = ttk.Label(window,text = "secs")
labela.grid(row=6, column=2)

labelb = ttk.Label(window,text = "secs")
labelb.grid(row=7, column=2)

# action function
def action():
    print(userFName.get())
    print(userLName.get())
    print(sport.get())
    print(gender.get())
    print(age.get())
    print(Notf_t.get())
    print(Int_t.get())
    window.destroy()

# Submit button for the form . Calls action method for further process
btn = ttk.Button(window, text="Submit", command=action)
btn.grid(row=8, column=0)

# open the window
window.mainloop()

while 1:
    #for generation of delay
    import time

    # displaying the stock market data
    from nsetools import Nse

    # gettinfg the sports data
    import sports

    from win10toast import ToastNotifier

    nse = Nse()

    stocks = {
        "ADANIPORTS": 284.95,
        "HINDALCO": 152.30,
        "ONGC": 279.70,
        "SBIN": 259.70
    }

    qty = {
        "ADANIPORTS": 20,
        "HINDALCO": 20,
        "ONGC": 20,
        "SBIN": 20
    }

    stock = nse.get_quote(str(company.get()))
    stock1Close = stock['closePrice']

    n = str(stock)

    x = sports.all_matches()
    c = x[sport.get()]
    m = str(c)

    notifier = ToastNotifier()
    notifier.show_toast(sport.get(), m, duration=int(Notf_t.get()))
    notifier.show_toast(company.get(), n, duration=int(Notf_t.get()))

    time.sleep(int(Int_t.get()))