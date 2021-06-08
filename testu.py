'''def diff(arr):
    sum1=0
    sum2=0
    for i in range(len(arr)):
        sum1+=arr[i][i]
        sum2+=arr[i][n-i-1]
    return abs(sum1-sum2)

n=int(input())
arr=[]

for i in range(n):          # A for loop for row entries 
    a =[] 
    for j in range(n):      # A for loop for column entries 
         a.append(int(input())) 
    arr.append(a)
#for _ in range(n):
#    	arr.append(list(map(int, input().rstrip().split())))

result=diff(arr)
print(result)
'''
'''import math
def countpage(p,n):
    return (min(p//2,n//2-p//2))

n=int(input())
p=int(input())
count=countpage(p,n)
print(count)
'''

'''scores = list(map(int,input().rstrip().split()))
print(scores)
unique=list(reversed(sorted(set(scores)))) 
i=1
sety = set(scores)

print(len(scores))
print(sety)


 
        
print(unique)   '''     

'''visited = []
visited=[False for _ in range(10)]
print(len(visited))
print(visited)
inputt = list(map(int,input().rstrip().split()))
l = inputt[0]
r = inputt[1]
count =0

for i in range(l,r+1):
    num = i
    visited = []
    visited=[False for _ in range(10)]
    while(num):
        num1 = num%10
        print(num1)
        if visited[num1] == True :
            break
        visited[num1] = True
        print(visited)
        num=num//10
        
    if num==0:
        count+=1
print (visited)        
if count>0:
    print('no of distinct digit count:',count)
else:
    print('No unique count')
'''


print(ord('a'))
print(ord('z'))

b = ord('h') - 5
print(chr(b))


a = "shivank"
b = "shivank"
if a==b:
    print(a)
else:
    print("not matched")



r = 

'''for i in range(0,len(word)):
        if word[i]==chara_guess:
            flag[i]=True
            token=True
            break'''
