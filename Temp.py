#first_list = [999, 333, 2, 8982, 12, 45, 77, 99, 11]
#second_list = []
#count = 0
#loop_time = len(first_list)
#while count < loop_time:
  #second_list.append(min(first_list))
  #first_list.remove(min(first_list))
  #count += 1
#print(second_list)
#print()




def order_lists_asc(temp_list):
  new_list = []
  count = 0
  loop_time = len(temp_list)
  while count < loop_time:
    new_list.append(min(temp_list))
    temp_list.remove(min(temp_list))
    count += 1
  print(new_list)

first_list = [999, 333, 2, 8982, 12, 45, 77, 99, 11]

order_lists_asc(first_list)  

print()

mylist = [999, 333, 2, 8982, 12, 45, 77, 99, 11]
print(mylist, 9)
for i in range(len(mylist)):
  print(mylist)
  for j in range(i+1,len(mylist)):
    print(i, j)
    if mylist[i] > mylist[j]:
      temp = mylist[i]
      mylist[i] = mylist[j]
      mylist[j] = temp
      print(mylist)
print(mylist)
print()
#
def my_function(a, b) :
    print(a * b)

my_function(10,20)
#
def my_function(a, b):
    hypotenuse = (a**2 + b**2)**0.5
    return hypotenuse
print(my_function(3,4))
print()

#
def longer(a, b):
    if len(a) >= len(b):
        return a
    else:
        return b

print(longer('Richard', 'John'))
print()

#

tersten = lambda texti : texti[::-1]
print(tersten("ters"))

iterable = [1,2,3,4,5]

nums1 = [9,6,7,4]
nums2 = [3,6,5,8]


aritmetic = map(lambda x, y : (x + y) / 2, nums1, nums2 )
print(list(aritmetic))
print()

#
words1 = ["you", "much", "hard"]
words2 = ["i", "you","he"]
words3 = ["love","ate", "works"]
sentence = map(lambda x, y, z : (y + " " + z + " " + x), words1, words2, words3)
print(list(sentence))

print(list(sentence))
for i in sentence:
  print(i)
print(list(sentence))
print()
#

words = ["apple","swim","clock","me","kiwi","mamtzta"]

count = filter(lambda x: len(x) < 5, words)
print(list(count))

def counter(x) :
  return len(x) < 5
words = ["apple","swim","clock","me","kiwi","mamtzta"]
for i in filter(counter, words):
  print(i)
print()

#Write a Python code to get lengths of a triangle from a user and then check them whether this triangle is equilateral, isosceles or scalene.

x = (int(input("Please enter the length of the first side of your triangle")))
y = (int(input("Please enter the length of the second side of your triangle")))
z = (int(input("Please enter the length of the third side of your triangle")))

if x == y == z :
  print("This is an equilateral triangle.")
if x == y or x == z or z == y :
  print("This is an isosceles triangle.")
else :
  print("This is an scalene triangle.")

#Write a Python code that counts how many vowels and constants a string has that a user entered.


