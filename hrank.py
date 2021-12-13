#hackerank problem solving
'''
Create a program that can determine whether 
a year is a leap year or not. And print to  
the user "this is a leap year" or "not a leap year"
'''

yr = input("enter a valid year: ")
if (yr % 4) ==0 or (yr % 400) ==0:
    print("this is a leap year")
else: 
    print("not a leap year")

if __name__ == "__main__":
    print("program finished")

 
        


