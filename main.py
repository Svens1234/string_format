#print(1+1)
#print('1'+'1')
#age = 23
#print('Jack is ' + str(age) + ' years old')
#print('Jack is ' + str(23) + ' years old')

name = 'Jack'
age = 23
name_and_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)
print(name_and_age)
name_and_age = 'My name is {0}. I\'m {1} years old.'.format('Jack', 23)
print(name_and_age)
name_and_age = 'My name is {}. I\'m {} years old.'.format('Jack', 23)
print(name_and_age)

week_days = 'There are 7 days in a week: {}, {}, {}, {}, {}, {}, {}.'\
    . format('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(week_days)

week_days1 = 'There are 7 days in a week: {1}, {6}, {2}, {3}, {0}, {5}, {4}.'\
    .format('Friday', 'Monday', 'Wednesday', 'Thursday', 'Sunday', 'Saturday', 'Tuesday')
print(week_days1)

week_days2 = 'There are 7 days in a week: {mo}, {tu}, {we}, {th}, {fr}, {sa}, {su}.'\
    .format(fr = 'Friday', mo = 'Monday', we = 'Wednesday', th = 'Thursday', su = 'Sunday', sa = 'Saturday', tu = 'Tuesday')
print(week_days2)

float_result = 1000 / 7
print(float_result)
print('The result of division is {0}'.format(float_result))
print('The result of division is {0:1.3f}'.format(float_result))

name = 'Bob'
age = 25
name_age1 = f'My name is {name}. I\'m {age} years old.'
print(name_age1)

name = 'Bob'
age = 25
print('My name is %s. I\m %d years old' % (name,age))
