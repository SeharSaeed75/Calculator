import time
print("welcome",
      "you may enter ypur numbers")
num1= input("ENTER NUM1:")
op= input("enter the operator:")
num2=input("ENTER NUM2:")

if(op== '-'):
 print("YOUR RESULT IS:",num1 - num2)
elif(op== '+'):
 print("YOUR RESULT IS:",num1+num2)
elif(op== '/'):
 print("YOUR RESULT IS:",float(num1/num2))
elif(op== '*'):
 print("YOUR RESULT IS:",num1*num2)
elif(op== '^'):
 print("YOUR RESULT IS:",num1^num2)
else:
 print("syntax error")

print("THANK YOU FOR USING")
time.sleep(5)