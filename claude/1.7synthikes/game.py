# ============================================
# ΠΑΙΧΝΙΔΙ - Μάντεψε τον Αριθμό!
# ============================================

# Εισάγουμε το module "random" που φτιάχνει τυχαίους αριθμούς
# Το "import" φορτώνει έτοιμα εργαλεία που έχει η Python
import random

# random.randint(1, 10) → διαλέγει τυχαίο αριθμό από 1 έως 10
mystikoς_arithmos = random.randint(1, 10)

# Αριθμός προσπαθειών που έχει ο παίκτης
max_prosp = 3

print("=" * 40)
print("    ΜΑΝΤΕΨΕ ΤΟΝ ΑΡΙΘΜΟ! 🎮")
print("=" * 40)
print(f"Σκέφτηκα έναν αριθμό από 1 έως 10.")
print(f"Έχεις {max_prosp} προσπάθειες!\n")

# Μετράμε πόσες προσπάθειες έκανε ο παίκτης
prosp = 0

# Μεταβλητή που δείχνει αν κέρδισε — ξεκινάει False
kerdisei = False

# Η πρώτη προσπάθεια
print("🎯 Προσπάθεια 1:")

# input() → ζητάει από τον χρήστη να γράψει κάτι στο terminal
# int(...) → μετατρέπει αυτό που έγραψε σε αριθμό
mandra = int(input("Γράψε τον αριθμό σου: "))
prosp = 1  # μετράμε ότι έκανε 1 προσπάθεια

# Ελέγχουμε αν μάντεψε
if mandra == mystikoς_arithmos:
    # == σημαίνει "είναι ίσο με"
    kerdisei = True
elif mandra < mystikoς_arithmos:
    # < σημαίνει "μικρότερο από"
    print("📈 Μικρός! Δοκίμασε μεγαλύτερο.\n")
else:
    # αν δεν είναι ίσο και δεν είναι μικρότερο, είναι μεγαλύτερο
    print("📉 Μεγάλος! Δοκίμασε μικρότερο.\n")

# Η δεύτερη προσπάθεια — μόνο αν δεν κέρδισε ακόμα
# "not kerdisei" σημαίνει "αν ΔΕΝ έχει κερδίσει"
if not kerdisei:
    print("🎯 Προσπάθεια 2:")
    mandra = int(input("Γράψε τον αριθμό σου: "))
    prosp = 2

    if mandra == mystikoς_arithmos:
        kerdisei = True
    elif mandra < mystikoς_arithmos:
        print("📈 Μικρός! Δοκίμασε μεγαλύτερο.\n")
    else:
        print("📉 Μεγάλος! Δοκίμασε μικρότερο.\n")

# Η τρίτη και τελευταία προσπάθεια
if not kerdisei:
    print("🎯 Τελευταία προσπάθεια!")
    mandra = int(input("Γράψε τον αριθμό σου: "))
    prosp = 3

    if mandra == mystikoς_arithmos:
        kerdisei = True

# Τελικό αποτέλεσμα
print("\n" + "=" * 40)

# Ελέγχουμε αν κέρδισε ή έχασε
if kerdisei:
    # f-string με \n για κενή γραμμή πριν
    print(f"🎉 ΚΕΡΔΙΣΕΣ! Ο αριθμός ήταν {mystikoς_arithmos}!")
    print(f"Το βρήκες σε {prosp} προσπάθειες!")
else:
    print(f"😢 ΕΧΑΣΕΣ! Ο αριθμός ήταν {mystikoς_arithmos}!")
    print("Δοκίμασε ξανά!")

print("=" * 40)