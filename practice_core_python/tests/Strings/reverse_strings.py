
########## Reverse String ###########


name = "sai Krishna"

##### Slicing ####
reversed_string = name[::-1]
print(reversed_string)

#### Using reversed() and join() #########
reve_string = "".join(reversed(name))

####### By using loop #######
loop_reverse = ""
for char in name:
    loop_reverse=char+loop_reverse
print(loop_reverse)

####### Remove duplicates with reverse order#######
unique_name = "".join(reversed(sorted(set(name), key=name.index)))
print(unique_name)