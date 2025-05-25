class MultipleFunctions():
    def eligibilityForMarriage(gender,age):
        if(gender=="Male"):
            if(age>20):
                message="ELIGIBLE"
            else:
                message="NOT ELIGIBLE"
        if(gender=="Female"):
            if(age>17):
                message="ELIGIBLE"
            else:
                message="NOT ELIGIBLE"
        return message
    def OddEven():
        num=int(input("Enter a number: "))
        if(num%2==0):
            message=f"{num} is Even Number"
        else:
            message=f"{num} is Odd Number"
        return message
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
    def subFields():
        print("Sub-fields in AI are:")
        subAIFieldList=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for field in subAIFieldList:
            print(field)
    def triangle():
        height = int(input("Enter Height: "))
        breadth = int(input("Enter Breadth: "))
        print("Height: ", height)
        print("Breadth: ", breadth)
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ", (height*breadth)/2)
        height1 = int(input("Enter Height1: "))
        height2 = int(input("Enter Height2: "))
        breadth2 = int(input("Enter Breadth: "))
        print("Perimeter Formula: Height1 + Height2 + Breadth")
        print("Perimeter of Triangle: ", height1 + height2 + breadth2)
    