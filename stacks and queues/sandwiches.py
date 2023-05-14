class Solution(object):
    def countStudents(students, sandwiches) -> int:

        count = 0
        while len(students) > count:
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                count = 0
            else:
                students.append(students[0])
                count+=1
            students.pop(0)
        return len(students)
    
stud = [1,1,1,0,0,1]
sand = [1,0,0,0,1,1]

solution = Solution.countStudents(students=stud, sandwiches=sand)
print(solution)