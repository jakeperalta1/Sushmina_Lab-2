#initialized a list
myNumbers = [1,2,3,4,5,6,7,8,9,10]
a=[]

print("List of numbers:",myNumbers)

#using for loop to print list of numbers greater than 5
for n in myNumbers:
    if n> 5:
        #forming a list
        a.append(n)
print ("List of numbers that are larger than 5 :")      
       
print(a) 
        