from tkinter import *
from tkinter import ttk
from PIL import Image ,ImageTk
import random,os
from tkinter import messagebox
import tempfile
import mysql.connector as mc
from time import strftime
import datetime as dt

class Bill():
    def __init__(self,root):
        self.root=root
        self.root.geometry('1313x615+0+0')
        self.root.title('Billing Software')
        # Variables======================================================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        self.e_name=StringVar()
        self.e_number=StringVar()
        self.e_email=StringVar()
        self.e_bill_no=StringVar()
        self.time=StringVar()
        #PRODUCT CATAGORY LIST======================================================
        self.catagory=["select one","Veg","Non-Veg","Dessert","Juice"]
        # sub category of veg
        self.subcat_veg=["Tiffin","Veg-briyani"]
        # price of veg [ tiffin]
        self.tiffin=["Dosa","Idly","Poori","Pongal"]
        self.price_dosa=50
        self.price_idly=40
        self.price_poori=70
        self.price_pongal=60
        # price of  veg [ veg briyani]
        self.vegbriyani=["Meals","Tomota-rice","Curd-rice"]
        self.price_meals=130
        self.price_tomota=80
        self.price_curd=60
        #sub category of non veg
        self.subcat_nonveg=["Chicken","Mutton"]
        # price non veg [ chicken]
        self.chicken=["Grill-full","Grill-half","Briyani"]
        self.price_grillfull=380
        self.price_grillhalf=190
        self.price_briyani=220
        # price of non veg [ mutton]
        self.mutton=["Mutton Briyani","Mutton-thokku"]
        self.mut_briyani=280
        self.mut_thokku=320
        #sub category of dessert
        self.subcat_dessert=["Cakes","Biscuits","Candies"]
        # price of cake
        self.cakes=["Vennila","chocko","Straberry"]
        self.price_vennila=500
        self.price_chocko=700
        self.price_straberry=900
        # price of cake
        self.biscuits=["Good-day","Marigold","Hide on sick"]
        self.price_goodday=20
        self.price_marigold=20
        self.price_hideonsick=30
        # price of candies
        self.candies=["Jelly Belly","Diary-Milk","Kit Kat","Milky Bar"]
        self.price_jellybelly=10
        self.price_diarymilk=20
        self.price_kitkat=20
        self.price_milkybar=20
        # subcategory of juice
        self.subcat_juice=["Fruits","Ice-cream"]
        # price on fruits
        self.fruits=["Apple","Orange","Banana"]
        self.price_apple=120
        self.price_orange=90
        self.price_banana=50
        # price on ice creams
        self.Icecream=["Cone","Butterscatch","Kulfi"]
        self.price_cone=50
        self.price_butterscatch=70
        self.price_kulfi=40
        
        
        
        # TITLE===========================================================================
        
        lbl_tittle=Label(self.root,text='GARDEN OF EAT’N ',font=('times new roman',35,'bold'),bg='#212F3C',fg='#F1C40F')
        lbl_tittle.place(x=0,y=0,width=1350,height=45)
        def time():
            string=strftime('%H:%M:%S:%p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(lbl_tittle,font=('times new roman',16,'bold'),bg='#212F3C', fg='red')
        lbl.place(x=0,y=0,width=120,height=45)
        time()
        
        
        # MAIN FRAME===================================================================
        Main_Frame=Frame(self.root,bd=5,relief=SUNKEN,bg="#34495E")
        Main_Frame.place(x=0,y=50,width=1350,height=615)
        
        # M.CUSTOMER FRAME==============================================================
        cust_Frame=LabelFrame(Main_Frame,text="Customer",font=('times new roman',15,'bold'),bg='white',fg='red')
        cust_Frame.place(x=10,y=5,width=400,height=140)
        # C. MOBILE NO==============================================================
        self.lbl_mbl=Label(cust_Frame,text='Mobile No',font=('times new roman',12,'bold'),bg='white',fg='black')
        self.lbl_mbl.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mbl=ttk.Entry(cust_Frame,textvariable=self.c_phone,font=('times new roman',12,'bold'),width=24)
        self.entry_mbl.grid(row=0,column=1)
        # C. CUSTOMER===================================================================
        self.lblcustname=Label(cust_Frame,text='Name',font=('times new roman',12,'bold'),bg='white',fg='black')
        self.lblcustname.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txtcustname=ttk.Entry(cust_Frame,textvariable=self.c_name,font=('times new roman',12,'bold'),width=24)
        self.txtcustname.grid(row=1,column=1)
        # C.EMAIL========================================================================
        self.lblemail=Label(cust_Frame,text='Email',font=('times new roman',12,'bold'),bg='white',fg='black')
        self.lblemail.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.txtemail=ttk.Entry(cust_Frame,textvariable=self.c_email,font=('times new roman',12,'bold'),width=24)
        self.txtemail.grid(row=2,column=1)
        
        # M. PRODUCT FRAME===============================================================
        product_Frame=LabelFrame(Main_Frame,text="Product",font=('times new roman',15,'bold'),bg='white',fg='red')
        product_Frame.place(x=10,y=170,width=400,height=200)
        
        # P.CATEGORY=====================================================================
        self.lblcategory=Label(product_Frame,text='Select Category',font=('times new roman',12,'bold'),bg='white',fg='black',bd=4)
        self.lblcategory.grid(row=3,column=0,stick=W,padx=5,pady=2)

        self.combo_category=ttk.Combobox(product_Frame,value=self.catagory,font=('arial',10,'bold'),width=24,state='readonly')
        self.combo_category.current(0)
        self.combo_category.grid(row=3,column=1,stick=W,padx=5,pady=2)
        self.combo_category.bind("<<ComboboxSelected>>",self.catagories)
        #P. SUBCATEGORY======================================================================
        self.lblsubcategory=Label(product_Frame,text='SubCategory',font=('times new roman',12,'bold'),bg='white',fg='black',bd=4)
        self.lblsubcategory.grid(row=4,column=0,stick=W,padx=5,pady=2)

        self.combo_subcategory=ttk.Combobox(product_Frame,value=[""],font=('arial',10,'bold'),width=24,state='readonly')
        self.combo_subcategory.grid(row=4,column=1,stick=W,padx=5,pady=2)
        self.combo_subcategory.bind("<<ComboboxSelected>>",self.product_add)
        
        
        # P.PRODUCT NAME===================================================================
        self.lblproduct=Label(product_Frame,text='Product Items',font=('times new roman',12,'bold'),bg='white',fg='black',bd=4)
        self.lblproduct.grid(row=5,column=0,stick=W,padx=5,pady=2)

        self.combo_product=ttk.Combobox(product_Frame,textvariable=self.product,font=('arial',10,'bold'),width=24,state='readonly')
        self.combo_product.grid(row=5,column=1,stick=W,padx=5,pady=2)
        self.combo_product.bind("<<ComboboxSelected>>",self.price)
        
        # P. PRICE===========================================================================
        self.lblprice=Label(product_Frame,text='Price',font=('times new roman',12,'bold'),bg='white',fg='black',bd=4)
        self.lblprice.grid(row=6,column=0,stick=W,padx=5,pady=2)

        self.combo_price=ttk.Combobox(product_Frame,textvariable=self.prices,font=('arial',10,'bold'),width=24,state='readonly')
        self.combo_price.grid(row=6,column=1,stick=W,padx=5,pady=2)
        

        # P.QTY================================================================
        self.lblqty=Label(product_Frame,text='Quantity',font=('times new roman',12,'bold'),bg='white',fg='black',bd=4)
        self.lblqty.grid(row=7,column=0,stick=W,padx=5,pady=2)

        self.lblqty=ttk.Entry(product_Frame,textvariable=self.qty,font=('arial',10,'bold'),width=26)
        self.lblqty.grid(row=7,column=1,stick=W,padx=5,pady=2)
        
        # M.BILL AREA================================================================= 
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",relief=SUNKEN,font=('times new roman',15,'bold'),bg='white',fg='red')
        RightLabelFrame.place(x=450,y=5,width=500,height=370)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg='white',fg='blue',font=('times new roman',12,'bold'))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        # M. BILL COUNTER FRAME=========================================================
        Bottom_Frame=LabelFrame(Main_Frame,text='Bill Counter',font=('times new roman',15,'bold'),bg='white',fg='red')
        Bottom_Frame.place(x=0,y=400,width=950,height=170)
        # B. SUBTOTAL
        self.lblsubtotal=Label(Bottom_Frame,text='SubTotal',font=('times new roman',12,'bold'),bg='white',fg='black',bd=4)
        self.lblsubtotal.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.txtsubtotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=('arial',10,'bold'),width=26)
        self.txtsubtotal.grid(row=0,column=1,stick=W,padx=5,pady=2)
        # B.TAX
        self.lbltax=Label(Bottom_Frame,text='Tax',font=('times new roman',12,'bold'),bg='white',fg='black',bd=4)
        self.lbltax.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=('arial',10,'bold'),width=26)
        self.txt_tax.grid(row=1,column=1,stick=W,padx=5,pady=2)
        # B.Total 
        self.lbltotal=Label(Bottom_Frame,text='GrandTotal',font=('times new roman',12,'bold'),bg='white',fg='black',bd=4)
        self.lbltotal.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.txt_total=ttk.Entry(Bottom_Frame,textvariable=self.total,font=('arial',10,'bold'),width=26)
        self.txt_total.grid(row=2,column=1,stick=W,padx=5,pady=2)

        # SEARCH BOX
        Search_Frame=Frame(Main_Frame,relief=SUNKEN,bd=2,bg='white')
        Search_Frame.place(x=1000,y=5,width=330,height=70)

        self.lblbill=Label(Search_Frame,text='Bill No',font=('times new roman',17,'bold'),bg='white',fg='red',bd=4)
        self.lblbill.grid(row=290,column=3,stick=W,padx=5,pady=2)

        self.txt_bill=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=('arial',12,'bold'),width=15)
        self.txt_bill.grid(row=290,column=6,stick=W,padx=5,pady=2)

        self.btnsearch=Button(Search_Frame,text='Search',command=self.find_bill,font=('times new roman',12,'bold'),bg='#D4AC0D',fg='black',relief=RAISED,bd=3)
        self.btnsearch.grid(row=290,column=50,padx=5,pady=3)
        
        # M. RIGHT SIDE PICTURE======================================================================
        img=Image.open("nans1.jpeg")
        img=img.resize((380,615),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=1000,y=150,width=320,height=500)
        
        # BUTTON FRAME==============================================================
      
        self.btnaddtocart=Button(Bottom_Frame,text='Add to Item',command=self.AddItem,font=('times new roman',15,'bold'),bg='#D4AC0D',fg='black',relief=RAISED,bd=4)
        self.btnaddtocart.grid(row=1,column=150,padx=10,pady=5)

        self.btngenerate=Button(Bottom_Frame,text='Generate Bill',command=self.gen_bill,font=('times new roman',15,'bold'),bg='#D4AC0D',fg='black',relief=RAISED,bd=4)
        self.btngenerate.grid(row=1,column=300,padx=10,pady=5)

        self.btnsave=Button(Bottom_Frame,text='Save Bill',command=self.save_bill,font=('times new roman',15,'bold'),bg='#D4AC0D',fg='black',relief=RAISED,bd=4)
        self.btnsave.grid(row=1,column=450,padx=10,pady=5)

        self.btnprint=Button(Bottom_Frame,text='Print',command=self.iprint,font=('times new roman',15,'bold'),bg='#D4AC0D',fg='black',relief=RAISED,bd=4)
        self.btnprint.grid(row=1,column=600,padx=10,pady=5)

        self.btnclear=Button(Bottom_Frame,text='Clear',command=self.clear,font=('times new roman',15,'bold'),bg='#D4AC0D',fg='black',relief=RAISED,bd=4)
        self.btnclear.grid(row=1,column=750,padx=10,pady=5)

        self.btnexit=Button(Bottom_Frame,text='Exit',command=self.root.destroy,font=('times new roman',15,'bold'),bg='#D4AC0D',fg='black',relief=RAISED,bd=4)
        self.btnexit.grid(row=1,column=900,padx=10,pady=10)
        self.welcome()
        self.l=[]
