from tkinter import *
import random
import time
import datetime
from tkinter import messagebox, ttk

root=Tk()
root.geometry("1550x850+0+0")
root.title("Restaurant Management System\n")
root.configure(background='black')
# ========================================================================================================
#                                FRAMES
#========================================================================================================
Tops = Frame(root, width=1550, height=80, bd=12, relief="raise")
Tops.pack(side = TOP)
lblTitle = Label(Tops, font=("arial", 50, 'bold'), text="     Restaurant Management System(NiGhtte)          ")
lblTitle.grid(row=0, column=0)


#==================================DATE TIME======================================================
localtime=time.asctime(time.localtime(time.time()))
lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
#===================================================================================================


BottomMainFrame = Frame(root, width=1550, height=770, bd=12, relief="raise")
BottomMainFrame.pack(side=BOTTOM)

f1 = Frame(BottomMainFrame, width=500, height=770, bd=12, relief=SUNKEN)
f1.pack(side=LEFT)

f1top = Frame(f1, width=500, height=570, bd=12, relief="raise")
f1top.pack(side=TOP)
f1bottom = Frame(f1, width=500, height=200, bd=12, relief="raise")
f1bottom.pack(side=BOTTOM)


f2 = Frame(BottomMainFrame, width=400, height=770, bd=12, relief=SUNKEN)
f2.pack(side=LEFT)
f2Top = Frame(f2, width=400, height=350, bd=4, relief="raise")
f2Top.pack(side=TOP)
f2Bottom = Frame(f2, width=400, height=450,bd=4, relief="raise")
f2Bottom.pack(side=BOTTOM)

f3 = Frame(BottomMainFrame, width=400, height=770, bd=12, relief=SUNKEN)
f3.pack(side=RIGHT)

f3top = Frame(f3, width=400, height=770, bd=12, relief="raise")
f3top.pack(side=TOP)
f3bottom = Frame(f3, width=400, height=100, bd=12, relief="raise")
f3bottom.pack(side=BOTTOM)

# ========================================================================================================
#                                VARIABLES
#========================================================================================================
Receipt_Ref = StringVar()
DateofOrder = StringVar()
DateofOrder.set(time.strftime("%d/%m/%y"))


var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var100 = IntVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var100.set(0)

#====================================BOTTOM FRAME : FRAME 1 VARIABLES==================================================
varFries = StringVar()
vaMADalad = StringVar()
varHamburger = StringVar()
varLittiChokha = StringVar()
varChickenSalad = StringVar()
varCheeseSandwich = StringVar()
varChickenSandwich = StringVar()
varFishSandwich = StringVar()

varFries.set(0)
vaMADalad.set(0)
varHamburger.set(0)
varLittiChokha.set(0)
varChickenSalad.set(0)
varCheeseSandwich.set(0)
varChickenSandwich.set(0)
varFishSandwich.set(0)

#====================================BOTTOM FRAME : FRAME 2 TOP FRAME VARIABLES==================================================
varChocoBrownie = StringVar()
varIceCream = StringVar()
varPanini = StringVar()
varChawarma = StringVar()
varTacos = StringVar()

varChocoBrownie.set(0)
varIceCream.set(0)
varPanini.set(0)
varChawarma.set(0)
varTacos.set(0)

#====================================BOTTOM FRAME : FRAME 2 BOTTOM FRAME VARIABLES==================================================
varTotal = StringVar()
varCGST = StringVar()
vaMADGST = StringVar()
vaMADerviceCharge = StringVar()
varPay = StringVar()
varPM = StringVar()
varTotal.set(0)
varCGST.set(0)
vaMADGST.set(0)
vaMADerviceCharge.set(0)
varPay.set(0)

#====================================BOTTOM FRAME : FRAME 3 VARIABLES==================================================
varTea = StringVar()
varCola = StringVar()
varCoffee = StringVar()
varOrange = StringVar()
varWater= StringVar()
varChocolateShake = StringVar()
varFruitCocktail = StringVar()
varVanillaShake = StringVar()
varOreoKrusher = StringVar()

