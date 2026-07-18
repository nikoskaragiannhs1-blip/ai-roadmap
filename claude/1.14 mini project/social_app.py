# ============================================================
# ΜΑΘΗΜΑ 1.14 — MINI PROJECT ΦΑΣΗΣ 1
# Mini Social Media App — CLI (Command Line Interface)
# CLI = "Command Line Interface" = "Διεπαφή Γραμμής Εντολών"
# → εφαρμογή που τρέχει στο terminal, όχι σε παράθυρο
# ============================================================
#
# ΤΙ ΧΡΗΣΙΜΟΠΟΙΟΥΜΕ ΑΠΟ ΟΛΑ ΤΑ ΜΑΘΗΜΑΤΑ:
#
# ✅ 1.2  — Μεταβλητές & Τύποι     → αποθηκεύουμε δεδομένα χρηστών
# ✅ 1.3  — Τελεστές               → υπολογισμοί (likes, posts)
# ✅ 1.4  — Strings                → ονόματα, usernames, περιεχόμενο
# ✅ 1.5  — Λίστες                 → λίστες χρηστών και posts
# ✅ 1.6  — Dictionaries & Tuples  → δομή δεδομένων χρηστών
# ✅ 1.7  — Συνθήκες               → έλεγχοι (υπάρχει χρήστης;)
# ✅ 1.8  — Βρόχοι                 → μενού, αναζήτηση
# ✅ 1.9  — Συναρτήσεις            → οργάνωση κώδικα
# ✅ 1.10 — Error Handling         → ασφαλής είσοδος δεδομένων
# ✅ 1.11 — Αρχεία                 → αποθήκευση δεδομένων σε αρχείο
# ✅ 1.12 — Modules                → datetime για χρονοσφραγίδα
# ✅ 1.13 — OOP                    → κλάσεις User και Post
#
# ============================================================

# --------------------------------------------------
# IMPORTS — φορτώνουμε τα modules που χρειαζόμαστε
# --------------------------------------------------

# "import" = αγγλικά "εισαγωγή" (ξέρουμε από 1.12!)
# → φορτώνει έτοιμα εργαλεία

import datetime
# "datetime" = αγγλικά "ημερομηνία-ώρα" (ξέρουμε από 1.12!)
# → θα το χρησιμοποιήσουμε για να βάζουμε ημερομηνία στα posts

import os
# "os" = αγγλικά "operating system" = "λειτουργικό σύστημα"
# → εδώ το χρησιμοποιούμε για να ελέγχουμε αν υπάρχει αρχείο

import json
# "json" = αγγλικά "JavaScript Object Notation"
# → μορφή αποθήκευσης δεδομένων — μοιάζει με dictionary!
# → ΝΕΟΣ τρόπος αποθήκευσης που μαθαίνουμε εδώ
# → θα αποθηκεύουμε τους χρήστες σε αρχείο .json

# ============================================================
# ΚΛΑΣΗ POST (Ανάρτηση)
# ============================================================
# "class" = αγγλικά "κλάση" = το καλούπι (ξέρουμε από 1.13!)
# → ορίζουμε εδώ τι είναι ένα "post" (ανάρτηση)

