from kanren import Relation, facts, run, var, conde

student = Relation()

likes = Relation()

facts(student, ("alice",), ("bob",))
facts(likes, ("alice", "math"), ("bob", "science"))

def is_intelligent(person):
    return conde((student(person), likes(person, var())))

x = var()

print("Queries:")
print("1. Who is intelligent?")
print("2. Is Alice intelligent?")
print("3. Is Bob Intelligent?")

choice = int(input("Enter the number of your choice (1-3): "))
if choice == 1:
    result = run(0, x, is_intelligent(x))
    print("Intelligent people:", result)
elif choice == 2:
    result = run(0, x, is_intelligent("alice"))
    if result:
        print("Alice is intelligent.")
    else:
        print("Alice is not intelligent.")
elif choice == 3:
    result = run(0, x, is_intelligent("bob"))
    if result:
        print("Bob is intelligent.")
    else:
        print("Bob is not intelligent.")
else:
    print("Invalid choice.")
