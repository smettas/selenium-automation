from collections import Counter

my_list = [1,2,5,2,4,5,13,7,4,2,3,4,4,10,4,5,3,10,12]

counter = Counter(my_list)
print(f"count occurences: {counter}")

most_common_element, frequency = counter.most_common(1)[0]

print(most_common_element)
print(frequency)