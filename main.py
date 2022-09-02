

'''
#Question 1
'''
# defining the list of student ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#sorting the ages in the list
ages.sort()
print('Sorted List is \n',ages)

# finding the minimum most age among the students
miniage=min(ages)
print('minimum value is',miniage)

# finding the maximum most age among the students
maxage=max(ages)
print('maximum value is',maxage)

#Appending both minimum and maximum ages to the list and printing new list
ages.append(miniage)
ages.append(maxage)
print('After appending minimum and maximum\n',ages)

#Finding the median of the list
length=len(ages)                          #finding the length of list
lenmed= (length-1)//2                     # floor division by 2
median=(ages[lenmed]+ages[lenmed+1])/2    # finding the median
print('median =',median)                  #printing median value

#Finding and printing the average of the list
itemsum=sum(ages)
avg=itemsum/length
print('average=',avg)

#finding and printing the range of list
rangeofages=maxage-miniage
print('range =',rangeofages)




'''
#Question 2
'''
#creating an empty dog dictionary and inserting values into keys

dog=dict()
dog['name']='Woof Woof'
dog['color']='Yellow'
dog['breed']='Labrador'
dog['legs']='4'
dog['age']='3'
print('Dog dictionary is',dog)

#creating an empty student dictionary and inserting values into keys

student=dict()
student['first_name']='Govind'
student['last_name']='Tatiyal'
student['gender']='Male'
student['age']='29'
student['marital status']='Single'
student['skills']= ['Java','Python','sql']
student['country']='India'
student['city']='Amritsar'
student['address']='Gali #14, New Pavan Nagar'
print('student dictionary is',student)

#finding the length of student dictionary
stulen=len(student)
print(stulen)

#Printing student skills along with the type of input
print(student['skills'])
print(type(student['skills']))

#Modifying skills and adding values
student['skills'].extend(['Nutrition','Exercise Physiology','Sports Science'])
print(student['skills'])

#printing dictionary keys as list
print(student.keys())

#printing dictionary values as list
print(student.values())



'''
#Question 3
'''
#creating tuples with imaginary brother and sister
sister=("Radhika ","Rajma")
brother=("Sandip","Shiva")

#joining the tuples into siblings
siblings=sister+ brother
print(siblings)

#printing number of siblings
len1 =len(siblings)
print(len1)


#adding parents to siblings tuples and adding all to family members
family_members= siblings+("Sham Lal","Santosh Rani",)
print(family_members)


'''#Question 4
'''
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#finding the length of it_companies set
print(len(it_companies))

#adding a value to the it_companies set
it_companies.add('Twitter')
print(it_companies)

#adding multiple companies to it_companies set
it_companiesnew={'TCS','JPMC','EPAM'}
it_companies.update(it_companiesnew)
print(it_companies)

#removing one of the comapnies from it_comapnies set
it_companies.remove('EPAM')
print(it_companies)

'''
#The main difference between remove and discard methods in python is that
#if there is no particular item which i want to remove from the set
#then discard() method will never raise and error, whereas remove method will
#raise error if value specified is not present in the set

#For instance above i have removed company named EPAM by remove() method
#it did so successfully, but i use that method again it will raise an error
#again stating that item could not be found , but on the other hand discard
#mthod will never raise an error, it will print whole set as it is instead.
'''

#Joining A and B
print(A.union(B))

# finding A intersection B
print(A.intersection(B))

#verifying if A is subset of B
print(A.issubset(B))

#verifying if A and B are disjoint sets
print(A.isdisjoint(B))

#joining A with B and B with A
print(A.union(B))
print(B.union(A))

#finding symmetric difference between A and B
print(A.symmetric_difference(B))

#deleting both the sets A and B
A.clear()
print(A)

B.clear()
print(B)

#converting ages to a set
agesintoset=set(age)
print(agesintoset)

#comparing length of list to the set

lengthoflist=len(age)
print(lengthoflist)

lengthofset=len(agesintoset)
print(lengthofset)

'''
#after printing the length of set and list, it can be noticed that length of set
#is less than the list. Because in set duplicate elements will be removed.
'''


'''
#Question 5
'''
#Given area of circle =30 meters
from math import pi           #importing pi from math
radii=30
area_of_circle=pi*radii**2        #formula for finding area of circle

#printing the value of calculated area
print('Area of circle with given radius 30 is', area_of_circle )

circum_of_circle=2*pi*radii
print('Circumference of circle with given radius 30 is', circum_of_circle )

radius=float(input("Enter a value for radius of circle"))
area_of_circle_new=pi*radius**2
print("Area of circle with radius",radius,'is',area_of_circle_new)


'''
#Question 6
'''
#Given string = “I am a teacher and I love to inspire and teach people”

string1= 'I am a teacher and I love to inspire and teach people'

#splitting and printing string with split method
strsplit=string1.split()
print(strsplit)

#removing duplicates by converting list into set inorder to get unique words

uniquewords=set(strsplit)
print(uniquewords)
print('number of unique words are',len(uniquewords))


'''
#Question 7
'''
#Given Name Age Country City as Asabeneh 250 Finland Helsinki respectively

#writing and printing the sequence in which we want to have desirable output
tabseq='Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki'
print(tabseq)



'''
#Question 8
'''
#Given radius =10 and area= 3.14 * radius ** 2

radius=10
area=3.14*radius**2
#printing the message by using string formatting method
print("The area of a circle with radius {} is {} meters square.".format(radius,int(area)))




#Question 9

# Creating an empty student weights list and reading the input from user
studentsweightlist = list()
noofstudents = int(input("Enter the number of students : "))

for i in range(noofstudents):                              # initiating a for loop
    studentsweight = float(input("Enter the weight of Student of student " + str(i+1)))     # Taking the weight of the students in pounds from user
    studentsweightlist.append(studentsweight*0.453592)                                      # Converting weights in kgs and appending them to the list
studentsWeightListWithPrecision = ['%.2f' % elem for elem in studentsweightlist]            # Converting Student weight list to list with 2 decimal places
print(studentsWeightListWithPrecision)



#importing required libraries


import pandas as pd
# importing libraries
from sklearn.model_selection import train_test_split  # Package for splitting the data

datainput = {'first_column': ['1', '2', '3', '6', '6', '7', '10', '11'],
        'second_column': ['o', 'o', 'x', 'x', 'x', 'o', 'o', 'o'],
        }
gt = pd.DataFrame(datainput)

print(gt)
gt.head(5)
x = gt.loc[:, ["first_column"]]
y = gt.loc[:, ["second_column"]]
x_training, x_testing, y_training, y_testing = train_test_split(x, y, random_state=0, train_size=.75)
# importing required libraries
from sklearn.neighbors import KNeighborsClassifier

# using KNN classifier with no of neighbours as 3
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_training, y_training)
y_testing = knn.predict(x_testing)
# accuracy
acc_knn = round(knn.score(x_testing, y_testing) * 100, 2)
# printing for the accuracy
print("KNN accuracy is:", acc_knn)
# importing required libraries for the classification report
from sklearn.metrics import classification_report
print(classification_report(x_testing, y_testing))