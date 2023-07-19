info=[]
info_no_qty=[]

import operations

def read_stock():
    '''
        reads the stocklist.txt file and store data in the info array

        Returns:
            void
    '''
    f = open("stocklist.txt", "r")
    data = f.readlines()
    
    for i in range(len(data)):
        info.append(data[i].strip().split(","))  # strip function removes the \n
        info_no_qty.append(data[i].strip().split(",")) #to create a list without quantity later
    f.close()
    
def read_show_stock():
    '''
        shows stock..
        can be used only after calling the read_stock() function first

        returns:
            void
    '''
    print("\n=========================== LAPTOPS IN STOCK========================")
    print("Sn |   MODEL    | BRAND | PRICE |  GRAPHICS |  PROCESSOR   |  QTY")
    print("-------------------------------------------------------------------")
    serial = 1 # initialising to provide a serial number 
    for i in range(len(info)):
        if int(info[i][3]) == 0: #if qty 0
            a=str(serial)+ " | "+ info[i][0]+" |  "+ info[i][1]+" |  "+info[i][2]+" |  "+ info[i][5]+" |  "+info[i][4]
            print(operations.strike(a)+"  N/A")
        else:
            print(serial, " |", info[i][0]+" | ", info[i][1]+" | ",
                info[i][2]+" | ", info[i][5]+" | ", info[i][4]+" | ",info[i][3])
            
        serial = serial+1
    print("====================================================================")
