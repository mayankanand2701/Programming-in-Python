StringList1 = input("Enter the list of strings separated by space: ")
StringList1 = StringList1.split()

# Count the occurrences of each string in the list
from collections import Counter
d = Counter(StringList1)

# Generate a list containing strings repeated twice or more
MStringList1 = [k for k, v in d.items() if v >= 2]

# Print the generated list
print("The list containing strings repeated twice or more:")
print(MStringList1)

# Check if each item in MStringList1 occurs even or odd number of times in StringList1
for item in MStringList1:
    occurrence_count = StringList1.count(item)
    if occurrence_count % 2 == 0:
        print(f"The item '{item}' occurs even number of times in StringList1.")
    else:
        print(f"The item '{item}' occurs odd number of times in StringList1.")

# Remove the ith (i >= 2) occurrence of a given word in StringList1
word_to_remove = input("Enter the word you want to remove :(that occurs twice)")
if StringList1.count(word_to_remove) >= 2:
    index_to_remove = StringList1.index(word_to_remove, StringList1.index(word_to_remove) + 1)
    del StringList1[index_to_remove]
    print(f"The {index_to_remove + 1}th occurrence of '{word_to_remove}' is removed from StringList1.")
else:
    print(f"'{word_to_remove}' does not occur at least twice in StringList1.")

# Print the updated StringList1
print("StringList1 after removal operation:")
print(StringList1)
