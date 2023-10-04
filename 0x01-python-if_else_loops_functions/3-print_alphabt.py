#!/usr/bin/python3
for letters in range(97,123):
    if chr(letters) == "q" or chr(letters) == "e":
        continue
    else:
        print(f"{chr(letters)}", end="")
