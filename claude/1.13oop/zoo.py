# ============================================================
# ΜΑΘΗΜΑ 1.13 — OOP (Object Oriented Programming)
#               Αντικειμενοστραφής Προγραμματισμός
# ============================================================
#
# ΤΙ ΘΑ ΜΑΘΟΥΜΕ ΣΗΜΕΡΑ:
#
# OOP = "Object Oriented Programming"
#     = "Αντικειμενοστραφής Προγραμματισμός"
#     → τρόπος οργάνωσης κώδικα με "αντικείμενα"
#     → κάθε αντικείμενο έχει ΧΑΡΑΚΤΗΡΙΣΤΙΚΑ και ΔΥΝΑΤΟΤΗΤΕΣ
#
# Παράδειγμα από την πραγματικότητα:
# Ένα ΣΚΥΛί έχει:
#   ΧΑΡΑΚΤΗΡΙΣΤΙΚΑ: όνομα, ράτσα, ηλικία
#   ΔΥΝΑΤΟΤΗΤΕΣ:    γαυγίζει, τρέχει, κοιμάται
#
# Στην Python:
#   ΧΑΡΑΚΤΗΡΙΣΤΙΚΑ = "attributes" = αγγλικά "ιδιότητες"
#   ΔΥΝΑΤΟΤΗΤΕΣ    = "methods"    = αγγλικά "μέθοδοι" (συναρτήσεις μέσα σε class)
#
# ΕΝΝΟΙΕΣ ΠΟΥ ΘΑ ΜΑΘΟΥΜΕ:
# 1. class      = αγγλικά "κλάση/τάξη" → το "καλούπι" για αντικείμενα
# 2. object     = αγγλικά "αντικείμενο" → το "προϊόν" του καλουπιού
# 3. __init__   = αγγλικά "initialize" = "αρχικοποίηση" → constructor
# 4. self       = αγγλικά "εαυτός" → αναφέρεται στο ίδιο το αντικείμενο
# 5. inheritance= αγγλικά "κληρονομικότητα" → παιδί κλάσης παίρνει ό,τι έχει η μητρική
#
# ============================================================

# ============================================================
# ΒΗΜΑ 1: Η ΒΑΣΙΚΗ ΚΛΑΣΗ (BASE CLASS)
# ============================================================
#
# "class" = αγγλικά "κλάση/τάξη"
# → είναι το ΚΑΛΟΥΠΙ από το οποίο φτιάχνουμε αντικείμενα
# → φαντάσου ότι είναι η "συνταγή" και τα αντικείμενα είναι τα "πιάτα"
#
# "Animal" = αγγλικά "ζώο"
# → το όνομα της κλάσης — συνήθως ξεκινάει με ΚΕΦΑΛΑΙΟ
#
# Η δομή είναι:
# class ΌνομαΚλάσης:
#     def __init__(self, παράμετρος1, παράμετρος2):
#         self.ιδιότητα = παράμετρος

