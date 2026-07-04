# ============================================
# MINI PHONEBOOK - Μάθημα 1.6
# ============================================

# Δημιουργούμε την πρώτη επαφή σαν dictionary
# Το dictionary έχει "κλειδί": "τιμή"
# Π.χ. "onoma" είναι το κλειδί, "Nikos Karagiannhs" είναι η τιμή
epafi1 = {
    "onoma": "Nikos Karagiannhs",      # το όνομα της επαφής
    "tilefono": "6912345678",           # το τηλέφωνο
    "email": "nikos@gmail.com",         # το email
    "poli": "Aigio"                     # η πόλη
}

# Δεύτερη επαφή — ίδια δομή, διαφορετικά στοιχεία
epafi2 = {
    "onoma": "Kostas Papadopoulos",
    "tilefono": "6987654321",
    "email": "kostas@gmail.com",
    "poli": "Athina"
}

# Τρίτη επαφή
epafi3 = {
    "onoma": "Maria Nikolaou",
    "tilefono": "6945678123",
    "email": "maria@gmail.com",
    "poli": "Patra"
}

# Βάζουμε όλες τις επαφές σε μια ΛΙΣΤΑ
# Λίστα από dictionaries = έτσι φτιάχνονται οι βάσεις δεδομένων!
phonebook = [epafi1, epafi2, epafi3]

# TUPLE — σταθερά στοιχεία της εφαρμογής που ΔΕΝ αλλάζουν ποτέ
# Χρησιμοποιούμε () αντί για [] ακριβώς γι' αυτό
stoixeia_app = ("Mini Phonebook", "v1.0", "2026")

# Εκτυπώνουμε τίτλο
# "=" * 40 σημαίνει εκτύπωσε 40 φορές το "="
print("=" * 40)

# stoixeia_app[0] = "Mini Phonebook" (το πρώτο στοιχείο του tuple)
# stoixeia_app[1] = "v1.0"
# stoixeia_app[2] = "2026"
print(f"  {stoixeia_app[0]} {stoixeia_app[1]} ({stoixeia_app[2]})")

print("=" * 40)

# len(phonebook) μετράει πόσες επαφές έχουμε
print(f"📋 Σύνολο επαφών: {len(phonebook)}\n")

# Ο βρόχος for περνάει από ΚΑΘΕ επαφή μία-μία
# Σε κάθε επανάληψη το "epafi" γίνεται η επόμενη επαφή
for epafi in phonebook:

    # epafi['onoma'] διαβάζει την τιμή του κλειδιού 'onoma'
    print(f"👤 {epafi['onoma']}")

    # Ίδιο για τηλέφωνο, email, πόλη
    print(f"   📞 {epafi['tilefono']}")
    print(f"   📧 {epafi['email']}")
    print(f"   📍 {epafi['poli']}")

    # Κενή γραμμή μεταξύ επαφών για να φαίνεται καλύτερα
    print()

# Δημιουργούμε νέα επαφή για να την προσθέσουμε
nea_epafi = {
    "onoma": "Giorgos Dimitriou",
    "tilefono": "6911223344",
    "email":"@@@@@@@@" }