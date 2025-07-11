from tkinter import *
import random
import time

# Initialize the main Tkinter window
root = Tk()
root.geometry('1000x900')
root.resizable(False, False)
root.title("Hotel Management System")


# Function to calculate total cost of the each item
def totalcost():
    # Generate a random order number
    random_no = random.randint(1, 1000)
    of_on.delete(0, END)
    of_on.insert(0, random_no)

    # Calculate costs for each item
    try:
        item1 = int(f_drink.get() or 0) * 30
        item2 = int(f_burgerKing.get() or 0) * 60
        item3 = int(f_cherry.get() or 0) * 80
        item4 = int(f_nachosFries.get() or 0) * 150
        item5 = int(f_pizza.get() or 0) * 250
        item6 = int(f_biscuit.get() or 0) * 50
        item7 = int(f_roll.get() or 0) * 80
        item8 = int(f_tea.get() or 0) * 20

        prices_of_foods = item1 + item2 + item3 + item4 + item5 + item6 + item7 + item8
        f_cost.delete(0, END)
        f_cost.insert(0, prices_of_foods)

        service_cost = prices_of_foods * 0.005
        f_sc.delete(0, END)
        f_sc.insert(0, f"{service_cost:.2f}")

        service_tax = prices_of_foods * 0.002
        f_tax.delete(0, END)
        f_tax.insert(0, f"{service_tax:.2f}")

        subtotal = prices_of_foods + service_cost + service_tax
        f_st.delete(0, END)
        f_st.insert(0, f"{subtotal:.2f}")

    except ValueError:
        print("Invalid input, please enter numbers only!")


# Function to reset all fields
def reset():
    for entry in [f_drink, f_burgerKing, f_cherry, f_nachosFries, f_pizza, f_biscuit, f_roll, f_tea,
                  of_on, f_cost, f_sc, f_tax, f_st]:
        entry.delete(0, END)


# Function to generate the bill
def generate_bill():
    T.delete('1.0', END)  # Clear the text box
    order_no = of_on.get()
    total_cost = f_cost.get()
    service_charge = f_sc.get()
    tax = f_tax.get()
    subtotal = f_st.get()

    # Add header
    T.insert(END, "  Bill Reciept Of Order\n")
    T.insert(END, "**---***---***---***--** ")
    T.insert(END,"Welcome To Hotel Net-Tech")
    T.insert(END, "--------******-----------")
    T.insert(END, f"Order Number: {order_no}\n")
    T.insert(END, "======================================\n")

    # Add itemized costs
    items = [
        ("Drink", f_drink.get(), 30),
        ("Burger King", f_burgerKing.get(), 60),
        ("Cherry", f_cherry.get(), 80),
        ("Nachos Fries", f_nachosFries.get(), 150),
        ("Pizza", f_pizza.get(), 250),
        ("Biscuit", f_biscuit.get(), 50),
        ("Roll", f_roll.get(), 80),
        ("Tea", f_tea.get(), 20),
    ]

    for item, qty, price in items:
        if qty and qty.isdigit() and int(qty) > 0:
            T.insert(END, f"{item}: {qty} x {price} = Rs {int(qty) * price}\n")

    # Add cost breakdown
    T.insert(END, "======================================\n")
    T.insert(END, f"Total Cost: Rs {total_cost}\n")
    T.insert(END, f"Service Charge: Rs {service_charge}\n")
    T.insert(END, f"Tax: Rs {tax}\n")
    T.insert(END, f"Sub Total: Rs {subtotal}\n")
    T.insert(END, "======================================\n")
    T.insert(END, f"For the online Booking ororder contact on:-254 55 54\n")
    T.insert(END, "======================================\n")
    T.insert(END, f"Thank you for dining withus visit again!\n")


# Function to show price list in a listbox
def price():
    if list_box.winfo_ismapped():
        list_box.pack_forget()
    else:
        list_box.pack()


# Time display function
def tellmeTime():
    return time.strftime('%H:%M:%S')


def updateLabel():
    Time.configure(text=tellmeTime())
    root.after(1000, updateLabel)


# Top Frame
frame = Frame(root, bd=15, relief=GROOVE)
Label(frame, text='HOTEL Net-Tech Management', font=['Arial', 30, 'bold'],fg="red", width=42, height=2).grid(row=0, column=0)
frame.pack()

