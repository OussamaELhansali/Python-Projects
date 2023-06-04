from art import logo
#  Add function 
def add(n1, n2):
  return n1+n2

#Substract function 
def substract(n1,n2):
  return n1-n2

#Multiply function 
def multiply(n1,n2):
  return n1*n2

#Division function 
def divide(n1,n2):
  return n1/n2


def calculator():
  print(logo)
  operations = {"+": add, "-": substract, "*": multiply, "/": divide}
  
  num1 = float(input("What's you first number ? "))
  new_number = True 
  while new_number:
      num2 = float(input("What's you new number ? "))
      for i in operations : 
        print(i)
      op = str(input("Chose the symbol of an operation from the line above "))
      result= operations[op](num1,num2)
      print(f"{num1} {op} {num2} = {result}")
      num1= result
      still_calculating = input(f"Type 'y' if you want to continue calculating with {result}, 'n' to exit ")
      if still_calculating == 'n':
        new_number = False
        print("Calculator closed ")
      else:
        pass

calculator()
