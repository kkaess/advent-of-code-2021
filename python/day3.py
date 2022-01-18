# IPython log file


f = open('input.txt');lines = f.readlines();f.close()
sum = 0
lines[0]
ones = [0]*12
zeros = [0]*12
for line in lines:
    stripped = line[0:12]
    for ind,ch in enumerate(stripped):
        if ch == '0':
            zeros[ind] += 1
        else:
            ones[ind] += 1
            
ones
zeros
st = ''
for a,b in zip(ones,zeros):
    if a>b:
        st += '1'
    else:
        st += '0'
        
st
v1 = int(st,2)
st2 = '001111000000'
v2 = int(st2,2)
v1*v2
trim1 = [line[1:] for line in lines if line[0] == '1']
trim1
st
trim2 = [line[1:] for line in trim1 if line[0] == '1']
len(trim2)
trim3 = [line[1:] for line in trim2 if line[0] == '0']
len(trim3)
trim4 = [line[1:] for line in trim3 if line[0] == '0']
len(trim4)
trim5 = [line[1:] for line in trim4 if line[0] == '0']
len(trim5)
trim6 = [line[1:] for line in trim5 if line[0] == '0']
len(trim6)
trim7 = [line[1:] for line in trim6 if line[0] == '1']
len(trim7)
trim8 = [line[1:] for line in trim7 if line[0] == '1']
len(trim8)
trim8
trim1 = [line[1:] for line in lines if line[0] == '0']
len(trim1)
trim1 = [line[1:] for line in trim1 if line[0] == '0']
len(trim1)
trim1 = [line[1:] for line in trim1 if line[0] == '1']
len(trim1)
trim1 = [line[1:] for line in trim1 if line[0] == '1']
len(trim1)
trim1 = [line[1:] for line in trim1 if line[0] == '1']
len(trim1)
trim1 = [line[1:] for line in trim1 if line[0] == '1']
len(trim1)
trim1
st2
int('110000111011',2)*int('001111001001',2)
ones - zeros
diff = [a-b for a,b in zip(ones,zeros)]
diff
int('1011',2)*int('1001',2)
np.loadtxt('input.txt')
np.loadtxt('input.txt',dtype='b16')
np.loadtxt('input.txt',dtype='bin')
lines
check = [line for line in lines if line[0] == '0']
check
check2 = [lines[1:] for line in check]
check2
check2 = [line[1:] for line in check]
check2
exit()
