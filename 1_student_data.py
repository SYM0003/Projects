

n=int(input('enter the number of student\n'))
d={}
with open('student_data.txt','a') as f:
    f.write('The student details are given below:\n')
    while len(d)!=n:
        name=input('enter student name\n')
        f.write(name+'\t\t')
        marks=eval(input('enter the list of marks for {}\n'.format(name)))
        f.write(str(marks)+'\t\t\n')
        d[name]=marks

while True:
    name=input('enter student name for getting the marks detail\n')
    if name in d:
        print('Marks for {} are :{}'.format(name,d[name]))
    else:
        print('student not found')

    option=input("do you want to see another student's marks? enter yes|no\n").lower()
    # while True:
   
    while True:
        if option in ['yes','no']:
            break
        option=input('invalid option please enter yes|no\n').lower()
    if option =='no':
        break
        
print('Thankyou for using our services have a good day')