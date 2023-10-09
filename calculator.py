# start define the functions needed : add , sub , mul , div
#print option to the user
#ask for values  
#call the funnctions 
# while loop to continue the program 

# start add function 
def add(a,b):
    answer = a + b 
    print(str(a) + " + " + str(b) + " = " + str(answer) )
# finish add function 

# start sub function 
def sub(a,b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) )
# finish the sub function 

# start multy function
def multi(a,b):
    answer = a * b
    print(str(a) + " x " + str(b) + " = " + str(answer) )
# end of multi function 

# start div function
def div(a,b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) )
# end div function

print("A, Adition" )
print("B, Subtraction")
print("C, Multiplication")
print("D, Division")
print("E, Exit")
