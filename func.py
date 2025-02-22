# def tong(x, y):
#     return x + y
#
#
# def handle(f, x):
#     return f(x)
#
#
# def kt(z):
#     return z%2==0 #Trả về số chia hết cho 2 ->True
#
# n = handle(lambda a: a % 2 == 0, 9)
# # lambda a: a%2==0 <=> Fuction
# n2=handle(kt,9)
# print(n)
# print(n2)

# x=12
# y=9
# def uc_c1(x,y):
#     while x+y != 0:
#         if x>y:
#             x%=y
#         else:
#             y %=x
#     return x+y
# def uc_c2(x,y):
#     if x * y ==0:
#         return x+y
#     else:
#         return uc_c2(x%y,y) if x>y else uc_c2(x,y%x)
#
# print(uc_c1(9,9))
# print(uc_c2(9,0))


def tong_so_hang(n):
    tong=0
    for i in range(1,n+1):
        tong+=i
    return tong
print(tong_so_hang(5))

def tong_de_quy(n):
    if n==1:
        return 1
    return n+tong_de_quy(n-1)
print(tong_de_quy(5))


#cau 6
def bieu_thuc(x,n):
    tong=0
    for i in range(1,n+1):
        tong+=x**(2*i)
    return tong

def bieu_thuc_de_quy(x,n):
    if n == 1:  # Điều kiện dừng
        return x ** 2
    return x ** (2 * n) + bieu_thuc_de_quy(x, n - 1)
print(bieu_thuc_de_quy(3,6))

#cau 7
def cau_7(n):
    tong=0
    for i in range(1,n+1):
        mau = i*(i+1)//2
        tong+=1/mau
    return tong


def cau_7_dequy(n):
    if n==1:
        return 1
    return 1/(n*(n+1)//2) + cau_7_dequy(n-1)

