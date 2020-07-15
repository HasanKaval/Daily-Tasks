#Daily Task: Write a Python code that calculates the average of scores that students took in a math class at below.
scores = {
  "Mary" : 85,
  "Susan": 75,
  "Barry" : 65,
  "Alexis" : 88,
  "Jane" : 45,
  "Tina" : 100,
  "Tom" : 90,
  "Tim": 60
}
print("Math scores are as follows : ")
for i, j in scores.items():
  print(i," : ", j)
total = 0
for i in scores.values():
  total += i
avg_score = total / len(scores)
print("\nThe average score in Math is : ", avg_score)
#scores >= avg are high scores 
count_higher = 0
count_lower = 0
for i in scores.values():
  if i >= avg_score:
    count_higher += 1
  else:
    count_lower += 1
print("\nFrom a total of", len(scores), "students" , count_lower, "students are below average level and", \
count_higher, "students achieved to score higher than average. " )