varTea.set(0)
varCoffee.set(0)
varCola.set(0)
varOrange.set(0)
varWater.set(0)
varChocolateShake.set(0)
varFruitCocktail.set(0)
varVanillaShake.set(0)
varOreoKrusher.set(0)


#================================================================================
#                       BUTTON FUNCTIONS
# ================================================================================

#========================EXIT FUNCTION======================================
def iExit():
    qExit = messagebox.askyesno("Restraunt Management","Do you want to quit ?")
    if qExit > 0:
        root.destroy()
        return 
    
#========================RESET FUNCTION======================================

def Reset():
    varFries.set(0)
    vaMADalad.set(0)
    varHamburger.set(0)
    varLittiChokha.set(0)
    varChickenSalad.set(0)
    varCheeseSandwich.set(0)
    varChickenSandwich.set(0)
    varFishSandwich.set(0)
    varChocoBrownie.set(0)
    varIceCream.set(0)
    varPanini.set(0)
    varChawarma.set(0)
    varTacos.set(0)
    varTotal.set(0)
    varCGST.set(0)
    vaMADGST.set(0)
    vaMADerviceCharge.set(0)
    varPay.set(0)
    varTea.set(0)
    varCoffee.set(0)
    varCola.set(0)
    varOrange.set(0)
    varWater.set(0)
    varChocolateShake.set(0)
    varFruitCocktail.set(0)
    varVanillaShake.set(0)
    varOreoKrusher.set(0)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)

    txtFries.configure(state=DISABLED)
    txtSalad.configure(state=DISABLED)
    txtHamburger.configure(state=DISABLED)
    txtLittiChokha.configure(state=DISABLED)
    txtChickenSalad.configure(state=DISABLED)
    txtCheeseSandwich.configure(state=DISABLED)
    txtChickenSandwich.configure(state=DISABLED)
    txtFishSandwich.configure(state=DISABLED)
    txtChocoBrownie.configure(state=DISABLED)
    txtIceCream.configure(state=DISABLED)
    txtPanini.configure(state=DISABLED)
    txtChawarma.configure(state=DISABLED)
    txtTacos.configure(state=DISABLED)
    txtTotal.configure(state=DISABLED)
    txtCGST.configure(state=DISABLED)
    txtSGST.configure(state=DISABLED)
    txtServiceCharge.configure(state=DISABLED)
    txtpay.configure(state=DISABLED)
    txtTea.configure(state=DISABLED)
    txtCoffee.configure(state=DISABLED)
    txtCola.configure(state=DISABLED)
    txtOrange.configure(state=DISABLED)
    txtWater.configure(state=DISABLED)
    txtChocolateShake.configure(state=DISABLED)
    txtOreoKrusher.configure(state=DISABLED)
    txtVanillaShake.configure(state=DISABLED)
    txtOreoKrusher.configure(state=DISABLED)




# ===============================================================
#                       RECEIPT FUMCTION
# ================================================================

