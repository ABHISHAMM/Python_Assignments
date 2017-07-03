x=raw_input("Enter the numbers into list1:")
y=raw_input("Enter the numbers into list2:")
a=list(set(x)-set(y))
print "Difference b/w list 1 and 2:",a
b=list(set(y)-set(x))
print "Difference b/w list 2 and 1:",b
list3=a+b
print "Resulting List is :",list3
