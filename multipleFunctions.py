class multipleFunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        a = ['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        for items in a:
            print(items)
        
    def OddEven():
        num = int(input("Enter a number:"))
        if((num%2)==1):
            print(num,"is Odd Number")
        else:
            print(num,"is Even Number")   

    def Eligible():
        Gender = str(input("Your Gender:"))
        Age = int(input("Your age:"))
        if (Gender =="Male" and Age>=21):
            print("ELIGIBLE")
        elif(Gender =="Female" and Age>=18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage():
        a = int(input("Subject1 = "))
        b = int(input("Subject2 = "))
        c = int(input("Subject3 = "))
        d = int(input("Subject4 = "))
        e = int(input("Subject5 = "))
        Total = a+b+c+d+e
        print("Total = ",Total)
        Percentage = (Total / 500)*100
        print("Percentage = ",Percentage)

    def triangle():
        height = int(input("Height:"))
        breadth = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        print(f"Area of Triangle: {height*breadth/2}")
        height1 = int(input("Height1:"))
        height2 = int(input("Height2:"))
        breadth1 = int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print(f"Perimeter of Triangle:{height1+height2+breadth1}")