def Receipt():
    roor = Tk()
    roor.geometry("600x700+0+0")

    f1 = Frame(roor, width = 1600, height = 700, bd = 12, relief = "raise")
    f1.pack()
    lblReceipt = Label(f1, font=('arial', 12, 'bold'), text="Receipt", bd=2, anchor='w')
    lblReceipt.grid(row=0, column=0, sticky=W)
    txtReceipt = Text(f1, width=64, height=35, bg="white", bd=8, font=('arial', 11, 'bold'))
    txtReceipt.grid(row=1, column=0)
    txtReceipt.delete("1.0", END)
    x = random.randint(1000, 500890)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t'+ Receipt_Ref.get() + '\t\t\t' + DateofOrder.get()+"\n")
    txtReceipt.insert(END, 'Items\t\t\t\t' + "No. of Items \n\n")
    txtReceipt.insert(END, 'Fries:\t\t\t\t\t' + varFries.get() + "\n")
    txtReceipt.insert(END, 'Salad: \t\t\t\t\t' + vaMADalad.get() + "\n")
    txtReceipt.insert(END, 'HamBurger: \t\t\t\t\t' + varHamburger.get() + "\n")
    txtReceipt.insert(END, 'Litti-Chokha: \t\t\t\t\t' + varLittiChokha.get() + "\n")
    txtReceipt.insert(END, 'Chicken Salad: \t\t\t\t\t' + varChickenSalad.get() + "\n")
    txtReceipt.insert(END, 'Cheese Sandwhich: \t\t\t\t\t' + varCheeseSandwich.get() + "\n")
    txtReceipt.insert(END, 'Chicken Sandwhich: \t\t\t\t\t' + varChickenSandwich.get() + "\n")
    txtReceipt.insert(END, 'Fish Sandwhich: \t\t\t\t\t' + varFishSandwich.get() + "\n")
    txtReceipt.insert(END, 'Choco Brownie: \t\t\t\t\t' + varChocoBrownie.get() + "\n")
    txtReceipt.insert(END, 'IceCream: \t\t\t\t\t' + varIceCream.get() + "\n")
    txtReceipt.insert(END, 'Panini: \t\t\t\t\t' + varPanini.get() + "\n")
    txtReceipt.insert(END, 'Chawarma: \t\t\t\t\t' + varChawarma.get() + "\n")
    txtReceipt.insert(END, 'Tacos: \t\t\t\t\t' + varTacos.get() + "\n")
    txtReceipt.insert(END, 'Tea: \t\t\t\t\t' + varTea.get() + "\n")
    txtReceipt.insert(END, 'Coffee: \t\t\t\t\t' + varCoffee.get() + "\n")
    txtReceipt.insert(END, 'Cola: \t\t\t\t\t' + varCola.get() + "\n")
    txtReceipt.insert(END, 'Orange Juice: \t\t\t\t\t' + varOrange.get() + "\n")
    txtReceipt.insert(END, 'Water: \t\t\t\t\t' + varWater.get() + "\n")
    txtReceipt.insert(END, 'Chocolate Shake: \t\t\t\t\t' + varChocolateShake.get() + "\n")
    txtReceipt.insert(END, 'Fruit Cocktail: \t\t\t\t\t' + varFruitCocktail.get() + "\n")
    txtReceipt.insert(END, 'Vanilla Shake: \t\t\t\t\t' + varVanillaShake.get() + "\n")
    txtReceipt.insert(END, 'Oreo Krusher: \t\t\t\t\t' + varOreoKrusher.get() + "\n")
    txtReceipt.insert(END, '\nTotal Cost of Food: \t\t' + varTotal.get() + "\nCGST:\t\t" + varCGST.get() + "\nSGST:\t\t" +
                      vaMADGST.get() + "\nService Charge:\t\t" + vaMADerviceCharge.get() + "\nTotal Payble amount:\t\t" + varPay.get())
    roor.mainloop()


