# Στοιχεία χρήστη
onoma = "Nikos"
epileto = "Karagiannhs"
xronia_gennisis = 1995

# Δημιουργία username
# Παίρνουμε τα 3 πρώτα γράμματα από το όνομα και επίθετο
meros_onoma = onoma[:3]        # "Nik"
meros_epileto = epileto[:3]    # "Kar"

# Το χρόνο γέννησης τον κάνουμε κείμενο για να τον ενώσουμε
xronia_str = str(xronia_gennisis)  # "1995"
meros_xronia = xronia_str[2:]      # "95" (τα τελευταία 2 ψηφία)

# Ενώνουμε όλα μαζί και κάνουμε κεφαλαία
username = (meros_onoma + meros_epileto + meros_xronia).lower()

# Email
email = username + "@gmail.com"

# Αποτέλεσμα
print("=" * 35)
print("     USERNAME GENERATOR")
print("=" * 35)
print(f"Όνομα:    {onoma} {epileto}")
print(f"Username: {username}")
print(f"Email:    {email}")
print(f"Μήκος username: {len(username)} χαρακτήρες")
print("=" * 35)