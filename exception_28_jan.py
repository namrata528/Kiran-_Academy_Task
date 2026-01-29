# try:
#     print(4/0)
# except ZeroDivisionError as e: 
#     print("You can't divide by zero!") 
#     print(e)  

# try:
#     a="hello"+20
# except TypeError as e:
#     print(e)     

# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# try:
#     result=num1/num2
#     print("The result is:", result)
# except ZeroDivisionError as e:
#     print("You can't divide by zero!")
#     print(e)
    
# try:
#     num1=int(input("Enter first number: "))
#     num2=int(input("Enter second number: "))
#     result=num1/num2
#     print(result)
# # except Exception as e:
# #     print("error")
# #     print(e)    
# except (ValueError,ZeroDivisionError) as e:
#     print("error")
#     print(e)

# else:
#     print("Successfully Completed")  
  
  
# finally:
#     print("clean up activiy")  
# print("hello")    
     
# class humpadhainahikarteException(Exception):
#     def __init__(self, msg):
#         self.msg=msg
#         #super().__init__(msg) 
# marks=60
# if marks<70:
#     obj=humpadhainahikarteException("Nahi karenge") 
#     raise obj    

#homework 
# you are working on pune RTO project for liecence accept age from user and check if age is less than 18 then raise AgeTOOLowException,if age is above 75 then raise AgeTOOHighExceptio and if age is betwwen 18 to 75 display welcome to pune rto profile 

class AgeTooLowException(Exception) :
    def __init__(self, msg):
        super().__init__(msg)
        
class AgeTooHighException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        
try:        
    age=int(input())
    if age<18:
       obj=AgeTooLowException("Age too low")
       raise obj
    elif age>75:
       obj=AgeTooHighException("Age too High")
       raise obj
    else:
      print("Welcome To Pune RTO Profile")  
       
except AgeTooLowException as e:
    print(e)     
          
except AgeTooHighException as e:
    print(e)  

except ValueError as e:
    print("Invalid age ")
    print(e)

          