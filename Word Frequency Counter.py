from collections import Counter
import re

text = input("Please paste your text here:")

words = re.findall(r'\b[a-z]+\b', text.lower())

stopwords = {"the" , "a" , "an" , "and" , "is" , "it" , "of" , "to"}
filtered = [w for w in words if w not in stopwords]

counts = Counter(filtered)

print("\nTop 10 words:")
for word, count in counts.most_common(10):
    bar = "" * count
    print(f"{word: 15} {count:3} {bar}")