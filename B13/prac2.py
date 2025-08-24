from collections import deque

def count_studennts_unable_to_eat(sandwiches, students):
    students = deque(students)
    sandwiches = deque(sandwiches)
    
    count = 0
    while students and sandwiches:
        if students[0] == sandwiches[0]:
            students.popleft()
            sandwiches.popleft()
            count = 0
        else:
            std = students.popleft()
            students.append(std)
            count+=1
            if count == len(students):
                break
    
    return len(students)

print(
    count_studennts_unable_to_eat(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1])
)
print(
    count_studennts_unable_to_eat(
        students=[1, 1, 0, 0, 1], sandwiches=[0, 1, 1, 1, 0]
    )
)