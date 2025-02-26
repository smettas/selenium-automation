
from collections import Counter


names = "sdsghdhjkldfvhuowqedwoihij[ejpnnheoijffjpef]"

counter = Counter(names) ####### count repeated letters in key:value
print(counter)

most_count_letter, freq = counter.most_common(1)[0] ###### Most repeated letter
print(most_count_letter,freq)