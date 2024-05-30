s = {1, 2, 3, 4, 5} # we can create a set like this
print(s)

#set always contain unordered hashable unique elements
s = {1,2,3,4,5}
print(s)

s = {1,"linkan", True, 1.5, [2,3,4]} # this will gives us error because it contains 1.5 and a list as a element which are unhashable

s1 = {1,} # this is used to create a single element set
print(type(s1))
s2 = {1,True,False,0,2} # does not allow duplicate
print(s1)
print(s2)

s = set() # this creates an empty set
# set() is also used to convert any iterable to set like this
s = set("linkan")
print(s)

#Set Functions
# len()
s = {1,2,3,4,5}
print(len(s)) # gives length of the set

# max()
s = {1,2,3,4,5}
print(max(s)) # gives maximum value from the set

# min()
s = {1,2,3,4,5}
print(min(s)) # gives minimum value from the set

# all()
s = {1,2,3,4,5,True}
print(all(s)) # returns true if all elements are non-zero

# any()
s = {1, 0, False, 2}
print(any(s)) # returns True if a single element is non-zero

# add()
s = {1,2,3,4,5}
s.add(6) # add an element to the set
s.add((7,8,9)) # add multiple element in the set
print(s)

# remove()
s = {1,2,3,4,5}
s.remove(5) # remove 5 from the set
# if the element given inside remove() is not present it will give KeyError
# s.remove(6) # this gives error
print(s)

# discard()
s = {1,2,3,4,5}
s.discard(5) # it will remove 5 from the set
# if the element is not present in the set it will not give any error
s.discard(6)
print(s)

# clear()
s = {1,2,3,4,5}
s.clear() # remove all element from the set
print(s)

# union()
s1 = {1,2,3,4}
s2 = {1,2,5,6}
s3 = s1.union(s2) # it combines s1 and s2 together
print(s3)

# intersection()
s1 = {1,2,3,4}
s2 = {1,2,5,6}
print(s1.intersection(s2)) # it gives common element from both the set
print(s2.intersection(s1))

# difference()
s1 = {1,2,3,4}
s2 = {1,2,5,6}
print(s1.difference(s2)) # it gives unmatching elements from s1 set
print(s2.difference(s1)) # it gives unmatching elements from s2 set

# symmetric_difference()
s1 = {1,2,3,4}
s2 = {1,2,5,6}
print(s1.symmetric_difference(s2)) # it gives unmatched element from both the set
print(s2.symmetric_difference(s1)) # it gives unmatched element from both the set

# intersection_update()
s1 = {1,2,3,4}
s2 = {1,2,5,6}
s1.intersection_update(s2) # update s1 with the result of intersection
print(s1)
print(s2)

# difference_update()
s1 = {1,2,3,4}
s2 = {1,2,5,6}
s1.difference_update(s2) # update s1 with the result of difference
print(s1)
print(s2)

# symmetric_difference_update()
s1 = {1,2,3,4}
s2 = {1,2,5,6}
s1.symmetric_difference_update(s2) # update s1 with the result of symmetric difference
print(s1)
print(s2)