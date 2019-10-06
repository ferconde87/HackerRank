# Enter your code here. Read input from STDIN. Print output to STDOUT
def designerDoorMat(N,M):
    for i in range(1, N, 2): 
        print((".|."*i).center(M, '-'))
    print(("WELCOME").center(M, '-'))
    for i in range(N-2, -1, -2): 
        print((".|."*i).center(M, '-'))

def designerDoorMat2(N,M):
    mid = N // 2
    padding = M // 2 - 1
    mid_padding = (M - 7) // 2
    for i in range(mid):
        cur = padding-3*i
        times = (2*i)+1 
        print(("-"*cur)+(".|."*times)+("-"*cur))
    print(("-"*mid_padding)+"WELCOME"+("-"*mid_padding))
    for i in range(mid-1,-1,-1):
        cur = padding-3*i
        times = (2*i)+1 
        print(("-"*cur)+(".|."*times)+("-"*cur))

if __name__ == '__main__':
    N, M = map(int, input().split())
    designerDoorMat(N,M)
