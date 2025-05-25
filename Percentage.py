class Percentage:
    def percentage():
        mark1=int(input("Enter the mark1: "))
        mark2=int(input("Enter the mark2: "))
        mark3=int(input("Enter the mark3: "))
        mark4=int(input("Enter the mark4: "))
        mark5=int(input("Enter the mark5: "))
        print("Subject1= ",mark1)
        print("Subject2= ",mark2)
        print("Subject3= ",mark3)
        print("Subject4= ",mark4)
        print("Subject5= ",mark5)
        total=mark1+mark2+mark3+mark4+mark5;
        print("Total :",total)
        percentage=total/5
        print("Percentage: {:.14f}".format(percentage))