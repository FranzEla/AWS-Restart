import re

input_file = "preproinsulin-seq.txt"
output_file = "preproinsulin-seq-clean.txt"

with open(input_file, "r") as f:
    text = f.read()

print(text)

count_letters = 0
for i in text:
    count_letters += 1

print (count_letters, "\n")

# Remove all characters, except small letters:
text = re.sub(r'[^a-z]', '', text)

print(text, "\n")

count_letters = 0
for i in text:
    count_letters += 1

print (count_letters)

with open(output_file, "w") as f:
    f.write(text)






# Remove special characters using regular expressions
# text = re.sub(r'[^\w\s]', '', text)

# Remove special characters and whitespace using regular expressions
# text = re.sub(r'[^\w]', '', text)

# Remove numbers using regular expressions
# text = re.sub(r'\d+', '', text)

# Remove extra whitespace using regular expressions
# text = re.sub(r'\s+', ' ', text)  OR 
# text = re.sub(r'\s', '', text)

# Remove capital letters using regular expressions
# text = re.sub(r'[A-Z]', '', text)


