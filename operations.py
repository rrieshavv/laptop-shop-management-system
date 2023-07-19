#list declared
bill_total=[]
cart_list=[]
cart_qty=[]
invoice_list=[]


from read import info,info_no_qty


def no_qty_stock():
    '''
        simply info list but without quantity
        use case: called for purchasing non existing laptops

        returns:
            void
    '''
    for i in range(len(info_no_qty)):
        del info_no_qty[i][3] #deletes the quantity 

def update_stock_aftersales(model,qty):
    '''
        this function simply updates the quantity of item present in the stocklist according to the passed parameters that are model and qty.
        *** only after the sale by shop is carried out i.e it performs teh subtraction part only

        Args:
            model : string
            qty : int
        
        Returns:
            void
    '''
    for i in range(len(info)):
        if model in info[i]:
            if int(info[i][3])>=qty: #check if there's enough stock
                info[i][3]=str(int(info[i][3])-qty)
                save_stock_inFormat() 
                break
            else:
                print("Not enough in stock at the moment !!!")
                break

def update_stock_afterpurchase(model,qty):
    '''
        this function simply updates the quantity of item present in the stocklist according to the passed parameters that are model and qty.
        *** only after the purchase by shop is carried out i.e it performs the addition part only

        Args:
            model : string
            qty : int

        Returns:
            void
    '''
    for i in range(len(info)):
        if model in info[i]:
            info[i][3]=str(int(info[i][3])+qty)
            save_stock_inFormat()
            break
            
def save_stock_inFormat():
    '''
        opens the stock file in write mode and saves the new data in exactly the same format as before 

        Returns:
            void
    '''
    f=open("stocklist.txt","w")
    for i in range(len(info)):
        for j in range(len(info[0])):
            if j == len(info[0])-1:  # check if this is the last element in the row
                f.write(info[i][j])  # print the element without a comma
                f.write("\n") # and adds a line space
            else:
                f.write(info[i][j])  # print the element with a comma
                f.write(",")
    f.close()    

def amount_calc(a, b, qty):
    '''
        separates $ from amount, calculates amount and appends to a list

        Args:
            a : int
            b : int
            qty : int

        Returns:
            void
    '''
    amount = info[a][b]
    amount_no_dollar = ""
    for i in range(1, len(amount)):
        amount_no_dollar = amount_no_dollar+amount[i] #without dollar sign
    bill_total.append(float(amount_no_dollar)*qty)

def strike(text):
    '''
        create a strikethrough on a text

        Args:
            text (string)
        Returns:
            string: representing a strikethrough text
    '''
    i = 0
    new_text = ''
    while i < len(text):
        new_text = new_text + (text[i] + u'\u0336') # it is a code to add strike
        i = i + 1
    return(new_text)

def add_to_cart():
    '''
        adds the selected product to the invoice list

        Returns:
            void
    '''
    for i in range(len(cart_list)):
        a= str(cart_qty[i])
        for j in range(len(info)):
            if cart_list[i]==info[j][0]:
                amount_calc(j,2,int(a)) # calculates amount and adss to list 
                invoice_list.append(" "+info[j][1]+" "+info[j][0]+"    "+a+"  "+info[j][2]+"     "+"$"+str(bill_total[i]))

def update_new_afterPurchase(brand,model,price,qty,processor,graphics):
    '''
        This function either adds the quantity of the purchased item if it is already present in the stock or adds a new item to the stock if  it's a new product

        Args:
            brand : string
            model : string
            price : int
            qty : int
            processor : string
            graphics : string

        Returns:
            void

    '''
    laptop_detail=[model.lower(),brand.lower(),"$"+str(price),processor.upper(),graphics.upper()]
    final_detail=[model.lower(),brand.lower(),"$"+str(price),str(qty),processor.upper(),graphics.upper()]
    no_qty_stock()
    if laptop_detail in info_no_qty:
        for i in range(len(info_no_qty)):
            if laptop_detail[0]== info_no_qty[i][0]:
                info[i][3]=str(int(info[i][3])+int(qty)) # just adds up qty
    else:
        info.append(final_detail) # adds new laptop
    save_stock_inFormat()
    print("\nThe laptop has been purchased and added to the stock!")

def welcome_display():
    '''
        welcome message

        returns:
            void
    '''
    print("---------------------------------------------------------------")
    print()
    print("                      AOT Laptop Shop ")
    print("                        Durbargmarg \n")

    print("Hello, World! Welcome to the shop portal! \n")

    print("Press 1 | Perform a sales")
    print("Press 2 | Perform a purchase")
    print("Press 3 | Exit the portal \n")