def mytictactoe(val): 
    print("\n") 
    print("\t     |     |") 
    print("\t  {}  |  {}  |  {}".format(val[0], val[1], val[2])) 
    print('\t_____|_____|_____') 
  
    print("\t     |     |") 
    print("\t  {}  |  {}  |  {}".format(val[3], val[4], val[5])) 
    print('\t_____|_____|_____') 
  
    print("\t     |     |") 
  
    print("\t  {}  |  {}  |  {}".format(val[6], val[7], val[8])) 
    print("\t     |     |") 
    print("\n") 

def check_win ():
    result = [[1,2,3], [4,5,6,], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [[1,5,9], [3,5,7]]]


