from read import info
import operations
import datetime
import read
import write


date = datetime.datetime.now()
#date and time variables for invoice creation
filename_dt = str(date.year)+  "-"+str(date.month)+"-"+str(date.day)+"_"+str(date.hour)+str(date.minute)+str(date.second)
receipt_dt = str(date.year)+"-"+str(date.month)+"-"+str(date.day)+" "+str(date.hour)+":"+str(date.minute)+":"+str(date.second)

portalLoop=True # main loop inside which the program runs
while  portalLoop==True:
    operations.welcome_display()
    portalAns=input("Select an option: ").lower()
    if portalAns=="1":
        purchase_loop=True
        while purchase_loop==True:
            read.read_stock()
            read.read_show_stock() 
            add_to_cart_loop = True
            while add_to_cart_loop  == True:
                input_loop1=True 
                while input_loop1==True: #loop to keep adding product
                    try: #exception handling
                        serial_ans=int(input("\nEnter the serial of product you would like to add to your cart: "))-1
                    except ValueError:
                        # if entered value is a negative or non integer value
                        print("Invalid input!")
                        input_loop1=True
                    else:
                        if serial_ans>len(info)-1 or serial_ans<0:
                            #if the input is out of bounds
                            print("Invalid command!")
                        else:
                            input_loop2=True
                            while input_loop2==True:
                                try:
                                    qty_req=int(input("\nHow many would you like to buy? : "))
                                except ValueError:
                                    # if entered value is a negative or non integer value
                                    print("\nInvalid input")
                                    input_loop2=True
                                else:
                                    #serial_ans=serial_ans-1
                                    if qty_req<=0:
                                        # qty input less than 0
                                        print("\nSorry, invalid input!")
                                    elif int(info[serial_ans][3])>=qty_req and qty_req>0:
                                        #if stock is available
                                        operations.cart_list.append(info[serial_ans][0])
                                        operations.cart_qty.append(qty_req)
                                        cont_loop=True
                                        while cont_loop==True:
                                            cont = input("\nDo you wish to add another? (Y/N) : ").lower()
                                            if cont == "y":
                                                add_to_cart_loop  = True
                                                read.read_show_stock() # show the laptops 
                                                break
                                            elif cont == "n" and len(operations.cart_list)==0:
                                                    print("\nCan't move forward with an empty cart !!\n")
                                                    add_to_cart_loop  = True       
                                            elif cont == "n":
                                                add_to_cart_loop  = False
                                                break
                                            else:
                                                print("\nWrong command ! ")
                                                cont_loop=True
                                        input_loop2=False
                                    else:
                                        # if req qty is not available
                                        print("\nNot enough in stock! Only "+str(info[serial_ans][3])+" left.")
                                    
                                input_loop1=False
            operations.add_to_cart() # cart list added to the invoice list
            shipping_loop=True
            shipping_cost=0 # declared and initialised
            while shipping_loop==True:
                ship = input("\nAdd shipping facilty? Would cost an extra $45(Y/N) : ")
                ship=ship.lower()
                if ship == "y":
                    shipping_cost=45 # if shipping allowed
                    break
                elif ship=="n":
                    shipping_cost=0 # shipping not allowed
                    break
                else:
                    print("\nInvalid command! Try again")
                    shipping_loop=True
            total_amount = 0 #declared and intialised
            for each in operations.bill_total:
                total_amount = total_amount+each
            total_amount = float(total_amount)
            print("\nYour total is $"+str(shipping_cost+total_amount)+"\n") # print out total in the console
            str_empty_loop1=True
            while str_empty_loop1==True: # loop to enter valid name
                clientName=input("\nEnter the client name: ").upper()
                if clientName=="":
                    print("\nEmpty field  found! Try again.")
                else:
                    break
            checkout_loop=True
            while checkout_loop==True: # loop to confirm  check out
                checkout_answer=input("\nDo you want to check out?(Y/N)")
                checkout_asnwer=checkout_answer.lower()
                if checkout_answer == "y":
                    invoice_name1="SALE-"+clientName+"-"+filename_dt+".txt"
                    write.write_sale_invoice(clientName,invoice_name1,receipt_dt,shipping_cost,total_amount)
                    checkout_loop=False
                elif checkout_answer=="n":
                    checkout_loop=False
                    print("\nYour cart has been cleared! ")
                else:
                    print("\n Ooops, Invalid command! Try again!")
                    checkout_loop=True

            read.info=[] #to avoid multiple appending
            operations.bill_total=[] #to avoid multiple appending
            operations.cart_list=[] #to avoid multiple appending
            operations.cart_qty=[] #to avoid multiple appending
            operations.invoice_list=[] #to avoid multiple appending
            print("\nPress Y to continue selling or N to navigate to main menu : ")
            cont_loop=True
            while cont_loop==True: # loop to ask if continue
                cont_ans=input().lower()
                if cont_ans=="y":
                    add_to_cart_loop=True
                    break
                elif cont_ans=="n":
                    add_to_cart_loop=False
                    purchase_loop=False
                    print("\nExiting to main menu ... \n")
                    break
                else:
                    print("Invalid command!")  
    elif portalAns=="2": # purchase loop starts
        purchase2_loop=True
        while purchase2_loop==True:
            read.read_stock()
            read.read_show_stock() # display laptops
            try: #eception handling
                print("\nEnter 1 | To buy a previously existing laptop")
                print("Enter 2 | To buy a previously not existing laptop")
                purchase_main_ans = int(input("Enter option : "))
            except ValueError:
                print("\nInvalid command")
                read.info=[]
                read.info_no_qty=[]
            else:
                if purchase_main_ans==1: # existing laptop purchase
                    add_to_cart_loop = True
                    while add_to_cart_loop  == True:
                        input_loop1=True
                        while input_loop1==True:
                            try:
                                serial_ans=int(input("\nEnter the serial of product you would like to purchase and add stock: "))-1
                            except ValueError:
                                print("Invalid input.")
                                input_loop1=True
                            else:
                                if serial_ans>len(info)-1 or serial_ans<0:
                                    print("Invalid command!")
                                else:
                                    input_loop2=True
                                    while input_loop2==True:
                                        try:
                                            qty_req=int(input("\nHow many would you like to buy? : "))
                                        except ValueError:
                                            print("\nInvalid input")
                                            input_loop2=True
                                        else:
                                            
                                            if qty_req>0:
                                                operations.cart_list.append(info[serial_ans][0])
                                                operations.cart_qty.append(qty_req)
                                                cont_loop=True
                                                while cont_loop==True:
                                                    cont = input("\nDo you wish to add another? (Y/N) : ").lower()
                                                    if cont == "y":
                                                        add_to_cart_loop  = True
                                                        read.read_show_stock() # display laptop
                                                        break
                                                    elif cont == "n" and len(operations.cart_list)==0:
                                                            print("\nCan't move forward with an empty cart !!\n")
                                                            add_to_cart_loop  = True       
                                                    elif cont == "n":
                                                        add_to_cart_loop  = False
                                                        break
                                                    else:
                                                        print("\nWrong command ! ")
                                                        cont_loop=True
                                                input_loop2=False
                                            else:
                                                print("\nInvalid command!")
                                            
                                        input_loop1=False
                    operations.add_to_cart() # add to invoice list
                    total_amount=0
                    for each in operations.bill_total:
                        total_amount = total_amount+each
                    total_amount = float(total_amount)
                    str_empty_loop1=True
                    while str_empty_loop1==True: # client name input loop
                        sellerName=input("\nEnter the name of the dealer: ").upper()
                        if sellerName=="":
                            print("\nEmpty field  found! Try again.")
                        else:
                            break
                    checkout_loop=True
                    while checkout_loop==True: # loop to confirm checkout
                        checkout_answer=input("\nDo you want to check out?(Y/N)")
                        checkout_asnwer=checkout_answer.lower()
                        if checkout_answer == "y":
                            invoice_name1="PURCHASE-"+sellerName+"-"+filename_dt+".txt"
                            write.write_purchase_invoice(sellerName,invoice_name1,receipt_dt,total_amount)
                            checkout_loop=False
                        elif checkout_answer=="n":
                            checkout_loop=False
                            print("\nYour cart has been cleared! ")
                        else:
                            print("\n Ooops, Invalid command! Try again!")
                            checkout_loop=True
                    read.info=[] # to avoid multiple appending
                    operations.bill_total=[] # to avoid multiple appending
                    operations.cart_list=[] # to avoid multiple appending
                    operations.cart_qty=[] # to avoid multiple appending
                    operations.invoice_list=[] # to avoid multiple appending
                    read.info=[] # reseting the list to prevent multiple appending
                    read.info_no_qty=[]# reseting the list to prevent multiple appending
                    print("\nPress Y to continue purchasing or N to navigate to main menu : ")
                    cont3_loop=True
                    while cont3_loop==True: # go to menu or continue
                        cont3_ans=input().lower()
                        if cont3_ans=="y":
                            add_to_cart_loop=True
                            break
                        elif cont3_ans=="n":
                            add_to_cart_loop=False
                            purchase2_loop=False
                            print("\nExiting to main menu ... \n")
                            break
                        else:
                            print("Invalid command!")   
                elif purchase_main_ans==2: # not existing laptop purchase
                    print("\n------------------------------------------------------------")
                    print("Enter Laptop details:")
                    print("------------------------------------------------------------\n")
                    details_input_loop1=True
                    while details_input_loop1==True:
                        brand_input=input("Enter the brand name: ")
                        model_input=input("Enter the model name: ")
                        if  brand_input=="" or model_input=="":
                            print("\nEmpty fields found! Enter again.")
                            details_input_loop1=True
                        else:
                            details_input_loop1=False
                    price_input_loop=True
                    while price_input_loop==True:    
                        try: #  exception handling
                            price_input=int(input("Enter the price per unit of the laptop ($): "))
                        except ValueError:
                            print("Invalid input! Enter number only.")
                            print("Note: Do not include $ sign!")
                            price_input_loop=True
                        else:
                            if price_input>0:
                                price_input_loop=False
                                pass
                            else:
                                print("\nInvalid command.")
                                price_input_loop=True
                    qty_input_loop=True
                    while qty_input_loop==True:
                        try: #  exception handling
                            qty_input=int(input("Enter the quantity: "))
                        except ValueError:
                            print("Invalid input! Enter number only.")
                            qty_input_loop=True
                        else:
                            if qty_input>0:
                                qty_input_loop=False
                                pass
                            else:
                                qty_input_loop=True
                                print("\nInvalid qty. Try again!")
                    details_loop=True
                    while details_loop==True:    
                        processor_input=input("Enter the processor specification: ")
                        graphics_input=input("Enter the graphics card specification: ")
                        distributer_input=input("Enter the name of distributor(Company): ")

                        if processor_input=="" or graphics_input=="" or distributer_input=="":
                            details_loop=True
                            print("\nEmpty fields found! Enter again!")
                        else:
                            invoice_name2="ORDER-"+model_input+"-"+filename_dt+".txt"

                            operations.update_new_afterPurchase(brand_input,model_input,price_input,qty_input,processor_input,graphics_input)
                            write.order_invoice(invoice_name2,brand_input,model_input,price_input,qty_input,processor_input,graphics_input,distributer_input,receipt_dt)
                            details_loop=False

                        read.info=[] # reseting the list to prevent multiple appending
                        read.info_no_qty=[]# reseting the list to prevent multiple appending
                    print("\nPress Y to continue purchasing or N to navigate to main menu : ")
                    cont2_loop=True
                    while cont2_loop==True: # go to menu or continue purchasing
                        cont3_ans=input().lower()
                        if cont3_ans=="y":
                            add_to_cart_loop=True
                            break
                        elif cont3_ans=="n":
                            add_to_cart_loop=False
                            purchase2_loop=False
                            print("\nExiting to main menu ... \n")
                            break
                        else:
                            print("Invalid command!")  
                else:
                    print("\nInvalid command!")
                    read.info=[] # to prevent multiple appending
                    read.info_no_qty=[] # to prevent multiple appending
                
    elif portalAns=="3": # exit the portal
        print("\nExiting portal!\n")
        portalLoop=False
    else:
        print("\n Invalid command! ")