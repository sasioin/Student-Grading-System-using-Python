# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1956146
 
# Date: 2022/12/14




valid_inputs=[0,20,40,60,80,100,120]
progress_count=0
trailer_count=0
retriver_count=0
exclude_count=0
progress_list=[]
trailer_list=[]
retriver_list=[]
exclude_list=[]



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
    elif pass_grade == 120:
        progress_count=progress_count+1
        print('Progress')
        progress_list.append(['Progress','-' ,pass_grade,',',defer_grade,',',fail_grade])
    elif pass_grade==100:
        trailer_count=trailer_count+1
        print('Progress(module trailer)')
        trailer_list.append(['Progress(module trailer)','-' ,pass_grade,',',defer_grade,',',fail_grade])
    elif 60 >= fail_grade and fail_grade >=0:
        retriver_count=retriver_count+1
        print('Do not progress -Module retriver')
        retriver_list.append(['Module retriver','-' ,pass_grade,',',defer_grade,',',fail_grade])
    elif fail_grade >= 80 and fail_grade <=120:
        exclude_count=exclude_count+1
        print('Exclude')
        exclude_list.append(['Exclude','-' ,pass_grade,',',defer_grade,',',fail_grade])
    for i in range(total):
        loop_inputs=str(input('Would You Like To Enter Another Set Of Data?\nEnter ''y'' For Yes or ''q'' To Quit and View Results\n'))
        loop_input=loop_inputs.lower()
        if loop_input=='y':
            pass_grade,defer_grade,fail_grade=get_student_grades() 
            break
        elif loop_input=='q':
            histogram()
            textFile=open('program.txt','w') #add 'a' to record from past inputs
            for x in range(progress_count):
                print(*progress_list[x],file=open('program.txt','a'))#append & read records
            for x in range(trailer_count):
                print(*trailer_list[x], file=open('program.txt','a'))
            for x in range(retriver_count):
                print(*retriver_list[x], file=open('program.txt','a'))
            for x in range(exclude_count):
                print(*exclude_list[x], file=open('program.txt','a'))
            textFile.close()
            exit()
        else:
            ValueError
            print('Invalid Input Try Again')
            continue
            