#================================================PRICE LIST=======================================
def price_list():
    roo = Tk()
    roo.geometry("600x700+0+0")
    roo.title("Price List")

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Salad", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Hamburger", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Litti-Chokha", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="15", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chicken Salad", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Sandwhich", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chicken Sandwhich", fg="steel blue", anchor=W)
    lblinfo.grid(row=7, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=7, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fish Sandwhich", fg="steel blue", anchor=W)
    lblinfo.grid(row=8, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=8, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chocolate Brownie", fg="steel blue", anchor=W)
    lblinfo.grid(row=9, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="steel blue", anchor=W)
    lblinfo.grid(row=9, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Icecream", fg="steel blue", anchor=W)
    lblinfo.grid(row=10, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="steel blue", anchor=W)
    lblinfo.grid(row=10, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Panini", fg="steel blue", anchor=W)
    lblinfo.grid(row=11, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=11, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chawarma", fg="steel blue", anchor=W)
    lblinfo.grid(row=12, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=12, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Tacos", fg="steel blue", anchor=W)
    lblinfo.grid(row=13, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="steel blue", anchor=W)
    lblinfo.grid(row=13, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Tea", fg="steel blue", anchor=W)
    lblinfo.grid(row=14, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="15", fg="steel blue", anchor=W)
    lblinfo.grid(row=14, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Coffee", fg="steel blue", anchor=W)
    lblinfo.grid(row=15, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="15", fg="steel blue", anchor=W)
    lblinfo.grid(row=15, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cola", fg="steel blue", anchor=W)
    lblinfo.grid(row=16, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="steel blue", anchor=W)
    lblinfo.grid(row=16, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Orange Juice", fg="steel blue", anchor=W)
    lblinfo.grid(row=17, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="steel blue", anchor=W)
    lblinfo.grid(row=17, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Mineral Water", fg="steel blue", anchor=W)
    lblinfo.grid(row=18, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="7", fg="steel blue", anchor=W)
    lblinfo.grid(row=18, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chocolate Shake", fg="steel blue", anchor=W)
    lblinfo.grid(row=19, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="15", fg="steel blue", anchor=W)
    lblinfo.grid(row=19, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Oreo Krusher", fg="steel blue", anchor=W)
    lblinfo.grid(row=20, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="15", fg="steel blue", anchor=W)
    lblinfo.grid(row=20, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Vanilla Shake", fg="steel blue", anchor=W)
    lblinfo.grid(row=21, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="15", fg="steel blue", anchor=W)
    lblinfo.grid(row=21, column=3)
    roo.mainloop()

# ===============================TOTAL FUNCTION===============================================
def TotalCost():
    m1 = float(varFries.get())
    m2 = float(vaMADalad.get())
    m3 = float(varHamburger.get())
    m4 = float(varLittiChokha.get())
    m5 = float(varChickenSalad.get())
    m6 = float(varCheeseSandwich.get())
    m7 = float(varChickenSandwich.get())
    m8 = float(varFishSandwich.get())
    m9 = float(varChocoBrownie.get())
    m10 = float(varIceCream.get())
    m11 = float(varPanini.get())
    m12 = float(varChawarma.get())
    m13 = float(varTacos.get())
    m14 = float(varTea.get())
    m15 = float(varCola.get())
    m16 = float(varCoffee.get())
    m17 = float(varOrange.get())
    m18 = float(varWater.get())
    m19 = float(varChocolateShake.get())
    m20 = float(varVanillaShake.get())
    m21 = float(varOreoKrusher.get())

    iTotal = (m1*10 + m2*25 + m3*25 + m4*15 + m5*25 + m6*30 + m7*30 + m8*30 + m9*10 + m10*10 + m11*30 + m12*30 + m13*30 + m14*10 + m15*15 + m16*15 +
                 m17*10 + m18*7 + m19*15 + m20*15 + m21*15)

    striTotal = 'MAD',str(iTotal)
    varTotal.set(striTotal)

    cgst = (9/100)*iTotal
    strcgst = 'MAD',str(cgst)
    varCGST.set(strcgst)

    sgst = (9/100)*iTotal
    stMADgst = 'MAD',str(sgst)
    vaMADGST.set(stMADgst)

    service_charge = 0.1*iTotal
    stMADervice_charge = "MAD",str(service_charge)
    vaMADerviceCharge.set(stMADervice_charge)

    strPay = 'MAD', str('%.2f'%(iTotal+cgst+sgst+service_charge))
    varPay.set(strPay)

#================================================================================
#                       CHECKBOX FUNCTION
# ================================================================================
def a():
    if var1.get() == 1:
        txtFries.configure(state=NORMAL)
        varFries.set("")
    elif var1.get() == 0:
        txtFries.configure(state=DISABLED)
        varFries.set("0")

def b():
    if var2.get() == 1:
        txtSalad.configure(state=NORMAL)
        vaMADalad.set("")
    elif var2.get() == 0:
        txtSalad.configure(state=DISABLED)
        vaMADalad.set("0")

def c():
    if var3.get() == 1:
        txtHamburger.configure(state=NORMAL)
        varHamburger.set("")
    elif var3.get() == 0:
        txtHamburger.configure(state=DISABLED)
        varHamburger.set("0")

def d():
    if var4.get() == 1:
        txtLittiChokha.configure(state=NORMAL)
        varLittiChokha.set("")
    elif var4.get() == 0:
        txtLittiChokha.configure(state=DISABLED)
        varLittiChokha.set("0")

def e():
    if var5.get() == 1:
        txtChickenSalad.configure(state=NORMAL)
        varChickenSalad.set("")
    elif var5.get() == 0:
        txtChickenSalad.configure(state=DISABLED)
        varChickenSalad.set("0")


def f():
    if var6.get() == 1:
        txtCheeseSandwich.configure(state=NORMAL)
        varCheeseSandwich.set("")
    elif var6.get() == 0:
        txtCheeseSandwich.configure(state=DISABLED)
        varCheeseSandwich.set("0")

def g():
    if var7.get() == 1:
        txtChickenSandwich.configure(state=NORMAL)
        varChickenSandwich.set("")
    elif var7.get() == 0:
        txtChickenSandwich.configure(state=DISABLED)
        varChickenSandwich.set("0")

def h():
    if var8.get() == 1:
        txtFishSandwich.configure(state=NORMAL)
        varFishSandwich.set("")
    elif var8.get() == 0:
        txtFishSandwich.configure(state=DISABLED)
        varFishSandwich.set("0")

def i():
    if var9.get() == 1:
        txtChocoBrownie.configure(state=NORMAL)
        varChocoBrownie.set("")
    elif var9.get() == 0:
        txtChocoBrownie.configure(state=DISABLED)
        varChocoBrownie.set("0")

def j():
    if var10.get() == 1:
        txtIceCream.configure(state=NORMAL)
        varIceCream.set("")
    elif var10.get() == 0:
        txtIceCream.configure(state=DISABLED)
        varIceCream.set("0")

def k():
    if var11.get() == 1:
        txtPanini.configure(state=NORMAL)
        varPanini.set("")
    elif var11.get() == 0:
        txtPanini.configure(state=DISABLED)
        varPanini.set("0")
        
def l():
    if var12.get() == 1:
        txtChawarma.configure(state=NORMAL)
        varChawarma.set("")
    elif var12.get() == 0:
        txtChawarma.configure(state=DISABLED)
        varChawarma.set("0")
        
def m():
    if var13.get() == 1:
        txtTacos.configure(state=NORMAL)
        varTacos.set("")
    elif var13.get() == 0:
        txtTacos.configure(state=DISABLED)
        varTacos.set("0")
        
def n():
    if var14.get() == 1:
        txtTea.configure(state=NORMAL)
        varTea.set("")
    elif var14.get() == 0:
        txtTea.configure(state=DISABLED)
        varTea.set("0")
        
def o():
    if var15.get() == 1:
        txtCola.configure(state=NORMAL)
        varCola.set("")
    elif var15.get() == 0:
        txtCola.configure(state=DISABLED)
        varCola.set("0")
        
def p():
    if var16.get() == 1:
        txtCoffee.configure(state=NORMAL)
        varCoffee.set("")
    elif var16.get() == 0:
        txtCoffee.configure(state=DISABLED)
        varCoffee.set("0")
        
def q():
    if var17.get() == 1:
        txtOrange.configure(state=NORMAL)
        varOrange.set("")
    elif var17.get() == 0:
        txtOrange.configure(state=DISABLED)
        varOrange.set("0")
        
def r():
    if var18.get() == 1:
        txtWater.configure(state=NORMAL)
        varWater.set("")
    elif var18.get() == 0:
        txtWater.configure(state=DISABLED)
        varWater.set("0")
        
def s():
    if var19.get() == 1:
        txtChocolateShake.configure(state=NORMAL)
        varChocolateShake.set("")
    elif var19.get() == 0:
        txtChocolateShake.configure(state=DISABLED)
        varChocolateShake.set("0")
        
def t():
    if var20.get() == 1:
        txtVanillaShake.configure(state=NORMAL)
        varVanillaShake.set("")
    elif var20.get() == 0:
        txtVanillaShake.configure(state=DISABLED)
        varVanillaShake.set("0")
        
def u():
    if var21.get() == 1:
        txtOreoKrusher.configure(state=NORMAL)
        varOreoKrusher.set("")
    elif var21.get() == 0:
        txtOreoKrusher.configure(state=DISABLED)
        varOreoKrusher.set("0")






#================================================================================
#                       FRAME 1
# ================================================================================



lblMeal = Label(f1top,font=("arial",25,'bold'), text="Fast Meal")
lblMeal.grid(row=0, column=0)

Fries = Checkbutton(f1top, text="Fries", variable=var1, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=a)
Fries.grid(row=1, column=0, sticky = W)
txtFries = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varFries, width=4, justify="right",state=DISABLED)
txtFries.grid(row=1, column=1)

Salad = Checkbutton(f1top, text="Salad", variable=var2, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=b)
Salad.grid(row=2, column=0, sticky = W)
txtSalad = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = vaMADalad, width=4, justify="right",state=DISABLED)
txtSalad.grid(row=2, column=1)

Hamburger = Checkbutton(f1top, text="Hamburger", variable=var3, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=c)
Hamburger.grid(row=3, column=0, sticky = W)
txtHamburger = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varHamburger, width=4, justify="right",state=DISABLED)
txtHamburger.grid(row=3, column=1)

LittiChokha = Checkbutton(f1top, text="Litti Chokha", variable=var4, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=d)
LittiChokha.grid(row=4, column=0, sticky = W)
txtLittiChokha = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varLittiChokha, width=4, justify="right",state=DISABLED)
txtLittiChokha.grid(row=4, column=1)

ChickenSalad = Checkbutton(f1top, text="Chicken Salad", variable=var5, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=e)
ChickenSalad.grid(row=5, column=0, sticky = W)
txtChickenSalad = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varChickenSalad, width=4, justify="right",state=DISABLED)
txtChickenSalad.grid(row=5, column=1)

lblSpace = Label(f1top,text="\n")
lblSpace.grid(row=6, column=0)
lblSandwich = Label(f1top,font=("arial",25,'bold'), text="Sandwiches")
lblSandwich.grid(row=7, column=0)

CheeseSandwich = Checkbutton(f1top, text="Cheese Sandwich", variable=var6, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=f)
CheeseSandwich.grid(row=8, column=0, sticky = W)
txtCheeseSandwich = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varCheeseSandwich, width=4, justify="right",state=DISABLED)
txtCheeseSandwich.grid(row=8, column=1)

ChickenSandwich = Checkbutton(f1top, text="Chicken Sandwich", variable=var7, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=g)
ChickenSandwich.grid(row=9, column=0, sticky = W)
txtChickenSandwich = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varChickenSandwich, width=4, justify="right",state=DISABLED)
txtChickenSandwich.grid(row=9, column=1)

FishSandwich = Checkbutton(f1top, text="Fish Sandwhich", variable=var8, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=h)
FishSandwich.grid(row=10, column=0, sticky = W)
txtFishSandwich = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varFishSandwich, width=4, justify="right",state=DISABLED)
txtFishSandwich.grid(row=10, column=1)

#lblSpace = Label(f1top,text="\n\n\n\n\n\n\n")
#lblSpace.grid(row=11, column=0)
btnReceipt=Button(f1bottom,padx=20,pady=2,bd=14,fg="black",font=('arial',16,'bold'),width=16,text="GENERATE RECEIPT", command = Receipt)
btnReceipt.grid(row=0,column=0)
#================================================================================
#                       FRAME 2 Top
# ================================================================================



lblMeal = Label(f2Top,font=("arial",25,'bold'), text="Desserts")
lblMeal.grid(row=0, column=0)

ChocoBrownie = Checkbutton(f2Top, text="Chocolate Brownie", variable=var9, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=i)
ChocoBrownie.grid(row=1, column=0, sticky = W)
txtChocoBrownie = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varChocoBrownie, width=4, justify="right",state=DISABLED)
txtChocoBrownie.grid(row=1, column=1)

IceCream = Checkbutton(f2Top, text="Icecream", variable=var10, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=j)
IceCream.grid(row=2, column=0, sticky = W)
txtIceCream = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varIceCream, width=4, justify="right",state=DISABLED)
txtIceCream.grid(row=2, column=1)

Panini = Checkbutton(f2Top, text="Panini", variable=var11, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=k)
Panini.grid(row=3, column=0, sticky = W)
txtPanini = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varPanini, width=4, justify="right",state=DISABLED)
txtPanini.grid(row=3, column=1)

Chawarma = Checkbutton(f2Top, text="Chawarma", variable=var12, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=l)
Chawarma.grid(row=4, column=0, sticky = W)
txtChawarma = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varChawarma, width=4, justify="right",state=DISABLED)
txtChawarma.grid(row=4, column=1)

Tacos = Checkbutton(f2Top, text="Tacos", variable=var13, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=m)
Tacos.grid(row=5, column=0, sticky = W)
txtTacos = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varTacos, width=4, justify="right",state=DISABLED)
txtTacos.grid(row=5, column=1)


#================================================================================
#                       FRAME 2 BOTTOM
# ================================================================================



lblPaymentMethod = Label(f2Bottom, font=("arial", 18, 'bold'), text = "Payment Method", bd=10, width=16, anchor='w')
lblPaymentMethod.grid(row=0,column=0)

cmbPaymentMethod = ttk.Combobox(f2Bottom, textvariable=varPM, state="readonly", font=("arial", 10, 'bold'), width=20)
cmbPaymentMethod['value']=('Cash','Master Card','Visa Card')
cmbPaymentMethod.current(0)
cmbPaymentMethod.grid(row=0, column=1)

lblTotal = Label(f2Bottom, font=("arial", 18, 'bold'), text = "Total", bd=10, width=16, anchor='e')
lblTotal.grid(row=2,column=1)
txtTotal = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varTotal, width=10, justify="right",state=DISABLED)
txtTotal.grid(row=2, column=2)

