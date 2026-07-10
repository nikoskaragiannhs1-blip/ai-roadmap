# ============================================
# WORD COUNTER - Μάθημα 1.11
# ============================================

# os module — εργαλεία για το λειτουργικό σύστημα
# Το χρησιμοποιούμε για να ελέγξουμε αν υπάρχει αρχείο
import os

# Συνάρτηση που διαβάζει αρχείο με ασφάλεια
def diabase_arxeio(onoma_arxeiou):
    try:
        # encoding="utf-8" = διαβάζει ελληνικά σωστά
        with open(onoma_arxeiou, "r", encoding="utf-8") as f:
            # .read() διαβάζει ΟΛΟ το αρχείο σε ένα string
            return f.read()
    except FileNotFoundError:
        # FileNotFoundError = το αρχείο δεν υπάρχει
        print(f"❌ Το αρχείο '{onoma_arxeiou}' δεν βρέθηκε!")
        return None

# Συνάρτηση που μετράει στατιστικά κειμένου
def metrise_statistika(keimeno):
    # .split() κόβει το κείμενο σε λίστα λέξεων
    # Νέο σύμβολο: .split() = "κόψε στα κενά"
    # "Γεια σου Νίκο".split() = ["Γεια", "σου", "Νίκο"]
    lexeis = keimeno.split()

    # .splitlines() κόβει σε γραμμές
    # Νέο σύμβολο: .splitlines() = "κόψε στις αλλαγές γραμμής"
    grammes = keimeno.splitlines()

    # len() μετράει στοιχεία (το ξέρουμε από 1.5)
    arithmos_lexeon = len(lexeis)
    arithmos_grammon = len(grammes)
    arithmos_xarakteron = len(keimeno)

    # Επιστρέφουμε dictionary με όλα τα στατιστικά
    return {
        "lexeis": arithmos_lexeon,
        "grammes": arithmos_grammon,
        "xaraktires": arithmos_xarakteron,
        "lista_lexeon": lexeis
    }

# Συνάρτηση που βρίσκει τις πιο συχνές λέξεις
def syhnes_lexeis(lista_lexeon, top=5):
    # Dictionary για να μετράμε πόσες φορές εμφανίζεται κάθε λέξη
    metrima = {}

    for lexi in lista_lexeon:
        # .lower() κάνει μικρά γράμματα για να μην μετράμε
        # "Python" και "python" ξεχωριστά
        lexi = lexi.lower()

        # Αν η λέξη υπάρχει ήδη, αύξησε τον μετρητή
        if lexi in metrima:
            metrima[lexi] += 1
        # Αν δεν υπάρχει, πρόσθεσέ την με τιμή 1
        else:
            metrima[lexi] = 1

    # sorted() ταξινομεί — key=lambda x: x[1] ταξινομεί κατά τιμή
    # reverse=True = από το μεγαλύτερο στο μικρότερο
    # Νέο σύμβολο: sorted(..., key=lambda x: x[1], reverse=True)
    # = "ταξινόμησε κατά τη δεύτερη τιμή, φθίνουσα σειρά"
    taksinomimeno = sorted(metrima.items(), key=lambda x: x[1], reverse=True)

    # Επιστρέφουμε μόνο τις top λέξεις
    # [:top] παίρνει τα πρώτα "top" στοιχεία
    return taksinomimeno[:top]

# Συνάρτηση που αποθηκεύει αποτελέσματα σε νέο αρχείο
def apothikeuse_apotelesmata(stoixeia, syhnes):
    # "w" = write — δημιουργεί νέο αρχείο ή αντικαθιστά παλιό
    with open("apotelesmata.txt", "w", encoding="utf-8") as f:
        f.write("=" * 40 + "\n")
        f.write("ΑΠΟΤΕΛΕΣΜΑΤΑ WORD COUNTER\n")
        f.write("=" * 40 + "\n")
        f.write(f"Λέξεις: {stoixeia['lexeis']}\n")
        f.write(f"Γραμμές: {stoixeia['grammes']}\n")
        f.write(f"Χαρακτήρες: {stoixeia['xaraktires']}\n")
        f.write("\nΠιο συχνές λέξεις:\n")
        for lexi, fois in syhnes:
            # \t = tab (στοίχιση) — Νέο σύμβολο: \t = οριζόντιο κενό
            f.write(f"  {lexi}\t→ {fois} φορές\n")
    print("✅ Αποτελέσματα αποθηκεύτηκαν στο 'apotelesmata.txt'!")

# ---- ΚΥΡΙΟ ΠΡΟΓΡΑΜΜΑ ----

print("=" * 40)
print("        WORD COUNTER 📝")
print("=" * 40)

# Διαβάζουμε το αρχείο
keimeno = diabase_arxeio("keimeno.txt")

# Αν το αρχείο βρέθηκε (δεν είναι None)
if keimeno:
    # Υπολογίζουμε στατιστικά
    stoixeia = metrise_statistika(keimeno)

    # Εκτυπώνουμε αποτελέσματα
    print(f"\n📊 Στατιστικά αρχείου:")
    print(f"   📝 Λέξεις:      {stoixeia['lexeis']}")
    print(f"   📄 Γραμμές:     {stoixeia['grammes']}")
    print(f"   🔤 Χαρακτήρες: {stoixeia['xaraktires']}")

    # Βρίσκουμε τις 5 πιο συχνές λέξεις
    syhnes = syhnes_lexeis(stoixeia["lista_lexeon"], top=5)
    print(f"\n🔝 Top 5 πιο συχνές λέξεις:")
    for lexi, fois in syhnes:
        print(f"   '{lexi}' → {fois} φορές")

    # Αποθηκεύουμε αποτελέσματα
    apothikeuse_apotelesmata(stoixeia, syhnes)

print("=" * 40) 