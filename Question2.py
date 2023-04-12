#taking inputs
s= int(input("Starting number of organisms:"))
p= int(input("Average daily percentage increase:"))
m = int(input("Enter the number of days to display the final data:"))

if s<0:
    print("error")
elif p<0:
    print("error")
elif m<0:
    print("error")
else:
     j=0
     print("Day Approximate     Population")
     while(j<m):
        #printing putput simultaneously
        print(f"{j+1}                 : {s}")
        #using formula to print population according to inputs
        s=(s+(p/100)*s)
        #keeping it in loop
        j+=1