class Post:
    # "Post" = αγγλικά "ανάρτηση/δημοσίευση"
    # → κάθε Post αντικείμενο = μία ανάρτηση στο social media

    def __init__(self, singrафeas, periexomeno):
        # "__init__" = "initialize" = αρχικοποίηση (ξέρουμε από 1.13!)
        # → τρέχει ΑΥΤΟΜΑΤΑ όταν φτιάχνουμε νέο Post
        # "self" = αγγλικά "εαυτός" → το ίδιο το αντικείμενο (ξέρουμε από 1.13!)

        self.singrафeas = singrафeas
        # → "singrафeas" = συγγραφέας — ποιος έγραψε το post

        self.periexomeno = periexomeno
        # → "periexomeno" = περιεχόμενο — τι γράφει το post

        self.likes = 0
        # → ξεκινάει με 0 likes
        # → "likes" = αγγλικά "αρέσει" — πόσοι έκαναν like

        self.xronos_dimosiefsis = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        # → "xronos_dimosiefsis" = χρόνος δημοσίευσης
        # → datetime.datetime.now() = τρέχουσα ώρα (ξέρουμε από 1.12!)
        # → .strftime("%d/%m/%Y %H:%M") = μορφοποίηση σε κείμενο
        # → αποτέλεσμα π.χ.: "12/07/2026 14:35"

        self.sxolia = []
        # → άδεια λίστα για σχόλια (ξέρουμε από 1.5!)
        # → "sxolia" = σχόλια

    def emfanise(self, arithmos):
        # "emfanise" = εμφάνισε
        # "arithmos" = παράμετρος — αύξων αριθμός του post
        print(f"\n   {'─'*40}")
        print(f"   📌 Post #{arithmos}")
        print(f"   👤 Από: @{self.singrафeas}")
        # → "self.singrафeas" = διαβάζει ιδιότητα (ξέρουμε από 1.13!)
        print(f"   🕐 {self.xronos_dimosiefsis}")
        print(f"   💬 {self.periexomeno}")
        print(f"   ❤️  Likes: {self.likes}")
        # → "self.likes" = τρέχων αριθμός likes

        if len(self.sxolia) > 0:
            # len() = αγγλικά "length" = πλήθος (ξέρουμε από 1.5!)
            print(f"   💭 Σχόλια ({len(self.sxolia)}):")
            for sxolio in self.sxolia:
                # "for" = αγγλικά "για" (ξέρουμε από 1.8!)
                # → περνάει από κάθε σχόλιο
                print(f"      → {sxolio}")

    def dose_like(self):
        # "dose_like" = δώσε like
        # "+=" = αγγλικά "plus equals" (ξέρουμε από 1.8!)
        # → αυξάνει τον αριθμό likes κατά 1
        self.likes += 1
        print(f"   ❤️  +1 like! Συνολικά: {self.likes} likes")

    def prosthese_sxolio(self, sxolio):
        # "prosthese_sxolio" = πρόσθεσε σχόλιο
        # .append() = αγγλικά "προσάρτηση" (ξέρουμε από 1.5!)
        # → προσθέτει σχόλιο στη λίστα
        self.sxolia.append(sxolio)
        print(f"   💭 Σχόλιο προστέθηκε!")

# ============================================================
# ΚΛΑΣΗ USER (Χρήστης)
# ============================================================
# "User" = αγγλικά "χρήστης"
# → κάθε User αντικείμενο = ένας χρήστης του social media

class User:

    def __init__(self, eponymia, username, email, ilikia):
        # "eponymia" = επωνυμία — πλήρες όνομα χρήστη
        # "username" = αγγλικά "όνομα χρήστη" — το @ του χρήστη
        # "email"    = αγγλικά "ηλεκτρονικό ταχυδρομείο"
        # "ilikia"   = ηλικία χρήστη

        self.eponymia = eponymia
        self.username = username
        self.email = email
        self.ilikia = ilikia

        self.akolouthoi = []
        # → "akolouthoi" = ακόλουθοι — λίστα usernames που τον ακολουθούν
        # → ξεκινάει άδεια

        self.akoloutho = []
        # → "akoloutho" = ακολουθώ — λίστα usernames που ακολουθεί

        self.anaртисeis = []
        # → "anaртисeis" = αναρτήσεις — λίστα Post αντικειμένων

        self.imera_egrafis = datetime.datetime.now().strftime("%d/%m/%Y")
        # → "imera_egrafis" = ημέρα εγγραφής — πότε δημιούργησε λογαριασμό

    def emfanise_profil(self):
        # "emfanise_profil" = εμφάνισε προφίλ
        print(f"\n   {'═'*40}")
        print(f"   👤 ΠΡΟΦΙΛ ΧΡΗΣΤΗ")
        print(f"   {'═'*40}")
        print(f"   Επωνυμία:    {self.eponymia}")
        print(f"   Username:    @{self.username}")
        print(f"   Email:       {self.email}")
        print(f"   Ηλικία:      {self.ilikia} χρόνια")
        print(f"   Εγγραφή:     {self.imera_egrafis}")
        print(f"   Posts:       {len(self.anaртисeis)}")
        print(f"   Ακόλουθοι:   {len(self.akolouthoi)}")
        print(f"   Ακολουθώ:    {len(self.akoloutho)}")
        print(f"   {'═'*40}")

    def dimiourgise_post(self, periexomeno):
        # "dimiourgise_post" = δημιούργησε post
        # → φτιάχνει νέο Post αντικείμενο (ξέρουμε από 1.13!)
        nea_anartisi = Post(self.username, periexomeno)
        # → Post(singrафeas, periexomeno) = νέο αντικείμενο Post

        self.anaртисeis.append(nea_anartisi)
        # → προσθέτει το post στη λίστα αναρτήσεων του χρήστη

        print(f"   ✅ Νέο post δημιουργήθηκε από @{self.username}!")
        return nea_anartisi
        # "return" = αγγλικά "επιστροφή" (ξέρουμε από 1.9!)
        # → επιστρέφει το post για να μπορούμε να το χρησιμοποιήσουμε

    def akolouthise(self, allos_xristis):
        # "akolouthise" = ακολούθησε
        # "allos_xristis" = άλλος χρήστης — παράμετρος User αντικείμενο

        if allos_xristis.username not in self.akoloutho:
            # "not in" = αγγλικά "δεν υπάρχει μέσα" (ξέρουμε από 1.5!)
            # → ελέγχει αν δεν τον ακολουθεί ήδη
            self.akoloutho.append(allos_xristis.username)
            allos_xristis.akolouthoi.append(self.username)
            print(f"   ✅ @{self.username} ακολούθησε τον @{allos_xristis.username}!")
        else:
            print(f"   ℹ️  Ακολουθείς ήδη τον @{allos_xristis.username}!")

