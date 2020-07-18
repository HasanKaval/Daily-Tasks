# use of zip
x = []
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
for i in zip(a,b):
  x.append(i)
print("\n", x)

for j in range(len(x)):
  print("\n", x[(j)])

print()

#positional arguements
a = "i"
b = "love"
c = "you"

def texter(x, y, z):
  print(y, z, x)

texter(x = c, y = a, z = b,)
print()
texter(c, a, b)

print()

# *args question -> picking the even and odd numbers out of a given list and printing them as evens and odds. (2 differnet ways)

#first solution
def slicer(*numbers):
  even = []
  odd = []
  for i in numbers:
    if i % 2 == 0:
      even.append(i)
    else:
      odd.append(i)
  print("even list : ", even, "\nodd list : ", odd)

#second solution
def slicer1(*numbers):
  even = [i for i in numbers if i % 2 == 0]
  odd = [j for j in numbers if j %2 != 0]
  print("even list : ", even, "\nodd list : ", odd)

slicer(1, 2, 3, 4, 5, 6, 7, 8, 9)

print()

slicer1(1, 2, 3, 4, 5, 6, 7, 8, 9)

print()

# use of **kwargs
def organizer(**kwargs) :
  names =[]
  ages = []
  for i in kwargs.keys():
    names.append(i)
  for j in kwargs.values():
    ages.append(j)
  print("Names : ", names,"\n")
  print("Ages : ", ages)
   
organizer(Beth = 26, Oscar = 42, Justin = 18, Frank = 33)

print()

# use of lambda function

text = "Clarusway"
m = (lambda x : x[::-1])(text)
print(m)

print()

# use of lambda function + ternary operator

list_1 = [1, 2, 3, 4]
for x in list_1:
  print(x, ":", (lambda a : "even" if a % 2 ==0 else "odd")(x))
