# Η λίστα με τις εργασίες μας
# Ξεκινάμε με 3 εργασίες έτοιμες
tasks = ["Μάθημα Python", "Άσκηση", "Ψώνια"]

print("=" * 35)
print("        TO-DO LIST")
print("=" * 35)

# Εκτύπωση όλων των εργασιών
# Το enumerate μας δίνει και τον αριθμό και την εργασία μαζί
print("📋 Εργασίες:")
for i, task in enumerate(tasks):
    print(f"  {i+1}. {task}")

print(f"\nΣύνολο εργασιών: {len(tasks)}")
print("=" * 35)

# Προσθήκη νέας εργασίας
tasks.append("Διάβασμα βιβλίου")
print(f"✅ Προστέθηκε: 'Διάβασμα βιβλίου'")

# Αφαίρεση εργασίας
tasks.remove("Ψώνια")
print(f"❌ Αφαιρέθηκε: 'Ψώνια'")

# Έλεγχος αν υπάρχει εργασία
if "Άσκηση" in tasks:
    print(f"🔍 Η 'Άσκηση' υπάρχει στη λίστα!")

print("\n📋 Τελική λίστα:")
for i, task in enumerate(tasks):
    print(f"  {i+1}. {task}")

print(f"\nΣύνολο εργασιών: {len(tasks)}")
print("=" * 35)