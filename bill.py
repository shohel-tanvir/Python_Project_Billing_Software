import bdb
from cProfile import label
from cgitb import text
from sqlite3 import Row
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.tix import COLUMN
from turtle import right, title
import math,random
import os
class bill_app:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1275x740+0+0")
        self.root.title("Billing Software")
        bg_color="#3dcc57"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #=====variable==========
        #======customer variable======
        
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.search_bill=StringVar()
        #=========cosmetics variable==========
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
        #=========Grocery variable==========
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.suger=IntVar()
        self.tea=IntVar()
        #=========Cold drinks variable==========
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()
        #==========Total product price & Tax variable=========
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        self.total_cosmetic_price=StringVar()
        self.total_grocery_price=StringVar()
        self.total_cold_drink_price=StringVar()

        #===Customer frame======
        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=15,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=15,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        cbil_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=15,pady=5)
        cbil_txt=Entry(F1,width=15,textvariable=self.bill_no,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

        bil_btn=Button(F1,text="Search",width=10,command=self.find_bill,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10)
        #==Cosmatics frame
        F2=LabelFrame(self.root,text="Cosmetics",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=170,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        face_w_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hair_spray_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_spray_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hair_gell_lbl=Label(F2,text="Hair Gell",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_gell_txt=Entry(F2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_loshan_lbl=Label(F2,text="Body Loshan",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_loshan_txt=Entry(F2,width=10,textvariable=self.loshan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #==Grocery frame
        F3=LabelFrame(self.root,text="Grocery",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=335,y=170,width=325,height=380)

        g1_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_cream_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl=Label(F3,text="Suger",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.suger,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        


        #==Cold Drinks============
        F4=LabelFrame(self.root,text="Cold Drinks",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=665,y=170,width=325,height=380)

        c1_lbl=Label(F4,text="Maza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_lbl=Label(F4,text="Cock",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.cock,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lbl=Label(F4,text="Thumbs Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_lbl=Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        #====Bill Area====
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=995,y=170,width=300,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #===Bill menu====
        F6=LabelFrame(self.root,text="Bill Menu",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=170)

        m1_lbl=Label(F6,text="Total Cosmetic Price",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Grocery Price",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Cold Drinks Price",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
        #===tax lebel==
        c1_lbl=Label(F6,text="Cosmetic Tax",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=2,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text="Grocery Tax",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=1,column=2,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text="Cold Drinks Tax",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=2,column=2,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
        #==Button frame====
        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=720,y=5,width=520,height=120)

        totla_btn=Button(btn_F,text="Total",command=self.total,bg="cadetblue",fg="white",bd=5,pady=17,width=8,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=12)
        gbil_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=5,pady=17,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=12)
        clear_btn=Button(btn_F,text="New Bill",command=self.clear_data,bg="cadetblue",fg="white",bd=5,pady=17,width=8,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=12)
        exit_btn=Button(btn_F,text="Exit",command=self.exit,bg="cadetblue",fg="white",bd=5,pady=17,width=7,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=12)
        self.welcome_bill()

    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*110
        self.c_sp_p=self.spray.get()*40
        self.c_ge_p=self.gell.get()*50
        self.c_lo_p=self.loshan.get()*60

        self.total_cosmetic_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_sp_p+
                                    self.c_ge_p+
                                    self.c_lo_p
                                )
        self.cosmetic_price.set("Tk "+str(self.total_cosmetic_price))
        self.c_tax=self.total_cosmetic_price*0.05
        self.cosmetic_tax.set("Tk "+str(round((self.c_tax),2)))

        self.g_r_p=self.rice.get()*40
        self.g_f_p=self.food_oil.get()*120
        self.g_d_p=self.daal.get()*110
        self.g_w_p=self.wheat.get()*40
        self.g_s_p=self.suger.get()*50
        self.g_t_p=self.tea.get()*60

        self.total_grocery_price=float(
                                     self.g_r_p+
                                     self.g_f_p+
                                     self.g_d_p+
                                     self.g_w_p+
                                     self.g_s_p+
                                     self.g_t_p
                                )
        self.grocery_price.set("Tk "+str(self.total_grocery_price))
        self.g_tax=self.total_grocery_price*0.1
        self.grocery_tax.set("Tk "+str(round((self.g_tax),2)))
        
        self.c_m_p=self.maza.get()*40
        self.c_c_p=self.cock.get()*120
        self.c_f_p=self.frooti.get()*110
        self.c_t_p=self.thumbsup.get()*40
        self.c_l_p=self.limca.get()*50
        self.c_sp_p=self.sprite.get()*60

        self.total_cold_drink_price=float(
                                    self.c_m_p+
                                    self.c_c_p+
                                    self.c_f_p+
                                    self.c_t_p+
                                    self.c_l_p+
                                    self.c_sp_p
                                )
        self.cold_drink_price.set("Tk "+str(self.total_cold_drink_price))
        self.d_tax=self.total_cold_drink_price*0.1
        self.cold_drink_tax.set("Tk "+str(round((self.d_tax),2)))

        self.total_bill=float(self.total_cosmetic_price+
                        self.total_grocery_price+
                        self.total_cold_drink_price+
                        self.c_tax+
                        self.g_tax+
                        self.d_tax
                        )

    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tWelcome to Dream Shop")
        self.textarea.insert(END,f"\nBill Number :{self.bill_no.get()}")
        self.textarea.insert(END,f"\nCustomer Name :{self.c_name.get()}")
        self.textarea.insert(END,f"\nCustomer Phone No :{self.c_phone.get()}")
        self.textarea.insert(END,"\n================================")
        self.textarea.insert(END,"\nProducts\t\tQty\tPrice")
        self.textarea.insert(END,"\n================================")


    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmetic_price.get()=="Tk 0.0" and self.grocery_price.get()=="Tk 0.0" and self.cold_drink_price.get()=="Tk 0.0":
            messagebox.showerror("Error","No products are purched!")
        else:
            self.welcome_bill()
            #========Cosmetics bill==========
            if self.soap.get()!=0:
                self.textarea.insert(END,f"\nSoap\t\t{self.soap.get()}\t{self.c_s_p}")
            if self.face_cream.get()!="" or "0":
                self.textarea.insert(END,f"\nFace Cream\t\t{self.face_cream.get()}\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.textarea.insert(END,f"\nFace Wash\t\t{self.face_wash.get()}\t{self.c_fw_p}")
            if self.spray.get()!=0:
                self.textarea.insert(END,f"\nSpray\t\t{self.spray.get()}\t{self.c_sp_p}")
            if self.gell.get()!=0:
                self.textarea.insert(END,f"\nGell\t\t{self.gell.get()}\t{self.c_ge_p}")
            if self.loshan.get()!=0:
                self.textarea.insert(END,f"\nLoshan\t\t{self.loshan.get()}\t{self.c_lo_p}")
            #===========grocery bill==========
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\nRice\t\t{self.rice.get()}\t{self.g_r_p}")
            if self.food_oil.get()!=0:
                self.textarea.insert(END,f"\nFood Oil\t\t{self.food_oil.get()}\t{self.g_f_p}")
            if self.daal.get()!=0:
                self.textarea.insert(END,f"\nDaal\t\t{self.daal.get()}\t{self.g_d_p}")
            if self.wheat.get()!=0:
                self.textarea.insert(END,f"\nWheat\t\t{self.wheat.get()}\t{self.g_w_p}")
            if self.suger.get()!=0:
                self.textarea.insert(END,f"\nSuger\t\t{self.suger.get()}\t{self.g_s_p}")
            if self.tea.get()!=0:
                self.textarea.insert(END,f"\nTea\t\t{self.tea.get()}\t{self.g_t_p}")
            #=======cold drinks bill=========
            if self.maza.get()!=0:
                self.textarea.insert(END,f"\nMaza\t\t{self.maza.get()}\t{self.c_m_p}")        
            if self.cock.get()!=0:
                self.textarea.insert(END,f"\nCock\t\t{self.cock.get()}\t{self.c_c_p}")    
            if self.frooti.get()!=0:
                self.textarea.insert(END,f"\nFrooti\t\t{self.frooti.get()}\t{self.c_f_p}")
            if self.thumbsup.get()!=0:
                self.textarea.insert(END,f"\nThumbsup\t\t{self.thumbsup.get()}\t{self.c_t_p}")
            if self.limca.get()!=0:
                self.textarea.insert(END,f"\nLimca\t\t{self.limca.get()}\t{self.c_l_p}")
            if self.sprite.get()!=0:
                self.textarea.insert(END,f"\nSprite\t\t{self.sprite.get()}\t{self.c_sp_p}")
            
            self.textarea.insert(END,"\n--------------------------------")
            if self.cosmetic_tax.get()!="Tk 0.0":
                self.textarea.insert(END,f"\nCosmetics Tax\t\t\t{self.cosmetic_tax.get()}")
            
            if self.grocery_tax.get()!="Tk 0.0":
                self.textarea.insert(END,f"\nGrocery Tax\t\t\t{self.grocery_tax.get()}")
            
            if self.cold_drink_tax.get()!="Tk 0.0":
                self.textarea.insert(END,f"\nCold Drinks Tax\t\t\t{self.cold_drink_tax.get()}")
            self.textarea.insert(END,"\n--------------------------------")
            self.textarea.insert(END,f"\nTotal Bill\t\t\tTk {self.total_bill}")
            self.save_bill()
        #=======save bill===============    
    def save_bill(self):
        self.bill_data=self.textarea.get('1.0',END)
        f1=open("d:/Python Project/bills/"+str(self.bill_no.get())+".txt","w")
        f1.write(self.bill_data)
        f1.close()
    
    #======search bill===============
    def find_bill(self):
        present="no"
        for i in os.listdir("d:/Python Project/bills/"):
            if i.split('.')[0]==self.bill_no.get():
                f1=open(f"d:/Python Project/bills/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid bill no.!")
    
    def clear_data(self):
        self.c_name.set("")
        self.c_phone.set("")
        #=========cosmetics variable==========
        self.soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.spray.set(0)
        self.gell.set(0)
        self.loshan.set(0)
        #=========Grocery variable==========
        self.rice.set(0)
        self.food_oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.suger.set(0)
        self.tea.set(0)
        #=========Cold drinks variable==========
        self.maza.set(0)
        self.cock.set(0)
        self.frooti.set(0)
        self.thumbsup.set(0)
        self.limca.set(0)
        self.sprite.set(0)
        #==========Total product price & Tax variable=========
        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.cold_drink_price.set("")

        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.cold_drink_tax.set("")
        self.welcome_bill()

    def exit(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()

root=Tk()
obj=bill_app(root)
root.mainloop()
