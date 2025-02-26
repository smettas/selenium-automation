
###### Removing 5 in the list ##########
my_list = [1,2,5,1,2,52,6,5,5,]

updated_list = list(filter(lambda x:x!=2, my_list))
print(updated_list)

####### By using List comprehencsive #######
comprahensive_list = [x for x in my_list if x!=2]
print(comprahensive_list)