# ============================================================
# ΚΛΑΣΗ SocialApp (Η κεντρική εφαρμογή)
# ============================================================
# "SocialApp" = η κεντρική κλάση που διαχειρίζεται τα πάντα
# → όπως η κλάση Zoo διαχειριζόταν τα ζώα (ξέρουμε από 1.13!)

class SocialApp:

    def __init__(self, titlos_app):
        # "titlos_app" = τίτλος εφαρμογής
        self.titlos_app = titlos_app
        self.xristes = {}
        # → "xristes" = dictionary (ξέρουμε από 1.6!)
        # → κλειδί = username, τιμή = User αντικείμενο
        # → π.χ.: {"nikos": User(...), "maria": User(...)}

        self.arxeio_dedomenon = "social_data.json"
        # → "arxeio_dedomenon" = αρχείο δεδομένων
        # → θα αποθηκεύουμε τους χρήστες εδώ

        self.fortose_dedomena()
        # → καλούμε αμέσως τη method φόρτωσης δεδομένων

    def fortose_dedomena(self):
        # "fortose_dedomena" = φόρτωσε δεδομένα
        # → φορτώνει χρήστες από αρχείο αν υπάρχει

        if os.path.exists(self.arxeio_dedomenon):
            # os.path.exists() = αγγλικά "ο δρόμος υπάρχει"
            # → ελέγχει αν υπάρχει το αρχείο στον υπολογιστή
            try:
                # "try" = αγγλικά "δοκίμασε" (ξέρουμε από 1.10!)
                with open(self.arxeio_dedomenon, "r", encoding="utf-8") as arxeio:
                    # "with open()" = άνοιξε αρχείο (ξέρουμε από 1.11!)
                    # "r" = αγγλικά "read" = "διάβασε"
                    stoixeia = json.load(arxeio)
                    # json.load() = φορτώνει JSON από αρχείο σε dictionary

                    for username, dedomena in stoixeia.items():
                        # .items() = αγγλικά "στοιχεία" (ξέρουμε από 1.6!)
                        # → δίνει ζεύγη κλειδί-τιμή από dictionary
                        xristis = User(
                            dedomena["eponymia"],
                            username,
                            dedomena["email"],
                            dedomena["ilikia"]
                        )
                        self.xristes[username] = xristis
                print(f"   ✅ Φορτώθηκαν {len(self.xristes)} χρήστες!")
            except Exception as paragogi_sfalmatos:
                # "Exception" = οποιοδήποτε σφάλμα (ξέρουμε από 1.10!)
                # "as paragogi_sfalmatos" = αποθηκεύει το μήνυμα σφάλματος
                print(f"   ⚠️  Σφάλμα φόρτωσης: {paragogi_sfalmatos}")

    def apothikeuse_dedomena(self):
        # "apothikeuse_dedomena" = αποθήκευσε δεδομένα
        # → αποθηκεύει τους χρήστες στο αρχείο JSON

        stoixeia_pros_apothikeusi = {}
        # → "stoixeia_pros_apothikeusi" = στοιχεία προς αποθήκευση
        # → νέο dictionary που θα γεμίσουμε

        for username, xristis in self.xristes.items():
            # → περνάει από κάθε χρήστη
            stoixeia_pros_apothikeusi[username] = {
                "eponymia": xristis.eponymia,
                "email": xristis.email,
                "ilikia": xristis.ilikia,
                "imera_egrafis": xristis.imera_egrafis
            }

        try:
            with open(self.arxeio_dedomenon, "w", encoding="utf-8") as arxeio:
                # "w" = αγγλικά "write" = "γράψε" (ξέρουμε από 1.11!)
                json.dump(stoixeia_pros_apothikeusi, arxeio, ensure_ascii=False, indent=2)
                # json.dump() = αποθηκεύει dictionary σε JSON αρχείο
                # "ensure_ascii=False" = αποθηκεύει ελληνικά σωστά
                # "indent=2" = κάνει το JSON ευανάγνωστο με 2 κενά
            print(f"   ✅ Δεδομένα αποθηκεύτηκαν!")
        except Exception as paragogi_sfalmatos:
            print(f"   ❌ Σφάλμα αποθήκευσης: {paragogi_sfalmatos}")

    def egrafи_xristi(self):
        # "egrafи_xristi" = εγγραφή χρήστη
        print(f"\n   {'─'*40}")
        print(f"   ➕ ΕΓΓΡΑΦΗ ΝΕΟΥ ΧΡΗΣΤΗ")
        print(f"   {'─'*40}")

        # input() = αγγλικά "είσοδος" → ζητάει κείμενο (ξέρουμε από 1.7!)
        eponymia = input("   Πλήρες όνομα: ")
        username = input("   Username (χωρίς @): ").lower()
        # .lower() = αγγλικά "μικρά" (ξέρουμε από 1.4!)
        # → κάνει το username πάντα με μικρά γράμματα

        if username in self.xristes:
            # "in" = αγγλικά "μέσα" → ελέγχει αν υπάρχει στο dictionary
            print(f"   ❌ Το username @{username} υπάρχει ήδη!")
            return
            # "return" χωρίς τιμή = σταμάτα τη συνάρτηση εδώ

        email = input("   Email: ")

        try:
            # "try" = δοκίμασε (ξέρουμε από 1.10!)
            arithmos_ilikias = int(input("   Ηλικία: "))
            # int() = αγγλικά "integer" = ακέραιος (ξέρουμε από 1.2!)
        except ValueError:
            # "ValueError" = λάθος τύπος τιμής (ξέρουμε από 1.10!)
            print("   ❌ Η ηλικία πρέπει να είναι αριθμός!")
            return

        νεος_χρηστης = User(eponymia, username, email, arithmos_ilikias)
        # → δημιουργούμε νέο User αντικείμενο (ξέρουμε από 1.13!)

        self.xristes[username] = νεος_χρηστης
        # → προσθέτουμε στο dictionary με κλειδί το username

        self.apothikeuse_dedomena()
        # → αποθηκεύουμε αμέσως στο αρχείο

        print(f"   ✅ Καλώς ήρθες @{username}!")

    def syndesi_xristi(self):
        # "syndesi_xristi" = σύνδεση χρήστη — login
        print(f"\n   {'─'*40}")
        print(f"   🔑 ΣΥΝΔΕΣΗ")
        print(f"   {'─'*40}")

        username = input("   Username: ").lower()

        if username not in self.xristes:
            # "not in" = δεν υπάρχει μέσα
            print(f"   ❌ Ο χρήστης @{username} δεν βρέθηκε!")
            return None
            # "None" = αγγλικά "τίποτα" → δεν βρέθηκε χρήστης

        sindedimenos = self.xristes[username]
        # → παίρνουμε το User αντικείμενο από το dictionary

        print(f"   ✅ Καλώς ήρθες @{sindedimenos.username}!")
        return sindedimenos
        # → επιστρέφουμε τον χρήστη που συνδέθηκε

    def emfanise_oles_anaртисeis(self):
        # "emfanise_oles_anaртисeis" = εμφάνισε όλες τις αναρτήσεις

        oles_anartiseis = []
        # → λίστα που θα μαζέψει ΟΛΕΣ τις αναρτήσεις

        for xristis in self.xristes.values():
            # .values() = αγγλικά "τιμές" (ξέρουμε από 1.6!)
            # → παίρνει μόνο τις τιμές του dictionary (τα User αντικείμενα)
            for anartisi in xristis.anaртисeis:
                oles_anartiseis.append(anartisi)

        if len(oles_anartiseis) == 0:
            print("\n   ℹ️  Δεν υπάρχουν αναρτήσεις ακόμα!")
            return

        print(f"\n   📰 ΟΛΑ ΤΑ POSTS ({len(oles_anartiseis)} συνολικά):")

        for thesi, anartisi in enumerate(oles_anartiseis):
            # enumerate() = αγγλικά "απαρίθμηση" (ξέρουμε από 1.5!)
            # → δίνει αριθμό + στοιχείο μαζί
            anartisi.emfanise(thesi + 1)
            # → καλούμε τη method emfanise() του Post (ξέρουμε από 1.13!)

    def emfanise_xristes(self):
        # "emfanise_xristes" = εμφάνισε χρήστες
        if len(self.xristes) == 0:
            print("\n   ℹ️  Δεν υπάρχουν χρήστες ακόμα!")
            return

        print(f"\n   👥 ΧΡΗΣΤΕΣ ({len(self.xristes)} συνολικά):")
        print(f"   {'─'*40}")

        for username, xristis in self.xristes.items():
            print(f"   @{username} — {xristis.eponymia} | "
                  f"Posts: {len(xristis.anaртисeis)} | "
                  f"Ακόλουθοι: {len(xristis.akolouthoi)}")

