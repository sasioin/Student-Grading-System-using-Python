# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1956146
 
# Date: 2022/12/14





valid_inputs=[0,20,40,60,80,100,120]
progress_count=0
trailer_count=0
retriver_count=0
exclude_count=0
dictionary_inputs={}
student_id=()


def histogram():
            print('-'*40)
            print('Histogram')
            print('Progress',progress_count,' ', ':',' ',(progress_count)*' * ')
            print('Trailer',trailer_count,' ', ':',' ',(trailer_count)*' * ')
            print('Retriever',retriver_count,' ', ':',' ',(retriver_count)*' * ')
            print('Exclude',exclude_count,' ', ':',' ',(exclude_count)*' * ')
            print(progress_count+trailer_count+retriver_count+exclude_count , 'Outcome In Total')
            print('-'*40)


def get_student_grades():
    valid=[0,20,40,60,80,100,120] # valid range of credit values
    global student_id
    while True:
        student_id=input('Enter Your Student ID:')
        try:
            if (student_id[:1])!= 'w':
                print('Invalid Input , ID Should Start With - w ')
                continue
            if len(student_id)!=8:
                print('Invalid Input , ID Should have 8 Digits - w1234567 ')
                continue
        except :
            break
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
        progress_count=progress_count+1
        print('Progress')
        po='Progress'
    elif pass_grade==100:
        trailer_count=trailer_count+1
        print('Progress(module trailer)')
        po='Progress(module trailer)'
    elif 60 >= fail_grade and fail_grade >=0:
        retriver_count=retriver_count+1
        print('Do not progress -Module retriver')
        po='Do no progres(module retriever)'
    elif fail_grade >= 80 and fail_grade <=120:
        exclude_count=exclude_count+1
        print('Exclude')
        po='Exclude'
    dictionary_inputs[student_id]=po+'-'+' '+str(pass_grade)+','+str(defer_grade)+','+str(fail_grade)
    for i in range(total):
        loop_inputs=str(input('Would You Like To Enter Another Set Of Data?\nEnter ''y'' For Yes or ''q'' To Quit and View Results\n'))
        loop_input=loop_inputs.lower()
        if loop_input=='y':
            pass_grade,defer_grade,fail_grade=get_student_grades()
            break
        elif loop_input=='q':
            histogram()
            for key, value in dictionary_inputs.items():
                print(f"{key}: {value}")
            exit()
        elif ValueError:
            print('Invalid Input Try Again')
