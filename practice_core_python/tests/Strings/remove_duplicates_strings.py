
s="hello"

updated = "".join(sorted(set(s), key=s.index))
print(updated)
