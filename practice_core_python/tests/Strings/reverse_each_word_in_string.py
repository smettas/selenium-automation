

###### Reversed Words in a string ########
def reversed_words(num):
    words=num.split()
    reverse = [word[::-1] for word in words]

    return ' '.join(reverse)

input_string = "Hi how are you sai!"
print(reversed_words(input_string))