class Animal:
    # __init__ = "dunder init" (double underscore init)
    # "initialize" = αγγλικά "αρχικοποίηση"
    # → ΑΥΤΟΜΑΤΑ καλείται όταν φτιάχνουμε νέο αντικείμενο
    # → είναι σαν το "setup" του αντικειμένου
    # → ορίζουμε εδώ τι χαρακτηριστικά έχει κάθε ζώο
    #
    # "self" = αγγλικά "εαυτός"
    # → αναφέρεται στο ΙΔΙΟ το αντικείμενο που δημιουργείται
    # → ΠΑΝΤΑ είναι η πρώτη παράμετρος σε κάθε method!
    # → η Python το περνάει αυτόματα — εμείς δεν το γράφουμε όταν καλούμε
    def __init__(self, onoma, idos, ilikia, varo):
        # self.onoma = δημιουργούμε ΙΔΙΟΤΗΤΑ (attribute) με όνομα "onoma"
        # → το "self." μπροστά σημαίνει "αυτό το αντικείμενο έχει..."
        # → έτσι κάθε ζώο θυμάται το δικό του όνομα
        self.onoma = onoma      # όνομα του ζώου
        self.idos = idos        # είδος (π.χ. "Λιοντάρι")
        self.ilikia = ilikia    # ηλικία σε χρόνια
        self.varo = varo        # βάρος σε κιλά
        self.einai_xortato = False
        # → False = αγγλικά "ψευδές" (ξέρουμε από 1.2!)
        # → ξεκινάει πεινασμένο — False σημαίνει "δεν είναι χορτάτο"

    # --------------------------------------------------
    # METHODS (Μέθοδοι) = συναρτήσεις μέσα σε class
    # --------------------------------------------------
    # "method" = αγγλικά "μέθοδος"
    # → είναι απλά συνάρτηση (def) μέσα σε κλάση
    # → ΠΑΝΤΑ έχει "self" ως πρώτη παράμετρο
    # → καλείται με: αντικείμενο.method()

    def perigrafi(self):
        # "perigrafi" = περιγραφή
        # → εκτυπώνει τα στοιχεία του ζώου
        # f-string = (ξέρουμε από 1.4!) βάζει μεταβλητές σε κείμενο
        # self.onoma = διαβάζει την ιδιότητα "onoma" αυτού του αντικειμένου
        print(f"\n🐾 Στοιχεία ζώου:")
        print(f"   Όνομα:   {self.onoma}")
        print(f"   Είδος:   {self.idos}")
        print(f"   Ηλικία:  {self.ilikia} χρόνια")
        print(f"   Βάρος:   {self.varo} κιλά")

        # if/else = (ξέρουμε από 1.7!)
        # → ελέγχουμε αν είναι χορτάτο
        if self.einai_xortato:
            print(f"   Κατάσταση: Χορτάτο ✅")
        else:
            print(f"   Κατάσταση: Πεινασμένο 🍖")

    def taisi(self, trofi):
        # "taisi" = ταΐσι
        # "trofi" = παράμετρος = τι φαγητό δίνουμε
        print(f"   🍖 {self.onoma} τρώει {trofi}!")
        # self.einai_xortato = True → αλλάζουμε την ιδιότητα
        # True = αγγλικά "αληθές" (ξέρουμε από 1.2!)
        self.einai_xortato = True

    def foni(self):
        # "foni" = φωνή
        # → BASE method που θα ΑΝΤΙΚΑΤΑΣΤΗΣΟΥΝ τα παιδιά
        # → "base" = αγγλικά "βάση" → η βασική έκδοση
        print(f"   🔊 {self.onoma} κάνει κάποιο ήχο...")

    def xaraktires(self):
        # Επιστρέφει dictionary (ξέρουμε από 1.6!) με στοιχεία
        # return = αγγλικά "επιστροφή" (ξέρουμε από 1.9!)
        return {
            "onoma": self.onoma,
            "idos": self.idos,
            "ilikia": self.ilikia,
            "varo": self.varo
        }

# ============================================================
# ΒΗΜΑ 2: ΚΛΗΡΟΝΟΜΙΚΟΤΗΤΑ (INHERITANCE)
# ============================================================
#
# "inheritance" = αγγλικά "κληρονομικότητα"
# → η "παιδί" κλάση παίρνει ΟΛΑ τα χαρακτηριστικά της "γονέα"
# → και μπορεί να προσθέσει ΔΙΚΑ ΤΗΣ ή να ΑΛΛΑΞΕΙ παλιά
#
# Δομή: class ΠαιδίΚλάση(ΓονέαςΚλάση):
#
# Παράδειγμα: Το Lion (Λιοντάρι) ΕΙΝΑΙ Animal (Ζώο)
#             → παίρνει ό,τι έχει το Animal
#             → αλλά έχει και δικά του χαρακτηριστικά

class Lion(Animal):
    # "Lion" = αγγλικά "λιοντάρι"
    # "(Animal)" = κληρονομεί από την κλάση Animal
    # → το Lion ΕΙΝΑΙ Animal, οπότε έχει ό,τι έχει το Animal!

    def __init__(self, onoma, ilikia, varo, einai_vasiliasv):
        # "super()" = αγγλικά "super/ανώτερος"
        # → καλεί τον __init__ της ΓΟΝΕΑ κλάσης (Animal)
        # → έτσι δεν ξαναγράφουμε τον ίδιο κώδικα!
        # → "super" = ο "γονέας" στον κώδικα
        super().__init__(onoma, "Λιοντάρι", ilikia, varo)

        # Προσθέτουμε ΔΙΚΗ ΜΑΣ ιδιότητα που δεν έχει το Animal
        self.einai_vasilias = einai_vasiliasv
        # → True/False αν είναι ο "βασιλιάς" της αγέλης

    def foni(self):
        # OVERRIDE = αγγλικά "αντικατάσταση/υπερκάλυψη"
        # → ΑΝΤΙΚΑΘΙΣΤΟΥΜΕ τη method foni() του Animal
        # → το Lion έχει ΔΙΚΗ ΤΟΥ φωνή!
        print(f"   🦁 {self.onoma} ΡΟΥΓΚΑΝΙΖΕΙ δυνατά!")

    def perigrafi(self):
        # Καλούμε ΠΡΩΤΑ την perigrafi() του Animal με super()
        # → έτσι εκτυπώνει τα βασικά στοιχεία
        super().perigrafi()
        # Μετά προσθέτουμε τη ΔΙΚΗ ΜΑΣ πληροφορία
        if self.einai_vasilias:
            print(f"   👑 Είναι ο ΒΑΣΙΛΙΑΣ της αγέλης!")

