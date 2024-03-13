from collections import Counter

# Given dataset
interests = [(0,'Hadoop'),(1,'c'),(1,'c++'), (2,'java'),(2,'Data Science'),(2,'Big Data'), (3,'python'),(3,'data mining'),(4,'web mining'),(4,'data structure'),(5,'deep learning'),(5,'machine learning')]

# Count interests
interest_counts = Counter([interest for _, interest in interests])

# Get most common interests
most_common_interests = interest_counts.most_common()

# Print the most popular interests
print("Most popular interests:")
for interest, count in most_common_interests:
    print(f"{interest}: {count}")
