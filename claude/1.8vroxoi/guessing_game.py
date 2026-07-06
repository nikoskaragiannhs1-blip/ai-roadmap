# ============================================
# NUMBER GUESSING GAME v2.0 - Μάθημα 1.8
# ============================================

# Εισάγουμε το random για τυχαίους αριθμούς (το ξέρουμε από 1.7)
import random

# Ο μυστικός αριθμός — τυχαίος από 1 έως 20
mystikos = random.randint(1, 20)

# Μέγιστες προσπάθειες
max_prosp = 5

# Μετρητής προσπαθειών — ξεκινάει από 0
prosp = 0

# True/False αν κέρδισε
kerdisei = False

print("=" * 40)
print("    NUMBER GUESSING GAME v2.0 🎮")
print("=" * 40)
print(f"Σκέφτηκα αριθμό από 1 έως 20.")
print(f"Έχεις {max_prosp} προσπάθειες!\n")

# List Comprehension — φτιάχνουμε λίστα με τις εικασίες του παίκτη
# Ξεκινάει άδεια — θα γεμίζει με κάθε προσπάθεια
eikasies = []

# WHILE LOOP — συνεχίζει εωσότου:
# (1) εξαντληθούν οι προσπάθειες ή (2) μαντέψει
# "and not kerdisei" = και να μην έχει κερδίσει ακόμα
while prosp < max_prosp and not kerdisei:

    # Υπολογίζουμε πόσες προσπάθειες απομένουν
    # Το "-" κάνει αφαίρεση
    apoménoun = max_prosp - prosp

    print(f"🎯 Προσπάθεια {prosp + 1}/{max_prosp} (απομένουν {apoménoun}):")

    # Ζητάμε αριθμό από τον χρήστη
    # int() μετατρέπει το κείμενο σε αριθμό
    mandra = int(input("Γράψε τον αριθμό σου: "))

    # Προσθέτουμε την εικασία στη λίστα
    eikasies.append(mandra)

    # Αυξάνουμε τον μετρητή κατά 1
    # prosp += 1 είναι το ίδιο με prosp = prosp + 1
    # Νέο σύμβολο: += σημαίνει "πρόσθεσε στον εαυτό μου"
    prosp += 1

    # Ελέγχουμε την εικασία
    if mandra == mystikos:
        kerdisei = True
    elif mandra < mystikos:
        # Αν απομένουν προσπάθειες, δίνουμε υπόδειξη
        if apoménoun > 1:
            print("📈 Μικρός! Δοκίμασε μεγαλύτερο.\n")
    else:
        if apoménoun > 1:
            print("📉 Μεγάλος! Δοκίμασε μικρότερο.\n")

# Τελικό αποτέλεσμα
print("\n" + "=" * 40)

if kerdisei:
    print(f"🎉 ΚΕΡΔΙΣΕΣ!")
    print(f"Ο αριθμός ήταν: {mystikos}")
    print(f"Τον βρήκες σε {prosp} προσπάθειες!")
else:
    print(f"😢 ΕΧΑΣΕΣ!")
    print(f"Ο αριθμός ήταν: {mystikos}")

# Εκτυπώνουμε όλες τις εικασίες που έκανε
# List comprehension — μετατρέπει κάθε αριθμό σε κείμενο
# str(x) μετατρέπει αριθμό σε κείμενο
eikasies_str = [str(x) for x in eikasies]

# ", ".join(...) ενώνει τη λίστα με κόμμα μεταξύ τους
# Νέο σύμβολο: .join() ενώνει στοιχεία λίστας σε ένα string
print(f"Εικασίες σου: {', '.join(eikasies_str)}")
print("=" * 40)