class Elephant(Animal):
    # "Elephant" = αγγλικά "ελέφαντας"

    def __init__(self, onoma, ilikia, varo, mikos_vomvou):
        super().__init__(onoma, "Ελέφαντας", ilikia, varo)
        # Δική μας ιδιότητα — μήκος προβοσκίδας σε εκατοστά
        self.mikos_vomvou = mikos_vomvou
        # "vomvos" = βόμβος (προβοσκίδα)

    def foni(self):
        # Override της foni() για ελέφαντα
        print(f"   🐘 {self.onoma} ΤΡΟΜΠΑΡΙΖΕΙ!")

    def perigrafi(self):
        super().perigrafi()
        print(f"   🦣 Μήκος προβοσκίδας: {self.mikos_vomvou} εκ.")

class Penguin(Animal):
    # "Penguin" = αγγλικά "πιγκουίνος"

    def __init__(self, onoma, ilikia, varo, mporei_na_petaksei):
        super().__init__(onoma, "Πιγκουίνος", ilikia, varo)
        self.mporei_na_petaksei = mporei_na_petaksei
        # → True/False αν μπορεί να πετάξει (spoiler: False! 😄)

    def foni(self):
        print(f"   🐧 {self.onoma} κάνει: Ουα Ουα!")

    def perigrafi(self):
        super().perigrafi()
        # if/else (ξέρουμε από 1.7!)
        if self.mporei_na_petaksei:
            print(f"   ✈️  Μπορεί να πετάξει!")
        else:
            print(f"   🚫 ΔΕΝ μπορεί να πετάξει!")

# ============================================================
# ΒΗΜΑ 3: Η ΚΛΑΣΗ ΤΟΥ ΖΩΟΛΟΓΙΚΟΥ ΚΗΠΟΥ
# ============================================================
#
# Τώρα φτιάχνουμε ΜΙΑ ΚΛΑΣΗ που ΔΙΑΧΕΙΡΙΖΕΤΑΙ τα ζώα
# → αυτό είναι η δύναμη του OOP!
# → κάθε κλάση έχει τη δική της "ευθύνη"

class Zoo:
    # "Zoo" = αγγλικά "ζωολογικός κήπος"

    def __init__(self, onoma_zoo):
        self.onoma_zoo = onoma_zoo      # όνομα ζωολογικού κήπου
        self.zoa = []
        # → λίστα (ξέρουμε από 1.5!) που θα κρατάει ΟΛΑ τα ζώα
        # → ξεκινάει άδεια []

    def prosthese_zoo(self, zoo):
        # "prosthese" = πρόσθεσε
        # "zoo" = ζώο (παράμετρος — ένα αντικείμενο Animal)
        # .append() = αγγλικά "προσάρτηση" (ξέρουμε από 1.5!)
        # → προσθέτει το ζώο στη λίστα
        self.zoa.append(zoo)
        print(f"✅ Το {zoo.onoma} ({zoo.idos}) μπήκε στον ζωολογικό!")

    def emfanise_ola(self):
        # "emfanise" = εμφάνισε, "ola" = όλα
        print(f"\n{'='*45}")
        print(f"   ΖΩΟΛΟΓΙΚΟΣ ΚΗΠΟΣ: {self.onoma_zoo} 🦁")
        print(f"{'='*45}")
        print(f"   Συνολικά ζώα: {len(self.zoa)}")
        # len() = αγγλικά "length" = "μήκος/πλήθος" (ξέρουμε από 1.5!)

        # for loop (ξέρουμε από 1.8!)
        # → περνάει από κάθε ζώο και εκτυπώνει την περιγραφή του
        for zoo in self.zoa:
            zoo.perigrafi()  # καλεί τη method perigrafi() του κάθε ζώου

    def takise_ola(self, trofi):
        # "takise" = τάισε, "ola" = όλα
        print(f"\n🍖 Ώρα ταΐσματος! Τρόφιμο: {trofi}")
        for zoo in self.zoa:
            zoo.taisi(trofi)  # καλεί τη method taisi() του κάθε ζώου

    def akouse_fones(self):
        # "akouse" = άκουσε, "fones" = φωνές
        print(f"\n🔊 Φωνές ζώων:")
        for zoo in self.zoa:
            zoo.foni()  # καλεί τη method foni() — ΚΑΘΕ ζώο έχει ΔΙΚΗ ΤΟΥ!

    def vres_zoo(self, onoma):
        # "vres" = βρες, "zoo" = ζώο
        # → ψάχνει ζώο με συγκεκριμένο όνομα
        for zoo in self.zoa:
            # if zoo.onoma == onoma = αν το όνομα ταιριάζει
            # "==" = ίσο (ξέρουμε από 1.7!)
            if zoo.onoma == onoma:
                return zoo  # return = επιστρέφει το ζώο που βρήκε
        # Αν δεν βρεθεί, επιστρέφει None
        return None
        # "None" = αγγλικά "τίποτα" → δεν βρέθηκε ζώο

    def statistika(self):
        # "statistika" = στατιστικά
        # → εκτυπώνει στατιστικά για τον ζωολογικό
        print(f"\n📊 Στατιστικά {self.onoma_zoo}:")

        # Υπολογίζουμε μέσο όρο ηλικίας
        # sum() = αγγλικά "άθροισμα" → αθροίζει τιμές
        # List Comprehension (ξέρουμε από 1.8!)
        # → [zoo.ilikia for zoo in self.zoa] = λίστα με ηλικίες όλων
        if len(self.zoa) > 0:
            mesos_oros_ilikias = sum([z.ilikia for z in self.zoa]) / len(self.zoa)
            mesos_oros_varous = sum([z.varo for z in self.zoa]) / len(self.zoa)
            print(f"   Μέσος όρος ηλικίας: {round(mesos_oros_ilikias, 1)} χρόνια")
            # round() = αγγλικά "στρογγυλοποίηση" (ξέρουμε από 1.9!)
            print(f"   Μέσος όρος βάρους:  {round(mesos_oros_varous, 1)} κιλά")
            print(f"   Συνολικά ζώα:       {len(self.zoa)}")

