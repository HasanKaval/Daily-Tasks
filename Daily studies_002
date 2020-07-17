#Write a Python code to sort the list below without using .sort() method.
#elements of list = [999, 333, 2, 8982, 12, 45, 77, 99, 11]
#Expected output: [2, 11, 12, 45, 77, 99, 333, 999, 8982]

first_list = [999, 333, 2, 8982, 12, 45, 77, 99, 11]
second_list = []
count = 0
loop_time = len(first_list)
while count < loop_time:
  second_list.append(min(first_list))
  first_list.remove(min(first_list))
  count += 1
print(second_list)
print()

# this function also works

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

