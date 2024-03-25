# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1956146
 
# Date: 2022/12/14




def get_student_grades():
    valid=[0,20,40,60,80,100,120] # valid range of credit values
    while True:
        try:
            pass_grade = int(input('Please Enter Your Credits at Pass: '))
            if pass_grade not in valid:
                print('Out Of Range')
                continue
            defer_grade = int(input('Please Enter Your Credit at Defer: '))
            if defer_grade not in valid:
                print('Out Of Range')
                continue
            fail_grade = int(input('Please Enter Your Credit at Fail: '))
            if fail_grade not in valid:
                print('Out Of Range')
                continue
            break  # input is valid, exit the loop
        except ValueError:
            print('Integer required')
    return pass_grade,defer_grade,fail_grade

pass_grade,defer_grade,fail_grade=get_student_grades()
while True:
    total=pass_grade+defer_grade+fail_grade
    if total != 120:
        print('Total Incorrect ')
        pass_grade,defer_grade,fail_grade=get_student_grades()
        continue
    elif pass_grade == 120:
        print('Progress')
    elif pass_grade==100:
        print('Progress(module trailer)')
    elif 60 >= fail_grade and fail_grade >=0:
        print('Do not progress -Module retriver')
    elif fail_grade >= 80 and fail_grade <=120:
        print('Exclude')
    break
