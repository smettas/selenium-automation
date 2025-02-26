

dict1 = {'a':1, 'b':3, 'z':4, 'd':5}
dict2 = {'a':5, 'e':10, 'g':14, 'h':22}

merged_dict = dict1 | dict2
print(f"merged dict {merged_dict}")

dict1.update(dict2)
print(dict1)
