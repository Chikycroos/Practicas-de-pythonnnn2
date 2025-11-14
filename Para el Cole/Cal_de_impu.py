ingreso = float(input("Ingrese el ingreso anual: "))

if ingreso <=10000:
    impuesto = ingreso * 0.05

elif ingreso >10000 and ingreso <=20000:
    impuesto = ingreso * 0.10

else: 
    impuesto = ingreso * 0.15


pago_total = ingreso - impuesto 

print("Impuesto a pagar: ",impuesto)
print("Pago neto anual: ",pago_total)