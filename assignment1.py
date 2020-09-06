altitude=int(input("Enter the altitude of the plane  "))
if(altitude<=1000):
    print("Land the plane")
elif(altitude>1000 and altitude<=5000):
    print("Bring it to 1000ft")
else:
    print("Go around and Try Later")
