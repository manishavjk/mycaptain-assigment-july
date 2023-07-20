a = input("Enter File name:")
b = a.split(".")
if (b[-1]=='txt'):
   print("the extension of this file is: text")
elif(b[-1]=='html'):
   print("the extension of this file is: html")
elif (b[-1]=='py'):
   print("the extension of this file is: python")
elif (b[-1]=='java'):
   print("the extension of this file is: java")
else: 
   print("invaild")         