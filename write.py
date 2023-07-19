import operations
def write_sale_invoice(clientName,invoice_name1,receipt_dt,shipping_cost,total_amount):
    '''
        prints the sales invoice and saves it as a text file

        Args:
            clientName : string
            invoice_name1 : string
            receipt_dt : string
            shipping_cost : int
            total_amount : int

        Returns:
            void
    '''
    # opening a new invoice as a text  file
    newInvoice = open(invoice_name1, "w")
    print("\n===========================================")
    newInvoice.write("            AOT Laptop Shop"+"\n"+"              Durbargmarg\n\n"+"                           VAT: 55-01187233\n\n")
    print("            AOT Laptop Shop"+"\n"+"              Durbargmarg\n\n"+"                           VAT: 55-01187233\n")
    newInvoice.write("              Sales Invoice\n\n")
    print("              Sales Invoice\n")
    newInvoice.write("Date & time: "+receipt_dt+"\n")
    print("Date & time: "+receipt_dt)
    newInvoice.write("Client name: "+clientName+"\n\n")
    print("Client name: "+clientName+"\n")

    newInvoice.write("--------------------------------------------\n")
    print("--------------------------------------------")
    newInvoice.write("Sn     Particulars     Qty NetRate  NetAmt\n")
    print("Sn     Particulars     Qty NetRate  NetAmt")
    newInvoice.write("--  -----------------  --- -------  --------\n")
    print("--  -----------------  --- -------  --------")

    serial2=1 #to add serial  number in invoice
    for i in range(len(operations.invoice_list)):
        newInvoice.write(str(serial2)+"   ") #serial number
        print(str(serial2)+"   "+operations.invoice_list[i].upper()) #serial number
        newInvoice.write(operations.invoice_list[i].upper())
        newInvoice.write("\n")
        serial2=serial2+1
                    
    for i in range(len(operations.cart_list)):
        operations.update_stock_aftersales(operations.cart_list[i],int(operations.cart_qty[i]))


    newInvoice.write("--------------------------------------------\n\n")
    print("--------------------------------------------\n")
    newInvoice.write("Net total: " + "$" + str(total_amount)+"\n")
    print("Net total: " + "$" + str(total_amount))
                    
    newInvoice.write("Shipping cost: "+ "$" +str(shipping_cost)+"\n")
    print("Shipping cost: "+ "$" +str(shipping_cost))
    newInvoice.write("---------------------\n")
    print("---------------------")
    newInvoice.write("Grand total: "+ "$" +str(shipping_cost+total_amount)+"\n")
    print("Grand total: "+ "$" +str(shipping_cost+total_amount))
    newInvoice.write("---------------------\n\n")
    print("---------------------\n")
    newInvoice.write("	C O N D I T I O N S    A P P L Y\n\n1. Goods once sold will not be returned. \n2. Exchange within 7 days with receipt.\n\n      Thank you for shopping at AOT..")
    print("	C O N D I T I O N S    A P P L Y\n\n1. Goods once sold will not be returned. \n2. Exchange within 7 days with receipt.\n\n      Thank you for shopping at AOT..")


    newInvoice.close()

    print("\nThe invoice has been saved as", invoice_name1)

