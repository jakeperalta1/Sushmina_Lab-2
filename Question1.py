x= int(input("Enter number of years: "))
l= 0
#printing the number of year entered
num= print("For year", x, ":")
j= 0
k=0
total=0
while(j<12):
    k= int(input(f"Enter the rainfall amount for {j+1}:"))
    #using formula to calculate total
    t= total+k
    #converting cm to inches
    total= t/2.54
    j+=1
print("For 12 months")
print("Total rainfall:",total,"")
#using total calculated to calculate average
average = total/12
print("Average monthly rainfall:",average )
#keeping it in loop
l=l+1