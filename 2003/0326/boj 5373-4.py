import sys
sys.stdin=open('../input.txt','r')

def g(a):
    if a=='U':
        u[0],u[1],u[2],u[3],u[4],u[5],u[6],u[7],u[8]=u[6],u[3],u[0],u[7],u[4],u[1],u[8],u[5],u[2]
        b[2],b[1],b[0],r[2],r[1],r[0],f[2],f[1],f[0],l[2],l[1],l[0]=\
            l[2],l[1],l[0],b[2],b[1],b[0],r[2],r[1],r[0],f[2],f[1],f[0]
    if a=='D':
        d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8]=d[6],d[3],d[0],d[7],d[4],d[1],d[8],d[5],d[2]
        f[6],f[7],f[8],r[6],r[7],r[8],b[6],b[7],b[8],l[6],l[7],l[8]=\
            l[6],l[7],l[8],f[6],f[7],f[8],r[6],r[7],r[8],b[6],b[7],b[8]
    if a=='F':
        f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8]=f[6],f[3],f[0],f[7],f[4],f[1],f[8],f[5],f[2]
        u[6],u[7],u[8],r[0],r[3],r[6],d[2],d[1],d[0],l[8],l[5],l[2]=\
            l[8],l[5],l[2],u[6],u[7],u[8],r[0],r[3],r[6],d[2],d[1],d[0]
    if a=='B':
        b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8]=b[6],b[3],b[0],b[7],b[4],b[1],b[8],b[5],b[2]
        u[2],u[1],u[0],l[0],l[3],l[6],d[6],d[7],d[8],r[8],r[5],r[2]=\
            r[8],r[5],r[2],u[2],u[1],u[0],l[0],l[3],l[6],d[6],d[7],d[8]
    if a=='L':
        l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8]=l[6],l[3],l[0],l[7],l[4],l[1],l[8],l[5],l[2]
        u[0],u[3],u[6],f[0],f[3],f[6],d[0],d[3],d[6],b[8],b[5],b[2]=\
            b[8],b[5],b[2],u[0],u[3],u[6],f[0],f[3],f[6],d[0],d[3],d[6]
    if a=='R':
        r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8]=r[6],r[3],r[0],r[7],r[4],r[1],r[8],r[5],r[2]
        u[8],u[5],u[2],b[0],b[3],b[6],d[8],d[5],d[2],f[8],f[5],f[2]=\
        f[8],f[5],f[2],u[8],u[5],u[2],b[0],b[3],b[6],d[8],d[5],d[2]
for _ in range(int(input())):
    u=['w']*9;d=['y']*9;f=['r']*9;b=['o']*9;l=['g']*9;r=['b']*9;n=int(input());o=input().split()
    for i in o:
        if i[1]=='+':g(i[0])
        else:g(i[0]);g(i[0]);g(i[0])
    print(*u[0:3],sep="");print(*u[3:6],sep="");print(*u[6:9],sep="")