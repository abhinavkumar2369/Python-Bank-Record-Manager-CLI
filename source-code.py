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
