n = int(input())

students = (input().split(" "))
students_p = (input().split(" "))

partners = dict()

for a, b in zip(students, students_p):
    partners[a] = b

good = True

for k, v in partners.items():
    if k == v:
        good = False
        break
    elif partners[v] != k:
        good = False
        break

# if good:
#     print("good")
# else:
#     print("bad")

print("good" if good else "bad")