
lilei={"name":"Lilei","homework":[],"quizzes":[],"tests":[]}
hanmeimei={"name":"Hanmeimei","homework":[],"quizzes":[],"tests":[]}
jim={"name":"Jim","homework":[],"quizzes":[],"tests":[]}

lilei['homework']=[90,97,75,92]
lilei['quizzes']=[88,40,94]
lilei['tests']=[75,90]

hanmeimei['homework']=[100,92,98,100]
hanmeimei['quizzes']=[82,83,91]
hanmeimei['tests']=[89,97]

jim['homework']=[0,87,75,22]
jim['quizzes']=[0,75,78]
jim['tests']=[100,100]


students=[lilei,hanmeimei,jim]

for student in students:
    print(student['name'])
    print(student['homework'])
    print(student['quizzes'])
    print(student['tests'])


def average(numbers):
    total=0
    count=len(numbers)
    for i in numbers:
        total=total+i
    return total/count


def get_average(student):
    homework_avg=average(student['homework'])
    quizzes_avg=average(student['quizzes'])
    tests_avg=average(student['tests'])

    return homework_avg*0.1+quizzes_avg*0.3+tests_avg*0.6


print(get_average(lilei))

def get_letter_grade(score):
    if(score>=90):
        return "A"
    elif(score>=80):
        return "B"
    elif(score>=70):
        return "C"
    elif(score>=60):
        return "D"
    else:
        return "F"

print(get_letter_grade(get_average(lilei)))


def get_class_average(class_list):
    results=[]
    for i in class_list:
        results.append(get_average(i))
    average(results)
    
class_list=[80,40,94,82,83,91,0,75,78]
get_class_average(class_list)   

