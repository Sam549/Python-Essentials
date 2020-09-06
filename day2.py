#list datatype
list_dt=[1,2,3,4]
#append
list_dt.append(5)
print(list_dt)
#index
a=list_dt.index(4)
print(a)
#insert
list_dt.insert(3,66)
print(list_dt)
#sum of elements
print(sum(list_dt))
#length
print(len(list_dt))


#Tuple datatype
tup=(1,2.3,54)
#length
print(len(tup))
#max
print(max(tup))
#min
print(min(tup))
#index
print(tup.index(54))
#count
print(tup.count(5))

#Dictionary
dict={ 'Name' : 'Nandini', 'Age' : 12, 'ID' : 2541997 }
#type
print(type(dict))
#length
print(len(dict))
dict2={'Class':'six'}
#update
dict.update(dict2)


#Sets

sets1=set(["a", "b", "c"])
#add
sets1.add('rr')
#set2
sets2=set(["e"])
#intersection
print(sets1 & sets2)
#clear
sets1.clear()

#String Datatype

stri="This is first assignment"
#Slicing
print(stri[3:12])
#update
stri='i'
print(stri)
#deleting
del stri
