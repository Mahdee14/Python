print("Welcome to problem solver. Let's start. What is your name ?")
name = input()
print()

print("What exactly is your problem ?")
problem = input()
print()

print("What is the main cause to your problem ?")
problem_causes = input()
print()

print("Mention 3 possible solutions to your problem ?")
solution_1 = input()
solution_2 = input()
solution_3 = input()
print()

print("Select a solution (1, 2 or 3)")
solution = input()

if int(solution) == 1:
    solution = solution_1
elif int(solution) == 2:
    solution = solution_2
else:
    solution = solution_3

print(
    "\n" +
    name,
    "who has the problem",
    problem,
    "which was caused mainly due to",
    problem_causes,
    "has chosen to",
    solution,
    "to solve the problem\n\n"
)