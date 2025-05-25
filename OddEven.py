class OddEven:
    def OddEven():
        num=int(input("Enter a number: "))
        if(num%2==0):
            message=f"{num} is Even Number"
        else:
            message=f"{num} is Odd Number"
        return message