lblSGST = Label(f2Bottom, font=("arial", 18, 'bold'), text = "SGST @9%", bd=10, width=16, anchor='e')
lblSGST.grid(row=3,column=1)
txtSGST = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = vaMADGST, width=10, justify="right",state=DISABLED)
txtSGST.grid(row=3, column=2)

lblCGST = Label(f2Bottom, font=("arial", 18, 'bold'), text = "CGST @9%", bd=10, width=16, anchor='e')
lblCGST.grid(row=4,column=1)
txtCGST = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varCGST, width=10, justify="right",state=DISABLED)
txtCGST.grid(row=4, column=2)

lblServiceCharge = Label(f2Bottom, font=("arial", 18, 'bold'), text = "Service Charge @10%", bd=10, width=16, anchor='e')
lblServiceCharge.grid(row=5,column=1)
txtServiceCharge = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = vaMADerviceCharge, width=10, justify="right",state=DISABLED)
txtServiceCharge.grid(row=5, column=2)


#======================================================================================================================
#                                     BUTTONS
#======================================================================================================================
btnprice=Button(f2Bottom,padx=20,pady=1, bd=14 ,fg="black",font=('arial' ,16,'bold'),width=5, text="PRICE LIST", command = price_list)
btnprice.grid(row=2, column=0)

