
text = "abcabcd"
seen = ""
for char in text:

    if char not in seen:
        seen += char

count = len(seen)

print(count)