# ============================================================
# ΚΥΡΙΟ ΠΡΟΓΡΑΜΜΑ
# ============================================================
# Εδώ ΧΡΗΣΙΜΟΠΟΙΟΥΜΕ τις κλάσεις που ορίσαμε παραπάνω
# Φτιάχνουμε ΑΝΤΙΚΕΙΜΕΝΑ (objects) από τα "καλούπια" (classes)

print("=" * 45)
print("   ΖΩΟΛΟΓΙΚΟΣ ΚΗΠΟΣ - Μάθημα 1.13 OOP 🦁")
print("=" * 45)

# Δημιουργούμε αντικείμενα (objects)
# ΌνομαΚλάσης(παράμετροι) = "φτιάξε νέο αντικείμενο"
# → καλεί αυτόματα τον __init__

# Δημιουργούμε λιοντάρια
simba = Lion("Simba", 5, 190, True)
# → onoma="Simba", ilikia=5, varo=190, einai_vasilias=True

nala = Lion("Nala", 4, 160, False)
# → onoma="Nala", ilikia=4, varo=160, einai_vasilias=False

# Δημιουργούμε ελέφαντα
elefas = Elephant("Dumbo", 10, 4500, 180)
# → onoma="Dumbo", ilikia=10, varo=4500, mikos_vomvou=180

# Δημιουργούμε πιγκουίνο
pingouinos = Penguin("Tux", 3, 5, False)
# → onoma="Tux", ilikia=3, varo=5, mporei_na_petaksei=False

# Δημιουργούμε τον ζωολογικό κήπο
zoo = Zoo("Ζωολογικός Αιγίου")
# → onoma_zoo="Ζωολογικός Αιγίου"

# Προσθέτουμε ζώα στον ζωολογικό
# → καλούμε τη method prosthese_zoo() του αντικειμένου zoo
zoo.prosthese_zoo(simba)
zoo.prosthese_zoo(nala)
zoo.prosthese_zoo(elefas)
zoo.prosthese_zoo(pingouinos)

# Εμφανίζουμε όλα τα ζώα
zoo.emfanise_ola()

# Ακούμε τις φωνές — κάθε ζώο έχει ΔΙΑΦΟΡΕΤΙΚΗ φωνή!
# → αυτό λέγεται "polymorphism" = αγγλικά "πολυμορφισμός"
# → το ίδιο "κουμπί" (foni) κάνει ΔΙΑΦΟΡΕΤΙΚΑ πράγματα
#   ανάλογα με το ζώο!
zoo.akouse_fones()

# Ταΐζουμε όλα τα ζώα
zoo.takise_ola("κρέας και φρούτα")

# Ψάχνουμε συγκεκριμένο ζώο
print(f"\n🔍 Αναζήτηση ζώου 'Simba':")
vrethike = zoo.vres_zoo("Simba")

# if vrethike = αν βρέθηκε (δεν είναι None)
if vrethike:
    print(f"   ✅ Βρέθηκε! Είναι {vrethike.idos}!")
    vrethike.foni()  # καλούμε τη φωνή μόνο για αυτό
else:
    print(f"   ❌ Δεν βρέθηκε!")

# Στατιστικά
zoo.statistika()

print("\n" + "=" * 45)
print("   Τέλος μαθήματος 1.13 — OOP ✅")
print("=" * 45)