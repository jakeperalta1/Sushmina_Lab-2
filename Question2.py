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
        
        print(f"{j+1}                 : {s}")
        s=p/100*s
        j+=1