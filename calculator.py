import time
print("welcome",
      "you may enter your numbers")
num1=float(input("ENTER NUM1:"))
op= input("enter the operator:")
num2=float(input("ENTER NUM2:"))
if(op== '-'):
 print("YOUR RESULT IS:",(num1-num2))
elif(op== '+'):
 print("YOUR RESULT IS:",(num1 +num2))
elif(op== '/'):
 print("YOUR RESULT IS:"(num1/num2))
elif(op== '*'):
 print("YOUR RESULT IS:",(num1*num2))
elif(op== '^'):
 print("YOUR RESULT IS:",(num1^num2))
else:
 print("syntax error")
 
print("THANK YOU FOR USING")
time.sleep(5)
