# task 1
print('this is task 1')
value = 10 + 5
print(value)

value = input('input some text')
print(value)

# task 2
print('this is task 2')
seconds = int(input('input seconds:'))
seconds = seconds % (24 * 3600)
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print('%d:%02d:%02d' % (hour, minutes, seconds))

# task 3
print('this is task 3')
number = int(input('input number:'))
num2 = str(number) + str(number)
num3 = str(number) + str(number) + str(number)
print(number + int(num2) + int(num3))

# task 4
print('this is task 4')
number = str(input('input number:'))
counter = 0
x = 0
while counter < len(number):
    if x < int(number[counter]):
        x = int(number[counter])
    counter += 1
print('max digit = ', x)

# task 5
print('this is task 5')
income = int(input('input income = '))
costs = int(input('input costs = '))
profitability = 0
employees = 0
prof_per_emp = 0
if (income > costs):
    print('Our company doing well')
    profitability = income/costs
    employees = int(input('input employess = '))
    prof_per_emp = income / employees
    print('profitability per employee = %.2f' % prof_per_emp)
else:
    print('Our company have losses')

#task 6
print('this is task 5')

first_day_res = int(input('first day result = '))
target_res = int(input('target result = '))
coef = 0.1
result = first_day_res
day = 1
while True:
    print('%d-й день:%.2f' % (day, result))
    day += 1
    result = result + result * coef
    if result > target_res:
        print('%d-й день:%.2f' % (day, result))
        break





