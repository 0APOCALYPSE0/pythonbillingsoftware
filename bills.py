from tkinter import *
from tkinter import messagebox
import math, random, os
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x763+0+0")
        self.root.title("Billing Software")
        bgColor="#074463"
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg=bgColor, fg="white", font=("times new roman",30,"bold"), pady=2).pack(fill=X)

        #============= Variables =========================
        #========= Cosmetics Variables ===================
        self.soap = IntVar()
        self.faceCream = IntVar()
        self.faceWash = IntVar()
        self.spray = IntVar()
        self.gel = IntVar()
        self.lotin = IntVar()

        #========= Grocery Variables ===================
        self.rice = IntVar()
        self.oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        #========= Cold Drinks Variables ===================
        self.maza = IntVar()
        self.coca = IntVar()
        self.frooti = IntVar()
        self.sprite = IntVar()
        self.pepsi = IntVar()
        self.limca = IntVar()

        #=========Total Price and Tax Variables ============
        self.cosmeticsPrice = StringVar()
        self.groceriesPrice = StringVar()
        self.coldDrinksPrice = StringVar()

        self.cosmeticsTax = StringVar()
        self.groceriesTax = StringVar()
        self.coldDrinksTax = StringVar()

        #============Customer Variables ====================
        self.cName = StringVar()
        self.cPhone = StringVar()
        self.billNo = StringVar()
        number = random.randint(1000,9999)
        self.billNo.set(str(number))
        self.searchBill = StringVar()
 
        #========= Customer Details Frame ================
        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=("times new roman",15,"bold"), fg="gold", bg=bgColor)
        F1.place(x=0, y=80, relwidth=1)

        cName = Label(F1, text="Customer Name", bg=bgColor, fg="white", font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cNameIn = Entry(F1, width=15, textvariable=self.cName, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cPhone = Label(F1, text="Phone No.", bg=bgColor, fg="white", font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cPhoneIn = Entry(F1, width=15, textvariable=self.cPhone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        cBill = Label(F1, text="Bill Number", bg=bgColor, fg="white", font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cBillIn = Entry(F1, width=15, textvariable=self.searchBill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        billBTN = Button(F1, text="Search", command=self.findBill, width=10, bd=7, font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        #============= Cosmetics Frame =====================
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman",15,"bold"), fg="gold", bg=bgColor)
        F2.place(x=5, y=180, width=325, height=380)

        bath = Label(F2, text="Bath Soap", bg=bgColor, fg="lightgreen", font=("times new roman",16,"bold")).grid(row=0,column=0,padx=20,pady=5,sticky="w")
        bathIn = Entry(F2, width=10, textvariable=self.soap, font=('times new roman',16,"bold"), bd=5, relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        faceCream = Label(F2, text="Face Cream", bg=bgColor, fg="lightgreen", font=("times new roman",16,"bold")).grid(row=1,column=0,padx=20,pady=5,sticky="w")
        faceCreamIn = Entry(F2, width=10, textvariable=self.faceCream, font=('times new roman',16,"bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        faceWash = Label(F2, text="Face Wash", bg=bgColor, fg="lightgreen", font=("times new roman",16,"bold")).grid(row=2,column=0,padx=20,pady=5,sticky="w")
        faceWashIn = Entry(F2, width=10, textvariable=self.faceWash, font=('times new roman',16,"bold"), bd=5, relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        hairSpray = Label(F2, text="Hair Spray", bg=bgColor, fg="lightgreen", font=("times new roman",16,"bold")).grid(row=3,column=0,padx=20,pady=5,sticky="w")
        hairSprayIn = Entry(F2, width=10, textvariable=self.spray, font=('times new roman',16,"bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        hairGel = Label(F2, text="Hair Gel", bg=bgColor, fg="lightgreen", font=("times new roman",16,"bold")).grid(row=4,column=0,padx=20,pady=5,sticky="w")
        hairGelIn = Entry(F2, width=10, textvariable=self.gel, font=('times new roman',16,"bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        bodyLotion = Label(F2, text="Body Lotion", bg=bgColor, fg="lightgreen", font=("times new roman",16,"bold")).grid(row=5,column=0,padx=20,pady=5,sticky="w")
        bodyLotionIn = Entry(F2, width=10, textvariable=self.lotin, font=('times new roman',16,"bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

        #============= Grocery Frame =====================
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("times new roman",15,"bold"), fg="gold", bg=bgColor)
        F3.place(x=340, y=180, width=325, height=380)

        rice = Label(F3, text="Rice", bg=bgColor, fg="lightgreen", font=("times new roman",16,"bold")).grid(row=0,column=2,padx=20,pady=5,sticky="w")
        riceIn = Entry(F3, width=10, textvariable=self.rice, font=('times new roman',16,"bold"), bd=5, relief=SUNKEN).grid(row=0,column=3,pady=10,padx=10)

        foodOil = Label(F3, text="Food Oil", bg=bgColor, fg="lightgreen", font=("times new roman",16,"bold")).grid(row=1,column=2,padx=20,pady=5,sticky="w")
        foodOilIn = Entry(F3, width=10, textvariable=self.oil, font=('times new roman',16,"bold"), bd=5, relief=SUNKEN).grid(row=1,column=3,pady=10,padx=10)

        daal = Label(F3, text="Daal", bg=bgColor, fg="lightgreen", font=("times new roman",16,"bold")).grid(row=2,column=2,padx=20,pady=5,sticky="w")
        daalIn = Entry(F3, width=10, textvariable=self.daal, font=('times new roman',16,"bold"), bd=5, relief=SUNKEN).grid(row=2,column=3,pady=10,padx=10)

        wheat = Label(F3, text="Wheat", bg=bgColor, fg="lightgreen", font=("times new roman",16,"bold")).grid(row=3,column=2,padx=20,pady=5,sticky="w")
        wheatIn = Entry(F3, width=10, textvariable=self.wheat, font=('times new roman',16,"bold"), bd=5, relief=SUNKEN).grid(row=3,column=3,pady=10,padx=10)

        sugar = Label(F3, text="Sugar", bg=bgColor, fg="lightgreen", font=("times new roman",16,"bold")).grid(row=4,column=2,padx=20,pady=5,sticky="w")
        sugarIn = Entry(F3, width=10, textvariable=self.sugar, font=('times new roman',16,"bold"), bd=5, relief=SUNKEN).grid(row=4,column=3,pady=10,padx=10)

        tea = Label(F3, text="Tea", bg=bgColor, fg="lightgreen", font=("times new roman",16,"bold")).grid(row=5,column=2,padx=20,pady=5,sticky="w")
        teaIn = Entry(F3, width=10, textvariable=self.tea, font=('times new roman',16,"bold"), bd=5, relief=SUNKEN).grid(row=5,column=3,pady=10,padx=10)

        #============= Cold Drinks Frame =====================
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks", font=("times new roman",15,"bold"), fg="gold", bg=bgColor)
        F4.place(x=670, y=180, width=325, height=380)

        maza = Label(F4, text="Maza", bg=bgColor, fg="lightgreen", font=("times new roman",16,"bold")).grid(row=0,column=0,padx=20,pady=5,sticky="w")
        mazaIn = Entry(F4, width=10, textvariable=self.maza, font=('times new roman',16,"bold"), bd=5, relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        coca = Label(F4, text="Coca Cola", bg=bgColor, fg="lightgreen", font=("times new roman",16,"bold")).grid(row=1,column=0,padx=20,pady=5,sticky="w")
        cocaIn = Entry(F4, width=10, textvariable=self.coca, font=('times new roman',16,"bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        frooti = Label(F4, text="Frooti", bg=bgColor, fg="lightgreen", font=("times new roman",16,"bold")).grid(row=2,column=0,padx=20,pady=5,sticky="w")
        frootiIn = Entry(F4, width=10, textvariable=self.frooti, font=('times new roman',16,"bold"), bd=5, relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        sprite = Label(F4, text="Sprite", bg=bgColor, fg="lightgreen", font=("times new roman",16,"bold")).grid(row=3,column=0,padx=20,pady=5,sticky="w")
        spriteIn = Entry(F4, width=10, textvariable=self.sprite, font=('times new roman',16,"bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        pepsi = Label(F4, text="Pepsi", bg=bgColor, fg="lightgreen", font=("times new roman",16,"bold")).grid(row=4,column=0,padx=20,pady=5,sticky="w")
        pepsiIn = Entry(F4, width=10, textvariable=self.pepsi, font=('times new roman',16,"bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        limca = Label(F4, text="Limca", bg=bgColor, fg="lightgreen", font=("times new roman",16,"bold")).grid(row=5,column=0,padx=20,pady=5,sticky="w")
        limcaIn = Entry(F4, width=10, textvariable=self.limca, font=('times new roman',16,"bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

        #============== Bills Area =============================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)

        billTitle = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill="x")
        scrollY = Scrollbar(F5, orient=VERTICAL)
        self.textArea = Text(F5, yscrollcommand=scrollY.set)
        scrollY.pack(side=RIGHT, fill=Y)
        scrollY.config(command=self.textArea.yview)
        self.textArea.pack(fill=BOTH, expand=1)

        #================ Button Frame ==========================
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman",15,"bold"), fg="gold", bg=bgColor)
        F6.place(x=0, y=560, relwidth=1, height=140)

        totalCosmetics = Label(F6, text="Total Cosmetics Price", bg=bgColor, fg="lightgreen", font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        totalCosmeticsIn = Entry(F6, width=18, textvariable=self.cosmeticsPrice, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0,column=1,pady=1,padx=10)

        totalGrocery = Label(F6, text="Total Grocery Price", bg=bgColor, fg="lightgreen", font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        totalGroceryIn = Entry(F6, width=18, textvariable=self.groceriesPrice, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1,column=1,pady=1,padx=10)

        totalColdDrinks = Label(F6, text="Total Cold Drinks Price", bg=bgColor, fg="lightgreen", font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        totalColdDrinksIn = Entry(F6, width=18, textvariable=self.coldDrinksPrice, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2,column=1,pady=1,padx=10)

        cosmeticsTax = Label(F6, text="Cosmetics Tax", bg=bgColor, fg="lightgreen", font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        cosmeticsTaxIn = Entry(F6, width=18, textvariable=self.cosmeticsTax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0,column=3,pady=1,padx=10)

        groceryTax = Label(F6, text="Grocery Tax", bg=bgColor, fg="lightgreen", font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        groceryTaxIn = Entry(F6, width=18, textvariable=self.groceriesTax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1,column=3,pady=1,padx=10)

        coldDrinksTax = Label(F6, text="Cold Drinks Tax", bg=bgColor, fg="lightgreen", font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        coldDrinksTaxIn = Entry(F6, width=18, textvariable=self.coldDrinksTax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2,column=3,pady=1,padx=10)


        btnFrame = Frame(F6, bd=7, relief=GROOVE)
        btnFrame.place(x=750, width=580, height=105)

        totalBtn = Button(btnFrame, text="Total", command=self.total, bg="Cadetblue", fg="white", bd=2, pady=15, width=10, font="arial 15 bold").grid(row=0, column=0, padx=5, pady=5)
        billBtn = Button(btnFrame, text="Generate Bill", command=self.billArea, bg="Cadetblue", fg="white", bd=2, pady=15, width=10, font="arial 15 bold").grid(row=0, column=1, padx=5, pady=5)
        clearBtn = Button(btnFrame, text="Clear", command=self.clear, bg="Cadetblue", fg="white", bd=2, pady=15, width=10, font="arial 15 bold").grid(row=0, column=2, padx=5, pady=5)
        exitBtn = Button(btnFrame, text="Exit", command=self.exit, bg="Cadetblue", fg="white", bd=2, pady=15, width=10, font="arial 15 bold").grid(row=0, column=3, padx=5, pady=5)
        self.welcomeBill()

    def total(self):
        self.soapPrice = (self.soap.get()*40)
        self.faceCreamPrice = (self.faceCream.get()*120)
        self.faceWashPrice = (self.faceWash.get()*60)
        self.gelPrice = (self.gel.get()*140)
        self.sprayPrice = (self.spray.get()*180)
        self.lotionPrice = (self.lotin.get()*180)
        self.totalCosmeticPrice = float(
            self.soapPrice+
            self.faceCreamPrice+
            self.faceWashPrice+
            self.gelPrice+
            self.sprayPrice+
            self.lotionPrice
        )
        self.cosmeticsPrice.set("Rs. "+str(self.totalCosmeticPrice))
        self.cTax = round((self.totalCosmeticPrice*0.15),2)
        self.cosmeticsTax.set("Rs. "+str(self.cTax))

        self.ricePrice = (self.rice.get()*180)
        self.oilPrice = (self.oil.get()*180)
        self.daalPrice = (self.daal.get()*60)
        self.wheatPrice = (self.wheat.get()*240)
        self.sugarPrice = (self.sugar.get()*45)
        self.teaPrice = (self.tea.get()*150)
        self.totalGroceryPrice = float(
            self.ricePrice+
            self.oilPrice+
            self.daalPrice+
            self.wheatPrice+
            self.sugarPrice+
            self.teaPrice
        )
        self.groceriesPrice.set("Rs. "+str(self.totalGroceryPrice))
        self.gTax = round((self.totalGroceryPrice*0.05),2)
        self.groceriesTax.set("Rs. "+str(self.gTax))

        self.mazaPrice = (self.maza.get()*60)
        self.cocaPrice = (self.coca.get()*70)
        self.frootiPrice = (self.frooti.get()*50)
        self.pepsiPrice = (self.pepsi.get()*55)
        self.limcaPrice = (self.limca.get()*70)
        self.spritePrice = (self.sprite.get()*60)
        self.totalColdDrinkPrice = float(
            self.mazaPrice+
            self.cocaPrice+
            self.frootiPrice+
            self.pepsiPrice+
            self.limcaPrice+
            self.spritePrice
        )
        self.coldDrinksPrice.set("Rs. "+str(self.totalColdDrinkPrice))
        self.cdTax = round((self.totalColdDrinkPrice*0.1),2)
        self.coldDrinksTax.set("Rs. "+str(self.cdTax))

        self.totalBill = float(
            self.totalCosmeticPrice+
            self.totalGroceryPrice+
            self.totalColdDrinkPrice+
            self.cTax+
            self.gTax+
            self.cdTax
        )

    def welcomeBill(self):
        self.textArea.delete("1.0", END)
        self.textArea.insert(END, "\t Welcome General Store \n")
        self.textArea.insert(END, f"\n Bill Number:   {self.billNo.get()}")
        self.textArea.insert(END, f"\n Customer Name: {self.cName.get()}")
        self.textArea.insert(END, f"\n Phone Number:  {self.cPhone.get()}")
        self.textArea.insert(END, f"\n =====================================")
        self.textArea.insert(END, f"\n Products \t\t Qty \t\t Price")
        self.textArea.insert(END, f"\n =====================================")

    def billArea(self):
        if self.cName.get() == "" or self.cPhone.get() == "":
            messagebox.showerror("Error", "Customer details can not be empty.")
        elif self.cosmeticsPrice.get() == "Rs. 0.0" and self.groceriesPrice.get() == "Rs. 0.0" and self.coldDrinksPrice.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No product added.")
        else:
            self.welcomeBill()
            #========== Cosmetics =====================
            if self.soap.get() != 0:
                self.textArea.insert(END, f"\n Bath Soap   \t\t {self.soap.get()} \t\t {self.soapPrice}")
            if self.faceCream.get() != 0:
                self.textArea.insert(END, f"\n Face Cream  \t\t {self.faceCream.get()} \t\t {self.faceCreamPrice}")
            if self.faceWash.get() != 0:
                self.textArea.insert(END, f"\n Face Wash   \t\t {self.faceWash.get()} \t\t {self.faceWashPrice}")
            if self.gel.get() != 0:
                self.textArea.insert(END, f"\n Hair Gel    \t\t {self.gel.get()} \t\t {self.gelPrice}")
            if self.spray.get() != 0:
                self.textArea.insert(END, f"\n Hair Spray  \t\t {self.spray.get()} \t\t {self.sprayPrice}")
            if self.lotin.get() != 0:
                self.textArea.insert(END, f"\n Body Lotion \t\t {self.lotin.get()} \t\t {self.lotionPrice}")

            #========== Groceries =====================
            if self.rice.get() != 0:
                self.textArea.insert(END, f"\n Rice        \t\t {self.rice.get()} \t\t {self.ricePrice}")
            if self.oil.get() != 0:
                self.textArea.insert(END, f"\n Food Oil    \t\t {self.oil.get()} \t\t {self.oilPrice}")
            if self.daal.get() != 0:
                self.textArea.insert(END, f"\n Daal        \t\t {self.daal.get()} \t\t {self.daalPrice}")
            if self.wheat.get() != 0:
                self.textArea.insert(END, f"\n Wheat       \t\t {self.wheat.get()} \t\t {self.wheatPrice}")
            if self.sugar.get() != 0:
                self.textArea.insert(END, f"\n Sugar       \t\t {self.sugar.get()} \t\t {self.sugarPrice}")
            if self.tea.get() != 0:
                self.textArea.insert(END, f"\n Tea         \t\t {self.tea.get()} \t\t {self.teaPrice}")

            #========== Cold Drinks =====================
            if self.maza.get() != 0:
                self.textArea.insert(END, f"\n Maza        \t\t {self.maza.get()} \t\t {self.mazaPrice}")
            if self.coca.get() != 0:
                self.textArea.insert(END, f"\n Coca Cola   \t\t {self.coca.get()} \t\t {self.cocaPrice}")
            if self.frooti.get() != 0:
                self.textArea.insert(END, f"\n Frooti      \t\t {self.frooti.get()} \t\t {self.frootiPrice}")
            if self.pepsi.get() != 0:
                self.textArea.insert(END, f"\n Pepsi       \t\t {self.pepsi.get()} \t\t {self.pepsiPrice}")
            if self.limca.get() != 0:
                self.textArea.insert(END, f"\n Limca       \t\t {self.limca.get()} \t\t {self.limcaPrice}")
            if self.sprite.get() != 0:
                self.textArea.insert(END, f"\n Sprite      \t\t {self.sprite.get()} \t\t {self.spritePrice}")

            self.textArea.insert(END, f"\n -------------------------------------")
            if self.cosmeticsTax.get() != "Rs. 0.0":
                self.textArea.insert(END, f"\n Cosmetic Tax:   \t\t\t {self.cosmeticsTax.get()}")
            if self.groceriesTax.get() != "Rs. 0.0":
                self.textArea.insert(END, f"\n Grocery Tax:    \t\t\t {self.groceriesTax.get()}")
            if self.coldDrinksTax.get() != "Rs. 0.0":
                self.textArea.insert(END, f"\n Cold Drink Tax: \t\t\t {self.coldDrinksTax.get()}")
            self.textArea.insert(END, f"\n\n Total Bill:    \t\t\t Rs. {self.totalBill}")
            self.textArea.insert(END, f"\n -------------------------------------")
            self.saveBill()

    def saveBill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op>0:
            self.billData = self.textArea.get("1.0", END)
            f1 =  open("Bills/"+str(self.billNo.get())+".txt","w")
            f1.write(self.billData) 
            f1.close()
            messagebox.showinfo("saved",f"Bill {self.billNo.get()} saved.")
        else:
            return  

    def findBill(self):
        present = "no"
        for i in os.listdir("Bills/"):
            if i.split(".")[0]==self.searchBill.get():
                f1 = open(f"Bills/{i}","r")
                self.textArea.delete("1.0", END)
                for d in f1:
                    self.textArea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Bill Not Found.")

    def clear(self):
        op=messagebox.askyesno("Clear", "Do you want to clear.")
        if op>0:
            #============= Variables =========================
            #========= Cosmetics Variables ===================
            self.soap.set(0)
            self.faceCream.set(0)
            self.faceWash.set(0)
            self.spray.set(0)
            self.gel.set(0)
            self.lotin.set(0)

            #========= Grocery Variables ===================
            self.rice.set(0)
            self.oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            #========= Cold Drinks Variables ===================
            self.maza.set(0)
            self.coca.set(0)
            self.frooti.set(0)
            self.sprite.set(0)
            self.pepsi.set(0)
            self.limca.set(0)

            #=========Total Price and Tax Variables ============
            self.cosmeticsPrice.set("")
            self.groceriesPrice.set("")
            self.coldDrinksPrice.set("")

            self.cosmeticsTax.set("")
            self.groceriesTax.set("")
            self.coldDrinksTax.set("")

            #============Customer Variables ====================
            self.cName.set("")
            self.cPhone.set("")
            self.billNo.set("")
            number = random.randint(1000,9999)
            self.billNo.set(str(number))
            self.searchBill.set("")
            self.welcomeBill()

    def exit(self):
        op=messagebox.askyesno("Exit", "Do you want to exit.")
        if op>0:
            self.root.destroy()

root = Tk()
obj = Bill_App(root)
root.mainloop()