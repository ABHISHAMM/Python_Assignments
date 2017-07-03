x=raw_input('Enter the metals :')
y=raw_input('Enter the nonmetals :')
list1=x.split(",")
list2=y.split(",")
tuple1=tuple(list1)
tuple2=tuple(list2)
print'Metals :',tuple1
print'Non metals :',tuple2
a=len(tuple2)
print 'length of tuple2 is : ',a
tuple2=tuple2[:-1]
print 'Tuple2 after delete a last element is :',tuple2


