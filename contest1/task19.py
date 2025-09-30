data = input().split()

word_count = {}

for word in data:
    if word == "end":
        break
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

result_words = []
for word, count in word_count.items():
    if count > 1:
        result_words.append(word)

print(" ".join(sorted(result_words)))