p=float(input("price: "))
momssats= float(input("momssats: "))
pris= p/(1+momssats/100)
moms=momssats*pris/100
print(f"Du betalade {p}kr som motsvarar {pris}kr exklusiv moms samt du belade {moms}kr som moms")