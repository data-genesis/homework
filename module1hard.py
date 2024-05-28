grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

average_score = [(grades[0]), (grades[1]), (grades[2]), (grades[3]), (grades[4])]
student_id = list(students)

s1 = (student_id[4], (sum(average_score[0])/len(average_score[0])))
s2 = (student_id[1], (sum(average_score[1])/len(average_score[1])))
s3 = (student_id[0], (sum(average_score[2])/len(average_score[2])))
s4 = (student_id[3], (sum(average_score[3])/len(average_score[3])))
s5 = (student_id[2], (sum(average_score[4])/len(average_score[4])))

console = dict([(s1), (s2), (s3), (s4), (s5)])
print(console)

