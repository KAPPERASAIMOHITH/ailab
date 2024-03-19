from itertools import permutations

arr = ["SEND", "MORE"]
target_string = "MONEY"

unique_chars = set("".join(arr) + target_string)

if len(unique_chars) > 10:
    result = "No"
else:
    for perm in permutations("0123456789", len(unique_chars)):
        mapping = dict(zip(unique_chars, perm))
        if sum(int("".join(mapping[char] for char in s)) for s in arr) == int("".join(mapping[char] for char in target_string)):
            result = "Yes"
            break
    else:
        result = "No"

print(result)