btnTotal = Button(f2Bottom, padx=20, pady=1, bd=14, fg="black", font=("arial", 16, 'bold'), width=5,
                  text="TOTAL", command = TotalCost).grid(row=3, column=0)

btnReset=Button(f2Bottom,padx=20,pady=1,bd=14,fg="black",font=('arial',16,'bold'),width=5,text="RESET", command=Reset)
btnReset.grid(row=4,column=0)

btnExit=Button(f2Bottom,padx=20,pady=1,bd=14,fg="black",font=('arial',16,'bold'),width=5,text="EXIT", command = iExit)
btnExit.grid(row=5,column=0)



#================================================================================
#                       FRAME 3
# ================================================================================

lblDrinks = Label(f3top,font=("arial",25,'bold'), text="Drinks")
lblDrinks.grid(row=0, column=0)

Tea = Checkbutton(f3top, text="Tea", variable=var14, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=n)
Tea.grid(row=1, column=0, sticky = W)
txtTea = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varTea, width=4, justify="right",state=DISABLED)
txtTea.grid(row=1, column=1)

Cola = Checkbutton(f3top, text="Cola", variable=var15, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=o)
Cola.grid(row=2, column=0, sticky = W)
txtCola = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varCola, width=4, justify="right",state=DISABLED)
txtCola.grid(row=2, column=1)