#========================FUNCTION DECLRATION==============================================
            
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.time=dt.datetime.now()
        self.textarea.insert(END,f"{self.time:%X}\t Welcome to GARDEN OF EAT'N Hotel")
        self.textarea.insert(END,f"\nBill no:{self.bill_no.get()}")
        self.textarea.insert(END,f"\nCustomer name:{self.c_name.get()}")
        self.textarea.insert(END,f"\nCustomer Mobile no:{self.c_phone.get()}")
        self.textarea.insert(END,f"\nCustomer Email:{self.c_email.get()}")
        self.textarea.insert(END,"\n====================================================")
        self.textarea.insert(END,"\nProducts\t\tQty\t\tPrice")
        self.textarea.insert(END,"\n====================================================")    

    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=='':
            messagebox.showerror("Error","Please Select the Product")
        else:
            self.textarea.insert(END,f"\n{self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-
                                                            (self.prices.get()))*Tax)/100)))))
        

    def gen_bill(self):
        if self.product.get()=="":
             messagebox.showerror("Error","Please Add to cart the Product")
        else:
            text=self.textarea.get(9.0,END)
            self.time=dt.datetime.now().strftime('%X')
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n===================================================")
            self.textarea.insert(END,f"\nSub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\nTax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\nTotal Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n===================================================")
            
    
            self.e_name =self.c_name.get()
            self.e_number=self.c_phone.get()
            self.e_email =self.c_email.get()
            self.e_bill_no=self.bill_no.get()
            conn = mc.connect(host="localhost",user="root", password="",database="hotel")
            cur = conn.cursor()
            cur.execute("insert into client(cust_name,mbl_no,email,bill_no) values('"+self.e_name+"', '"+self.e_number+"', '"+self.e_email+"', '"+self.e_bill_no+"')")
            conn.close() 



    def save_bill(self):
        op=messagebox.askyesno("Save","Do you want to save the Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bill/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op1=messagebox.showinfo("Saved",f"Bill no:{self.bill_no.get()} Saved Successfully")
            f1.close()
            
    def iprint(self):
        q=self.textarea.get(1.0,'end-1c')
        filename=tempfile.mktemp(".txt")
        open(filename,'w').write(q)
        os.startfile(filename,'Print')
        
    def find_bill(self):
        found='no'
        for i in os.listdir('bill/'):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bill/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found='yes'
        if found=='no':
                messagebox.showerror('Error',"Invalid Bill No:")
            

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(x)
        self.c_email.set("")
        self.search_bill.set("")
        self.product.set("")
        self.prices.set("")
        self.qty.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.l=[]
        self.welcome()

    def exit(self):
       op=messagebox.askyesno('Exit','Do you really want to exit')
       if op>0:
           root.destroy    
        
    def catagories(self,event=''):
        if self.combo_category.get()=="Veg":
            self.combo_subcategory.config(value=self.subcat_veg)
            self.combo_subcategory.current(0)
    
        if self.combo_category.get()=="Non-Veg":
            self.combo_subcategory.config(value=self.subcat_nonveg)
            self.combo_subcategory.current(0)
            
        if self.combo_category.get()=="Dessert":
            self.combo_subcategory.config(value=self.subcat_dessert)
            self.combo_subcategory.current(0)     

        if self.combo_category.get()=="Juice":
            self.combo_subcategory.config(value=self.subcat_juice)
            self.combo_subcategory.current(0)
            
    def product_add(self,event=''):
        # veg food
        if self.combo_subcategory.get()=="Tiffin":
            self.combo_product.config(value=self.tiffin)
            self.combo_product.current(0)
            
        if self.combo_subcategory.get()=="Veg-briyani":
            self.combo_product.config(value=self.vegbriyani)
            self.combo_product.current(0)    
       # non-veg food
        if self.combo_subcategory.get()=="Chicken":
            self.combo_product.config(value=self.chicken)
            self.combo_product.current(0)
            
        if self.combo_subcategory.get()=="Mutton":
            self.combo_product.config(value=self.mutton)
            self.combo_product.current(0)
              
     # dessert food
        if self.combo_subcategory.get()=="Cakes":
            self.combo_product.config(value=self.cakes)
            self.combo_product.current(0)
            
        if self.combo_subcategory.get()=="Biscuits":
            self.combo_product.config(value=self.biscuits)
            self.combo_product.current(0)
            
        if self.combo_subcategory.get()=="Candies":
            self.combo_product.config(value=self.candies)
            self.combo_product.current(0) 
    # juice food
        if self.combo_subcategory.get()=="Fruits":
            self.combo_product.config(value=self.fruits)
            self.combo_product.current(0)
            
        if self.combo_subcategory.get()=="Ice-cream":
            self.combo_product.config(value=self.Icecream)
            self.combo_product.current(0)

    def price(self,event=''):
        # tiffin
       if self.combo_product.get()=="Dosa":
           self.combo_price.config(value=self.price_dosa)
           self.combo_price.current(0)
           self.qty.set(1)
       if self.combo_product.get()=="Idly":
           self.combo_price.config(value=self.price_idly)
           self.combo_price.current(0)
           self.qty.set(1)
       if self.combo_product.get()=="Poori":
           self.combo_price.config(value=self.price_poori)
           self.combo_price.current(0)
           self.qty.set(1)
           # veg briyanis
       if self.combo_product.get()=="Meals":
           self.combo_price.config(value=self.price_meals)
           self.combo_price.current(0)
           self.qty.set(1)
       if self.combo_product.get()=="Tomota-rice":
           self.combo_price.config(value=self.price_tomota)
           self.combo_price.current(0)
           self.qty.set(1)
       if self.combo_product.get()=="Curd-rice":
           self.combo_price.config(value=self.price_curd)
           self.combo_price.current(0)
           self.qty.set(1)
           # chicken
       if self.combo_product.get()=="Grill-full":
           self.combo_price.config(value=self.price_grillfull)
           self.combo_price.current(0)
           self.qty.set(1)
       if self.combo_product.get()=="Grill-half":
           self.combo_price.config(value=self.price_grillhalf)
           self.combo_price.current(0)
           self.qty.set(1)
       if self.combo_product.get()=="Briyani":
           self.combo_price.config(value=self.price_briyani)
           self.combo_price.current(0)
           self.qty.set(1)
                # mutton
       if self.combo_product.get()=="Mutton Briyani":
           self.combo_price.config(value=self.mut_briyani)
           self.combo_price.current(0)
           self.qty.set(1)
       if self.combo_product.get()=="Mutton-thokku":
           self.combo_price.config(value=self.mut_thokku)
           self.combo_price.current(0)
           self.qty.set(1)
            # cakes
       if self.combo_product.get()=="Vennila":
           self.combo_price.config(value=self.price_vennila)
           self.combo_price.current(0)
           self.qty.set(1)
       if self.combo_product.get()=="chocko":
           self.combo_price.config(value=self.price_chocko)
           self.combo_price.current(0)
           self.qty.set(1)
       if self.combo_product.get()=="Straberry":
           self.combo_price.config(value=self.price_straberry)
           self.combo_price.current(0)
           self.qty.set(1)
               # biscuits
       if self.combo_product.get()=="Good-day":
           self.combo_price.config(value=self.price_goodday)
           self.combo_price.current(0)
           self.qty.set(1)
       if self.combo_product.get()=="Marigold":
           self.combo_price.config(value=self.price_marigold)
           self.combo_price.current(0)
           self.qty.set(1)
       if self.combo_product.get()=="Hide on sick":
           self.combo_price.config(value=self.price_hideonsick)
           self.combo_price.current(0)
           self.qty.set(1)
               # candies
       if self.combo_product.get()=="Jelly Belly":
           self.combo_price.config(value=self.price_jellybelly)
           self.combo_price.current(0)
           self.qty.set(1)
       if self.combo_product.get()=="Diary-Milk":
           self.combo_price.config(value=self.price_diarymilk)
           self.combo_price.current(0)
           self.qty.set(1)
       if self.combo_product.get()=="Kit Kat":
           self.combo_price.config(value=self.price_kitkat)
           self.combo_price.current(0)
           self.qty.set(1)
       if self.combo_product.get()=="Milky Bar":
           self.combo_price.config(value=self.price_milkybar)
           self.combo_price.current(0)
           self.qty.set(1)              
                # fruits
       if self.combo_product.get()=="Apple":
           self.combo_price.config(value=self.price_apple)
           self.combo_price.current(0)
           self.qty.set(1)
       if self.combo_product.get()=="Orange":
           self.combo_price.config(value=self.price_orange)
           self.combo_price.current(0)
           self.qty.set(1)
       if self.combo_product.get()=="Banana":
           self.combo_price.config(value=self.price_banana)
           self.combo_price.current(0)
           self.qty.set(1)
        # ice creams
       if self.combo_product.get()=="Cone":
           self.combo_price.config(value=self.price_cone)
           self.combo_price.current(0)
           self.qty.set(1)
       if self.combo_product.get()=="Butterscatch":
           self.combo_price.config(value=self.price_butterscatch)
           self.combo_price.current(0)
           self.qty.set(1)
       if self.combo_product.get()=="Kulfi":
           self.combo_price.config(value=self.price_kulfi)
           self.combo_price.current(0)
           self.qty.set(1)
           
      
if __name__ =='__main__':
    root=Tk()
    obj=Bill(root)
    root.mainloop()
        
        
