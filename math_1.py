# num = input().split()


a = input().split()
static_pay=int(a[0])
flex_pay=int(a[1])
product_price=int(a[2])

if product_price-flex_pay <= 0:
    x = -1
else:
    x = static_pay/(product_price-flex_pay)+1


print(int(x))
