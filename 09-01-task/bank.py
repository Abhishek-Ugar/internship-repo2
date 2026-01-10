balace=5000
is_account_active=True

print("welcome to bank")

if is_account_active== True:
    print("Account is Active")
else:
    print("Account is blocked")

deposit=2000
balace+=deposit
print("after depoasit:,",balace)

withdraw=3000

if withdraw<=balace and is_account_active==True:
    balace==withdraw
    print("withdrawal successful")
else:
    print("insuffuciet balance or Account blocked ")

print("Final balance:",balace)