def write_purchase_invoice(sellerName,invoice_name1,receipt_dt,total_amount):
    '''
        prints the purchase invoice and saves it as a text file

        Args:
            sellerName : string
            invoice_name1 : string
            receipt_dt : string
            total_amount : int

        Returns:
            void
    '''
    # opening a new invoice as a text  file
    newInvoice = open(invoice_name1, "w")
    print("\n===========================================")
    newInvoice.write("            AOT Laptop Shop"+"\n"+"              Durbargmarg\n\n"+"                           VAT: 55-01187233\n\n")
    print("            AOT Laptop Shop"+"\n"+"              Durbargmarg\n\n"+"                           VAT: 55-01187233\n")
    newInvoice.write("              Purchase Invoice\n\n")
    print("              Purchase Invoice\n")
    newInvoice.write("Date & time: "+receipt_dt+"\n")
    print("Date & time: "+receipt_dt)
    newInvoice.write("Dealer name: "+sellerName+"\n\n")
    print("Dealer name: "+sellerName+"\n")

    newInvoice.write("--------------------------------------------\n")
    print("--------------------------------------------")
    newInvoice.write("Sn     Particulars     Qty NetRate  NetAmt\n")
    print("Sn     Particulars     Qty NetRate  NetAmt")
    newInvoice.write("--  -----------------  --- -------  --------\n")
    print("--  -----------------  --- -------  --------")

    serial2=1 #to add serial  number in invoice
    for i in range(len(operations.invoice_list)):
        newInvoice.write(str(serial2)+"   ") #serial number
        print(str(serial2)+"   "+operations.invoice_list[i].upper()) #serial number
        newInvoice.write(operations.invoice_list[i].upper())
        newInvoice.write("\n")
        serial2=serial2+1

  
                    
    for i in range(len(operations.cart_list)):
        operations.update_stock_afterpurchase(operations.cart_list[i],int(operations.cart_qty[i]))


    newInvoice.write("--------------------------------------------\n\n")
    print("--------------------------------------------\n")
    newInvoice.write("  Net total : " + "$" + str(total_amount)+"\n")
    print("  Net total : " + "$" + str(total_amount))
    newInvoice.write("    13% VAT : "+"$"+str((13/100)*total_amount)+"\n")                
    print("    13% VAT : "+"$"+str((13/100)*total_amount))                
    newInvoice.write("----------------------\n")
    print("----------------------")
    newInvoice.write("Grand total : "+"$"+str(((13/100)*total_amount)+total_amount)+"\n")
    print("Grand total : "+"$"+str(((13/100)*total_amount)+total_amount))
    newInvoice.write("----------------------\n")
    print("----------------------")

    print("\nThe invoice has been saved as", invoice_name1)

def order_invoice(iv_name,brand,model,price,qty,processor,graphics,distributor,dateTime):
    '''
        prints the purchase invoice of previously not exisiting laptop and saves it as a text file

        Args:
            iv_name : string
            brand : string
            model : string
            price : int
            qty : int
            processor: string
            graphics : string
            distributor : string
            dateTime : string

        Returns:
            void
    '''
    net_amt=int(price)*int(qty) #calulcations to add  in bill
    vat_amt=(13/100)*net_amt #calulcations to add  in bill
    total_amt=net_amt+vat_amt #calulcations to add  in bill
    invoice2 = open(iv_name,"w")

    invoice2.write("                VAT Invoice")
    print("                VAT Invoice")
    invoice2.write("\n\n                  	              VAT no.: 241-19992")
    print("\n                  	              VAT no.: 241-19992")
    invoice2.write("\n\nName of distributor: "+distributor.upper())
    print("\nName of distributor: "+distributor.upper())
    invoice2.write("\nDate & time: "+dateTime)
    print("Date & time: "+dateTime)
    invoice2.write("\nSold to: AOT Laptop Shop, Durbarmarg")
    print("Sold to: AOT Laptop Shop, Durbarmarg")
    invoice2.write("\n-------------------- LAPTOP DETAILS --------------------")
    print("-------------------- LAPTOP DETAILS --------------------")
    invoice2.write("\nBrand: "+brand.upper())
    print("Brand: "+brand.upper())
    invoice2.write("\nModel: "+model.upper())
    print("Model: "+model.upper())
    invoice2.write("\nProcessor: "+processor.upper())
    print("Processor: "+processor.upper())
    invoice2.write("\nGraphics: "+graphics.upper())
    print("Graphics: "+graphics.upper())
    invoice2.write("\n--------------------------------------------------------\n")
    print("--------------------------------------------------------\n")
    invoice2.write("\n  Price per unit: "+"$"+str(price))
    print("  Price per unit: "+"$"+str(price))
    invoice2.write("\n        Quantity: "+str(qty))
    print("        Quantity: "+str(qty))
    invoice2.write("\n               ----------------")
    print("                 ----------------")
    invoice2.write("\n      Net amount: "+"$"+str(net_amt))
    print("      Net amount: "+"$"+str(net_amt))
    invoice2.write("\n         13% Vat: "+"$"+str(vat_amt))
    print("         13% Vat: "+"$"+str(vat_amt))
    invoice2.write("\n               ----------------")
    print("                 ----------------")
    invoice2.write("\n    Total amount: "+"$"+str(total_amt))
    print("    Total amount: "+"$"+str(total_amt))
    invoice2.close()

    print("\nThe invoice has been saved as",iv_name)