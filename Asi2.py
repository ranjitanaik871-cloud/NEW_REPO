name="Priya Sharma"
product="laptop"
price=2499.00
quantity=2
gst=18
charge=99.00

invoice ="INV20250520"
date="20/May/2025"
total_price=price*quantity
Gst=total_price*gst/100
final=total_price+Gst+charge

print("\t\tSHOPSMART ONLINE")
print("----------------------------------------------------")
print("\t\tInvoice")
print(f"Customer Name{' '*3}:{' '*2}{name}")
print(f"Invoice Number{' '*2}:{' '*2}{invoice}")
print(f"Date{' '*12}:{' '*2}{date}\n")

print(f"{'Product Details'}{' '*5}{'Price(INR)'}{' '*5}{'Quantity'}{' '*5}{'Total(INR)'}")      
print(f"{product}{' '*13}{price:.2f}{' '*13}{quantity}{' '*11}{total_price:.2f}")

print(f"{'-'*60}")

print(f"Total Price{' '*6}:{' '*5}{total_price:.2f}")
print(f"GST{' '*14}:{' '*5}{Gst:.2f}")
print(f"Delivery Charge{' '*2}:{' '*5}{charge:.2f}")
print(f"{'-'*60}")

print(f"Final Amount{' '*5}:{' '*5}{final:.2f}")
