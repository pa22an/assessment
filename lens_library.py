s = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
s = s.split(",")
def get_current_value(a):
    curr_value = 0
    for i in a:
        curr_value = ((ord(i) + curr_value) * 17) % 256
    return curr_value

res = 0
for i in s:
    res += get_current_value(i)
        
print(res)

#another solution using map:
#print(sum(list(map(get_current_value, s))))