Coffee = Checkbutton(f3top, text="Coffee", variable=var16, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=p)
Coffee.grid(row=3, column=0, sticky = W)
txtCoffee = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varCoffee, width=4, justify="right",state=DISABLED)
txtCoffee.grid(row=3, column=1)

Orange = Checkbutton(f3top, text="Orange Juice", variable=var17, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=q)
Orange.grid(row=4, column=0, sticky = W)
txtOrange = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varOrange, width=4, justify="right",state=DISABLED)
txtOrange.grid(row=4, column=1)

Water = Checkbutton(f3top, text="Mineral Water", variable=var18, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=r)
Water.grid(row=5, column=0, sticky = W)
txtWater = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varWater, width=4, justify="right",state=DISABLED)
txtWater.grid(row=5, column=1)

lblSpace = Label(f3top,text="\n\n")
lblSpace.grid(row=6, column=0)

lblShakes = Label(f3top,font=("arial",25,'bold'), text="Shakes & Beverages")
lblShakes.grid(row=7, column=0)

ChocolateShake = Checkbutton(f3top, text="Chocolate Shake", variable=var19, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=s)
ChocolateShake.grid(row=8, column=0, sticky = W)
txtChocolateShake = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varChocolateShake, width=4, justify="right",state=DISABLED)
txtChocolateShake.grid(row=8, column=1)

VanillaShake = Checkbutton(f3top, text="Vanilla Shake", variable=var20, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=t)
VanillaShake.grid(row=9, column=0, sticky = W)
txtVanillaShake = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varVanillaShake, width=4, justify="right",state=DISABLED)
txtVanillaShake.grid(row=9, column=1)

OreoKrusher = Checkbutton(f3top, text="Oreo Krusher", variable=var21, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=u)
OreoKrusher.grid(row=10, column=0, sticky = W)
txtOreoKrusher = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varOreoKrusher, width=4, justify="right",state=DISABLED)
txtOreoKrusher.grid(row=10, column=1)

#lblSpace = Label(f3top,text="\n\n\n\n\n")
#lblSpace.grid(row=11, column=0)

lblpay = Label(f3bottom, font=("arial", 18, 'bold'), text = "Total Payable Amount", fg="red", bd=10, width=16, anchor='e')
lblpay.grid(row=0, column=0)
txtpay = Entry(f3bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varPay, width=10, justify="right",state=DISABLED)
txtpay.grid(row=0, column=1)

root.mainloop()
