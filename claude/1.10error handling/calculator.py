# ============================================
# ΑΣΦΑΛΗΣ CALCULATOR - Μάθημα 1.10
# ============================================

# Συνάρτηση που ζητάει αριθμό με ασφάλεια
# Αν ο χρήστης γράψει γράμματα, ξαναρωτάει
def zitise_arithmo(minima):
    # while True = συνέχισε μέχρι να πάρουμε σωστό αριθμό
    while True:
        try:
            # Προσπαθούμε να μετατρέψουμε σε float
            arithmos = float(input(minima))
            # Αν φτάσουμε εδώ, πήγε καλά — επιστρέφουμε τον αριθμό
            return arithmos
        except ValueError:
            # ValueError = ο χρήστης έγραψε γράμματα
            # Αντί να κρασάρουμε, εκτυπώνουμε μήνυμα και ξαναρωτάμε
            print("❌ Λάθος! Γράψε αριθμό, όχι γράμματα.")

# Συνάρτηση πρόσθεσης
def prosthesi(a, b):
    return a + b

# Συνάρτηση αφαίρεσης
def afairesi(a, b):
    return a - b

# Συνάρτηση πολλαπλασιασμού
def pollaplasiasmος(a, b):
    return a * b

# Συνάρτηση διαίρεσης — με έλεγχο για διαίρεση με μηδέν
def diairesi(a, b):
    # Ελέγχουμε αν το b είναι μηδέν ΠΡΙΝ διαιρέσουμε
    if b == 0:
        # raise = δημιουργούμε δικό μας error με μήνυμα
        raise ValueError("❌ Δεν μπορείς να διαιρέσεις με το 0!")
    return a / b

# Συνάρτηση ύψωσης σε δύναμη
def dynamis(a, b):
    # ** = ύψωση σε δύναμη (το ξέρουμε από 1.3)
    return a ** b

# ---- ΚΥΡΙΟ ΠΡΟΓΡΑΜΜΑ ----

print("=" * 40)
print("      ΑΣΦΑΛΗΣ CALCULATOR 🧮")
print("=" * 40)

# while True = το μενού επαναλαμβάνεται συνέχεια
while True:

    # Μενού επιλογών
    print("\nΕπιλογές:")
    print("  1. Πρόσθεση (+)")
    print("  2. Αφαίρεση (-)")
    print("  3. Πολλαπλασιασμός (*)")
    print("  4. Διαίρεση (/)")
    print("  5. Δύναμη (**)")
    print("  0. Έξοδος")
    print("-" * 40)

    epilogi = input("Επιλογή: ")

    # Αν επιλέξει 0, βγαίνουμε
    if epilogi == "0":
        print("\n👋 Αντίο!")
        break

    # Αν επιλέξει 1-5, ζητάμε αριθμούς
    elif epilogi in ["1", "2", "3", "4", "5"]:
        # in ["1","2"...] = ελέγχει αν η επιλογή υπάρχει στη λίστα
        # Νέο σύμβολο: "x" in [λίστα] = "υπάρχει το x στη λίστα;"

        # Καλούμε την ασφαλή συνάρτηση για κάθε αριθμό
        a = zitise_arithmo("Δώσε πρώτο αριθμό: ")
        b = zitise_arithmo("Δώσε δεύτερο αριθμό: ")

        # try/except γύρω από την πράξη
        # γιατί η διαίρεση μπορεί να κάνει raise ValueError
        try:
            if epilogi == "1":
                apotelesma = prosthesi(a, b)
                praxi = "+"
            elif epilogi == "2":
                apotelesma = afairesi(a, b)
                praxi = "-"
            elif epilogi == "3":
                apotelesma = pollaplasiasmος(a, b)
                praxi = "*"
            elif epilogi == "4":
                # Αυτή μπορεί να κάνει raise αν b==0
                apotelesma = diairesi(a, b)
                praxi = "/"
            elif epilogi == "5":
                apotelesma = dynamis(a, b)
                praxi = "**"

            # round() στρογγυλοποιεί στα 4 δεκαδικά
            print(f"\n✅ {a} {praxi} {b} = {round(apotelesma, 4)}")

        except ValueError as e:
            # "as e" αποθηκεύει το μήνυμα του error σε μεταβλητή e
            # Νέο σύμβολο: "except TypeError as e" = πιάσε το error και αποθήκευσέ το
            print(f"\n{e}")

        finally:
            # Τρέχει ΠΑΝΤΑ μετά από κάθε πράξη
            print("-" * 40)

    else:
        print("❌ Λάθος επιλογή! Γράψε αριθμό από 0 έως 5.")