1 == 1
1 != 1
1 is 1
data = [1, 1.5, 3.4]
test_data = [1, 1.5, 3.4]
data == test_data #true because values match
data is test_data #false because 2 different objects
#not Keyword
data is not test_data #true because objects are different
age = 29
#and keyword (similar to C++ &&)
if age > 20 and age < 30:
    print('between 20 and 30')
#not keyword (simlar to C++ !=)
if age < 30 or age > 60:
    print ('Not between 30 and 60')
if age > 20 and age < 30 or age > 60:
    print ('Yes')