

#### By using Sorting ######### 2nd method is Counter(str1)==Counter(str2)
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

print(are_anagrams("Sai", "Metta"))
print(are_anagrams("Metta", "Metta"))

