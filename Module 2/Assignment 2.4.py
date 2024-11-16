# input statements
salary = float(input('Enter your salary:'))
numDependents = float(input('Enter the number of dependents'))

# calculate taxes here
statetax = 0.065 * salary
federaltax = 0.28 * salary
dependentdeduction = 0.025 * salary * numDependents

# Calculate total withholding
totalWithholding = statetax + federaltax + dependentdeduction

#Calculate take-home pay 
takeHomePay = salary - totalWithholding

# output statements
print('StateTax:' + str(statetax))
print('Federal Tax:' + str(federaltax))
print('Dependents:' + str(dependentdeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))