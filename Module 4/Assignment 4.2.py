#assign values 
userinputname = input ('Please input employee name: ')
userinputshift = float(input ('Please insert how many shifts you had: '))
userinputtrans = float(input ('Please insert Number of Transactions processed: '))
userinputvalue = float(input ('Please insert transactions dollar value: '))

#calculating productivity score
productivy_score = userinputvalue / userinputtrans / userinputshift

#if statement 
if productivy_score <= 30:
    bonus = 50
if productivy_score >= 31 < 69:
    bonus = 75
if productivy_score >= 70 < 199:
    bonus = 100
if productivy_score >= 200:
    bonus = 200

#print result
print (f"Employee Name: {userinputname}" ) 
print (f"Employee Bonus: {bonus} $")