# ============================================================
# ΚΥΡΙΟ ΠΡΟΓΡΑΜΜΑ — ΜΕΝΟΥ ΕΦΑΡΜΟΓΗΣ
# ============================================================

# Δημιουργούμε την εφαρμογή
# → SocialApp("τίτλος") = νέο αντικείμενο (ξέρουμε από 1.13!)
efarmogi = SocialApp("PyGram")

sindedimenos_xristis = None
# → "sindedimenos_xristis" = ο χρήστης που είναι συνδεδεμένος αυτή τη στιγμή
# → None = κανείς δεν είναι συνδεδεμένος αρχικά

print("=" * 45)
print("   🐍 PyGram — Mini Social Media App")
print("   Μάθημα 1.14 — Τελικό Project Φάσης 1")
print("=" * 45)

# while True = βρόχος που τρέχει για πάντα (ξέρουμε από 1.8!)
# → σταματάει μόνο με break
while True:
    print(f"\n{'═'*45}")

    # if/else = (ξέρουμε από 1.7!) → διαφορετικό μενού ανάλογα αν είναι συνδεδεμένος
    if sindedimenos_xristis:
        # → αν κάποιος είναι συνδεδεμένος
        print(f"   📱 PyGram | @{sindedimenos_xristis.username}")
        print(f"{'═'*45}")
        print("   1. 📝 Δημιούργησε Post")
        print("   2. 📰 Δες όλα τα Posts")
        print("   3. 👤 Δες το Προφίλ σου")
        print("   4. 👥 Δες όλους τους Χρήστες")
        print("   5. 🤝 Ακολούθησε χρήστη")
        print("   6. ❤️  Κάνε Like σε Post")
        print("   7. 💭 Σχολίασε Post")
        print("   8. 🚪 Αποσύνδεση")
        print("   0. ❌ Έξοδος")
    else:
        # → αν κανείς δεν είναι συνδεδεμένος
        print(f"   📱 PyGram — Καλώς ήρθες!")
        print(f"{'═'*45}")
        print("   1. 🔑 Σύνδεση")
        print("   2. ➕ Εγγραφή")
        print("   3. 👥 Δες όλους τους Χρήστες")
        print("   4. 📰 Δες όλα τα Posts")
        print("   0. ❌ Έξοδος")

    print(f"{'═'*45}")
    epilogi = input("   Επιλογή: ")
    # → input() = ζητάει είσοδο από χρήστη

    # ---- ΜΕΝΟΥ ΧΩΡΙΣ ΣΥΝΔΕΣΗ ----
    if not sindedimenos_xristis:
        # "not" = αγγλικά "όχι" → αν ΔΕΝ είναι συνδεδεμένος

        if epilogi == "0":
            print("\n   👋 Αντίο! Επέστρεψε σύντομα!")
            break
            # "break" = αγγλικά "σπάσιμο" → σταματάει τον while loop

        elif epilogi == "1":
            sindedimenos_xristis = efarmogi.syndesi_xristi()

        elif epilogi == "2":
            efarmogi.egrafи_xristi()

        elif epilogi == "3":
            efarmogi.emfanise_xristes()

        elif epilogi == "4":
            efarmogi.emfanise_oles_anaртисeis()

        else:
            print("   ❌ Λάθος επιλογή!")

    # ---- ΜΕΝΟΥ ΜΕ ΣΥΝΔΕΣΗ ----
    else:

        if epilogi == "0":
            print("\n   👋 Αντίο! Επέστρεψε σύντομα!")
            break

        elif epilogi == "1":
            # Δημιουργία Post
            print(f"\n   {'─'*40}")
            print(f"   📝 ΝΕΟ POST")
            periexomeno_post = input("   Τι σκέφτεσαι; ")
            # → ζητάει το περιεχόμενο του post
            sindedimenos_xristis.dimiourgise_post(periexomeno_post)
            # → καλεί τη method του User αντικειμένου (ξέρουμε από 1.13!)

        elif epilogi == "2":
            efarmogi.emfanise_oles_anaртисeis()

        elif epilogi == "3":
            sindedimenos_xristis.emfanise_profil()

        elif epilogi == "4":
            efarmogi.emfanise_xristes()

        elif epilogi == "5":
            # Ακολούθηση χρήστη
            stohos_username = input("   Username χρήστη που θες να ακολουθήσεις: ").lower()
            # → "stohos_username" = στόχος username — ποιον θέλει να ακολουθήσει

            if stohos_username in efarmogi.xristes:
                stohos_xristis = efarmogi.xristes[stohos_username]
                # → παίρνουμε το User αντικείμενο από το dictionary
                sindedimenos_xristis.akolouthise(stohos_xristis)
            else:
                print(f"   ❌ Ο χρήστης @{stohos_username} δεν βρέθηκε!")

        elif epilogi == "6":
            # Like σε post
            efarmogi.emfanise_oles_anaртисeis()

            try:
                arithmos_post = int(input("\n   Αριθμός post για like: ")) - 1
                # → "-1" γιατί εμφανίζουμε από 1 αλλά η λίστα μετράει από 0

                oles = []
                for xr in efarmogi.xristes.values():
                    for an in xr.anaртисeis:
                        oles.append(an)
                # → μαζεύουμε ΟΛΕΣ τις αναρτήσεις σε μία λίστα

                if 0 <= arithmos_post < len(oles):
                    # → ελέγχουμε αν ο αριθμός είναι έγκυρος
                    oles[arithmos_post].dose_like()
                    # → καλούμε τη method dose_like() του Post
                else:
                    print("   ❌ Λάθος αριθμός post!")
            except ValueError:
                print("   ❌ Γράψε αριθμό!")

        elif epilogi == "7":
            # Σχόλιο σε post
            efarmogi.emfanise_oles_anaртисeis()

            try:
                arithmos_post = int(input("\n   Αριθμός post για σχόλιο: ")) - 1

                oles = []
                for xr in efarmogi.xristes.values():
                    for an in xr.anaртисeis:
                        oles.append(an)

                if 0 <= arithmos_post < len(oles):
                    periexomeno_sxoliou = input("   Γράψε το σχόλιό σου: ")
                    # → "periexomeno_sxoliou" = περιεχόμενο σχολίου
                    sxolio_me_username = f"@{sindedimenos_xristis.username}: {periexomeno_sxoliou}"
                    # → προσθέτουμε το @ του χρήστη μπροστά
                    oles[arithmos_post].prosthese_sxolio(sxolio_me_username)
                else:
                    print("   ❌ Λάθος αριθμός post!")
            except ValueError:
                print("   ❌ Γράψε αριθμό!")

        elif epilogi == "8":
            # Αποσύνδεση
            print(f"   👋 Αποσυνδέθηκες @{sindedimenos_xristis.username}!")
            sindedimenos_xristis = None
            # → None = κανείς δεν είναι συνδεδεμένος πλέον

        else:
            print("   ❌ Λάθος επιλογή!")

print("=" * 45)
print("   🏆 ΦΑΣΗ 1 ΟΛΟΚΛΗΡΩΘΗΚΕ! Συγχαρητήρια!")
print("=" * 45)
