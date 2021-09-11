# execption handling examples

try:
    print(2/0)

except ZeroDivisionError as message:            #division by zero 
    print("the description of exception:",message)