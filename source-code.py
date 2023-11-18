#------------------------------------------#
#          BANK  RECORD  MANAGER           #
#------------------------------------------#
#              SOURCE  CODE                #
#------------------------------------------#



#  [-- READING --]  FUNCTION

def read():
    import pickle
    file = open('User Database.dat','rb') 
    try:
        while True: 
            d = pickle.load(file) 
            print(d) 
    except: 
            file.close()



#  [-- WRITING --]  FUNCTION

def write(): 
    import pickle 
    file = open('User Database.dat','wb') 
    data = {} 
    n = int(input("How many User data you want to enter ? ")) 
    for a in range(n): 
        data['Employee No.'] = int(input("Enter Employee Number : ")) 
        data['Name'] = input("Enter Employee Name : ") 
        data['Department'] = input("Enter Department : ") 
        data['Salary'] = int(input("Salary : ")) 
        pickle.dump(data,file)
        print("-"*5)
    file.close() 
