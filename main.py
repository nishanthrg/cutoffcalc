from flask import Flask

app = Flask(__name__)


@app.route('/')
def cutoff():
   print("CUT OF CALCULATOR")

print("Cutt off calculator @nikku ")
x = int(input("Enter your maths mark:"))
y = int(input("enter your physics mark:"))
z = int(input("enter your chemistry mark:"))
average = (y+z)/2+x
print("your cut off is :" )
print(average)

