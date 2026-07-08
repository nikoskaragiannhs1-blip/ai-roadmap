# ============================================
# ΓΕΩΜΕΤΡΙΚΟΣ ΥΠΟΛΟΓΙΣΤΗΣ v2.0 - Μάθημα 1.9
# ============================================

import math

# ---- ΣΥΝΑΡΤΗΣΕΙΣ ----

def emvado_tetragono(pleura):
    return pleura ** 2

def emvado_orthogonio(mikos, platos):
    return mikos * platos

def emvado_kyklos(aktina):
    return round(math.pi * aktina ** 2, 2)

perim_tetragono = lambda x: x * 4

def perimetros_polygono(*plevres):
    return sum(plevres)

# ---- ΚΥΡΙΟ ΠΡΟΓΡΑΜΜΑ ----

print("=" * 40)
print("    ΓΕΩΜΕΤΡΙΚΟΣ ΥΠΟΛΟΓΙΣΤΗΣ ⬡")
print("=" * 40)

# WHILE LOOP — συνεχίζει μέχρι ο χρήστης να πει "exit"
# True σημαίνει "τρέχε για πάντα" — σταματάει μόνο με break
while True:

    # Εκτυπώνουμε το μενού επιλογών
    print("\nΤι θέλεις να υπολογίσεις;")
    print("  1. Εμβαδό Τετραγώνου")
    print("  2. Εμβαδό Ορθογωνίου")
    print("  3. Εμβαδό Κύκλου")
    print("  4. Περίμετρος Τετραγώνου")
    print("  5. Περίμετρος Πολυγώνου")
    print("  0. Έξοδος")
    print("-" * 40)

    # Ζητάμε επιλογή από τον χρήστη
    # Το αφήνουμε string (χωρίς int) για να ελέγξουμε αν έγραψε "0"
    epilogi = input("Γράψε αριθμό επιλογής: ")

    # Αν γράψει 0, σταματάμε τον βρόχο
    # break = "σπάσε" τον βρόχο και βγες έξω
    if epilogi == "0":
        print("\n👋 Αντίο!")
        break

    # Επιλογή 1 — Εμβαδό Τετραγώνου
    elif epilogi == "1":
        # float() γιατί μπορεί να δώσει δεκαδικό
        pleura = float(input("Δώσε πλευρά: "))
        apotelesma = emvado_tetragono(pleura)
        print(f"✅ Εμβαδό Τετραγώνου: {apotelesma}")

    # Επιλογή 2 — Εμβαδό Ορθογωνίου
    elif epilogi == "2":
        mikos = float(input("Δώσε μήκος: "))
        platos = float(input("Δώσε πλάτος: "))
        apotelesma = emvado_orthogonio(mikos, platos)
        print(f"✅ Εμβαδό Ορθογωνίου: {apotelesma}")

    # Επιλογή 3 — Εμβαδό Κύκλου
    elif epilogi == "3":
        aktina = float(input("Δώσε ακτίνα: "))
        apotelesma = emvado_kyklos(aktina)
        print(f"✅ Εμβαδό Κύκλου: {apotelesma}")

    # Επιλογή 4 — Περίμετρος Τετραγώνου
    elif epilogi == "4":
        pleura = float(input("Δώσε πλευρά: "))
        # Καλούμε την lambda συνάρτηση
        apotelesma = perim_tetragono(pleura)
        print(f"✅ Περίμετρος Τετραγώνου: {apotelesma}")

    # Επιλογή 5 — Περίμετρος Πολυγώνου
    elif epilogi == "5":
        # Ρωτάμε πόσες πλευρές έχει το πολύγωνο
        arithmos_plevron = int(input("Πόσες πλευρές έχει; "))

        # Λίστα για να μαζεύουμε τις πλευρές
        plevres = []

        # for loop — ζητάει κάθε πλευρά ξεχωριστά
        # range(1, arithmos_plevron+1) → 1, 2, 3... μέχρι τον αριθμό πλευρών
        for i in range(1, arithmos_plevron + 1):
            pleura = float(input(f"  Πλευρά {i}: "))
            plevres.append(pleura)

        # *plevres "ξεπακετάρει" τη λίστα σε ξεχωριστές τιμές
        # Νέο σύμβολο: *λίστα μέσα σε κλήση συνάρτησης
        # σημαίνει "πέρνα κάθε στοιχείο ξεχωριστά"
        apotelesma = perimetros_polygono(*plevres)
        print(f"✅ Περίμετρος Πολυγώνου: {apotelesma}")

    # Αν έγραψε κάτι άλλο εκτός από 0-5
    else:
        print("❌ Λάθος επιλογή! Γράψε αριθμό από 0 έως 5.")

print("=" * 40)