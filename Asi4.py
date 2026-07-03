name="Neha Kapoor"
age=28
gen="Female"
blood="B+"
weight=55.5
height=165.0
fee=500.0
charge=150
total=fee+charge
print("\tCITY CARE HOSPITAL")
print("\tPatient Information Card")
print(f"{'-'*40}")
print(f"Patient Name{' '*10}:{' '*2}{name}")
print(f"Age{' '*19}:{' '*2}{age}")  
print(f"Gender{' '*16}:{' '*2}{gen}")
print(f"Blood Group{' '*11}:{' '*2}{blood}")
print(f"Weight{' '*16}:{' '*2}{weight} kg") 
print(f"Height{' '*16}:{' '*2}{height} cm")
print(f"Consultation Fee{' '*6}:{' '*2}{fee:.2f}")
print(f"Registration Charge{' '*3}:{' '*2}{charge:.2f}")

print(f"{'-'*40}")
print(f"Total Amount{' '*10}:{' '*2}{total:.2f}")