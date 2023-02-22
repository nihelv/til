word=input()
# word='level'
in_word=[]

for item in word:
    in_word.append(item)

if in_word[:] == in_word[-1::-1]:
    print(1)
else:
    print(0)