# Left Side Frame1
frame1 = Frame(root, bg='Yellow', relief='sunken', borderwidth=10)
labels = ["Drink:", "Burger King:", "Cherry:", "Nachos Fries:", "Pizza:", "Biscuit:", "Roll:", "Tea:"]
entries = []
for i, text in enumerate(labels):
    Label(frame1, text=text,font=['Arial',10]).grid(row=i, column=0, sticky=W, padx=20, pady=20)
    entry = Entry(frame1, width=20, font=['Arial', 12])
    entry.grid(row=i, column=1, sticky=W, columnspan=12)
    entries.append(entry)

f_drink, f_burgerKing, f_cherry, f_nachosFries, f_pizza, f_biscuit, f_roll, f_tea = entries
frame1.place(x=10, y=150, width=350, height=500)

# Right Side Frame2
frame2 = Frame(root, bg='Purple', relief='sunken', borderwidth=10)
Label2 = ["Order Number", "Cost", "Service Cost", "Tax", "Sub Total"]
outputs = []
for i, text in enumerate(Label2):
    Label(frame2, text=text,font=['Arial',10]).grid(row=i, column=0, sticky=W, padx=20, pady=20)
    output = Entry(frame2, width=12, font=['Arial', 12])
    output.grid(row=i, column=1, sticky=W, columnspan=5)
    outputs.append(output)

of_on, f_cost, f_sc, f_tax, f_st = outputs
frame2.place(x=370, y=150, width=350, height=500)

# Bottom Buttons Frame3
frame3 = Frame(root, bg='Pink', relief='sunken', borderwidth=10)
Button(frame3, text='Price', font='Cambria', width=5, height=2,relief='sunken',borderwidth=10, command=price).place(x=40, y=10)
Button(frame3, text='Total', font='Cambria', width=5, height=2,relief='sunken',borderwidth=10, command=totalcost).place(x=180, y=10)
Button(frame3, text='Reset', font='Cambria', width=5, height=2,relief='sunken',borderwidth=10, command=reset).place(x=320, y=10)
Button(frame3, text='Bill', font='Cambria', width=5, height=2,relief='sunken' ,borderwidth=10, command=generate_bill).place(x=450, y=10)
Button(frame3, text='Quit', font='Cambria', width=5, height=2,relief='sunken' ,borderwidth=10, command=root.destroy).place(x=600, y=10)

frame3.place(x=10, y=670, width=720, height=100)


# Text Area for Bill
T = Text(root, height=8, width=25, padx=14, pady=15, relief='sunken', borderwidth=10)
T.place(x=740, y=610)

# Listbox for Price
list_box = Listbox(root)
prices = ["Drinks: Rs 30", "Burger King: Rs 60", "Cherry: Rs 80", "Nachos Fries: Rs 150",
          "Pizza: Rs 250", "Biscuit: Rs 50", "Roll: Rs 80", "Tea: Rs 20"]
for price in prices:
    list_box.insert(END, price)

# Time Display
Time = Label(root, text=tellmeTime(), background='Orange', foreground='Black', font=['arial', 38], relief='groove',borderwidth=10)
Time.place(x=750, y=150)
root.after(1000, updateLabel)
# Calculator
value = ""
data = StringVar()


def Buttonclick(number):
    global value
    value += str(number)
    data.set(value)


def clearButton():
    global value
    value = ""
    data.set("")


def Buttonequal():
    global value
    try:
        result = eval(value)
        data.set(result)
    except Exception as e:
        data.set("Error")
        value = ""


frame5 = Frame(root, relief='sunken', bg='Silver', bd=10)

Entry(frame5, textvariable=data, font=['arial', 30], width=10).grid(row=0, column=0)

calculator_buttons = [
    ('1', 10, 60), ('2', 60, 60), ('3', 110, 60), ('+', 160, 60),
    ('4', 10, 120), ('5', 60, 120), ('6', 110, 120), ('-', 160, 120),
    ('7', 10, 180), ('8', 60, 180), ('9', 110, 180), ('*', 160, 180),
    ('C', 10, 240), ('0', 60, 240), ('=', 110, 240), ('/', 160, 240),

]

for text, x, y in calculator_buttons:
    Button(frame5, text=text, height=2, width=4,relief='groove', bd=5,command=lambda t=text: Buttonclick(t) if t not in ['C', '='] else clearButton() if t == 'C' else Buttonequal()).place(x=x, y=y)
frame5.place(x=740, y=250, width=240, height=350)

root.mainloop()
