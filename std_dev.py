# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age
        #object
    def get_age(self):
        return self._age
    # get age function
def std_dev(namelist):
    number = namelist[1].get_age()
    for i in range(0, len(namelist)-1):
        number += namelist[i].get_age()
    mean = number/len(namelist)
    variance = ((namelist[1].get_age() - mean) ** 2)
    for i in range(0, len(namelist)-1):
        variance += ((namelist[i].get_age()-mean)**2)
    real_variance = variance/len(namelist)
    # calculates mean and variance
    stddev = real_variance**0.5
    # calculates standard deviation
    return stddev

#p1 = Person("mercedes", 13)
#p2 = Person("john", 18)
#person_list = [p1, p2]
#answer = std_dev(person_list)
#print(answer)
