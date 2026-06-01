import matplotlib.pyplot as plt

subjects = ['Math', 'Python', 'DBMS', 'OS', 'CN']

semester1 = [75, 80, 70, 65, 78]
semester2 = [82, 85, 76, 72, 88]

plt.figure(figsize=(8,5))

plt.plot(subjects, semester1,
         marker='o',
         linewidth=2,
         label='Semester 1')

plt.plot(subjects, semester2,
         marker='s',
         linewidth=2,
         label='Semester 2')

plt.title("Semester Result Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True)
plt.legend()

plt.show()