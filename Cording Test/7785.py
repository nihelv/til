
o={
}

log=int(input())
# log_c=4

for n in range(log):
    log_n=input().split()
    o[log_n[0]]=log_n[1]

e=[k for k, v in o.items() if v == 'enter']

print(*e, sep='\n')


# 소트 안해서 틀린 거 같음..