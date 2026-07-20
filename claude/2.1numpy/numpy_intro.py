# ============================================================
# ΜΑΘΗΜΑ 2.1 — NumPy Εισαγωγή
# NumPy = "Numerical Python" = "Αριθμητική Python"
# → η πιο σημαντική βιβλιοθήκη για αριθμούς στην Python
# → χρησιμοποιείται παντού: Data Science, AI, Machine Learning
# ============================================================
#
# ΤΙ ΘΑ ΜΑΘΟΥΜΕ ΣΗΜΕΡΑ:
# 1. Τι είναι το "array" = αγγλικά "πίνακας/συστοιχία"
#    → σαν λίστα αλλά ΠΟΛΥ πιο γρήγορη και δυνατή
# 2. Πώς φτιάχνουμε arrays
# 3. Βασικές πράξεις με arrays
# 4. Στατιστικές συναρτήσεις
#
# ΣΥΝΔΕΣΗ ΜΕ PYGRAM:
# → θα αναλύουμε δεδομένα χρηστών του PyGram
#   (likes, posts, ακόλουθοι) με NumPy!
# ============================================================

# --------------------------------------------------
# ΕΙΣΑΓΩΓΗ NUMPY
# --------------------------------------------------

# "import" = αγγλικά "εισαγωγή" (ξέρουμε από 1.12!)
# → φορτώνει το module
# "as" = αγγλικά "ως/σαν"
# → δίνουμε ΠΑΡΑΤΣΟΥΚΛΙ στο module για να γράφουμε λιγότερο
# → αντί για "numpy.array()" γράφουμε "np.array()"
# → το "np" είναι η ΣΥΜΒΑΣΗ — όλοι οι developers το χρησιμοποιούν!
import numpy as np

print("=" * 50)
print("   ΜΑΘΗΜΑ 2.1 — NumPy Εισαγωγή 📊")
print("=" * 50)

# ============================================================
# ΜΕΡΟΣ 1: ΤΙ ΕΙΝΑΙ ΤΟ ARRAY
# ============================================================
# "array" = αγγλικά "συστοιχία/πίνακας"
# → είναι σαν λίστα Python αλλά:
#   ✅ ΠΟΛΥ πιο γρήγορη σε μαθηματικές πράξεις
#   ✅ Μπορεί να έχει πολλές διαστάσεις (1D, 2D, 3D...)
#   ✅ Όλα τα στοιχεία ΠΡΕΠΕΙ να είναι ίδιου τύπου
#
# ΔΙΑΦΟΡΑ λίστας vs array:
# λίστα:  [1, 2, 3]        → Python list (ξέρουμε από 1.5!)
# array:  np.array([1,2,3]) → NumPy array (νέο!)

print("\n📌 ΜΕΡΟΣ 1: Δημιουργία Arrays")
print("-" * 50)

# np.array() = δημιουργεί array από λίστα
# → περνάμε λίστα [] μέσα στην np.array()
# → αποτέλεσμα: NumPy array αντί για Python list

# Δεδομένα PyGram — likes ανά ημέρα για έναν χρήστη
# "dedomena_likes" = δεδομένα likes (ξεκάθαρα διαφορετικό από τιμές!)
dedomena_likes = np.array([15, 23, 8, 42, 31, 19, 56])
# → [15, 23, 8, 42, 31, 19, 56] = likes Δευ, Τρι, Τετ, Πεμ, Παρ, Σαβ, Κυρ

print(f"Likes ανά ημέρα: {dedomena_likes}")
# → εκτυπώνει: [ 15  23   8  42  31  19  56]
# → παρατήρησε: χωρίς κόμματα! Αυτή είναι η μορφή NumPy array

print(f"Τύπος δεδομένων: {type(dedomena_likes)}")
# type() = αγγλικά "τύπος" (ξέρουμε από 1.2!)
# → θα δείξει: <class 'numpy.ndarray'>
# → "ndarray" = "n-dimensional array" = "πολυδιάστατος πίνακας"

print(f"Πλήθος στοιχείων: {dedomena_likes.shape}")
# ".shape" = αγγλικά "σχήμα/μέγεθος"
# → νέο σύμβολο: .shape δείχνει τις ΔΙΑΣΤΑΣΕΙΣ του array
# → (7,) σημαίνει: 7 στοιχεία σε 1 διάσταση

print(f"Τύπος αριθμών: {dedomena_likes.dtype}")
# ".dtype" = αγγλικά "data type" = "τύπος δεδομένων"
# → δείχνει τι ΤΥΠΟ αριθμών έχει το array (int64, float64 κ.λπ.)
# → "int64" = ακέραιος 64-bit (μεγάλο εύρος αριθμών)

# --------------------------------------------------
# ΤΡΟΠΟΙ ΔΗΜΙΟΥΡΓΙΑΣ ARRAY
# --------------------------------------------------

print("\n📌 Τρόποι δημιουργίας array:")

# np.zeros() = αγγλικά "μηδενικά"
# → δημιουργεί array με ΟΛΟΥΣ ΜΗΔΕΝ
# → χρήσιμο για αρχικοποίηση (ξέρουμε την έννοια από 1.13 __init__!)
pinakasv_midenikwn = np.zeros(5)
# → (5) = 5 στοιχεία
print(f"Πίνακας μηδενικών:  {pinakasv_midenikwn}")
# → [ 0.  0.  0.  0.  0.]

# np.ones() = αγγλικά "μονάδες"
# → δημιουργεί array με ΟΛΟΥΣ ΜΟΝΑ
pinakasv_monadwn = np.ones(5)
print(f"Πίνακας μονάδων:    {pinakasv_monadwn}")
# → [ 1.  1.  1.  1.  1.]

# np.arange() = αγγλικά "array range" = "εύρος πίνακα"
# → σαν το range() που ξέρουμε (1.8!) αλλά επιστρέφει array
# → np.arange(αρχή, τέλος, βήμα)
arithmoi_apo_0_eos_9 = np.arange(0, 10, 1)
# → ξεκινάει από 0, σταματάει ΠΡΙΝ το 10, βήμα 1
print(f"arange(0,10,1):     {arithmoi_apo_0_eos_9}")
# → [0 1 2 3 4 5 6 7 8 9]

# np.linspace() = αγγλικά "linear space" = "γραμμικός χώρος"
# → δημιουργεί Ν ισαπέχοντα σημεία μεταξύ δύο τιμών
# → np.linspace(αρχή, τέλος, πλήθος)
isotimes_times = np.linspace(0, 1, 5)
# → 5 ισαπέχοντα σημεία από 0 έως 1
print(f"linspace(0,1,5):    {isotimes_times}")
# → [0.   0.25 0.5  0.75 1.  ]

# np.random.randint() = τυχαίοι ακέραιοι
# → random = αγγλικά "τυχαίος" (ξέρουμε από 1.7!)
# → np.random.randint(min, max, size)
tixaia_dedomena = np.random.randint(1, 100, 7)
# → 7 τυχαίοι αριθμοί από 1 έως 99
print(f"Τυχαία δεδομένα:    {tixaia_dedomena}")

# ============================================================
# ΜΕΡΟΣ 2: ΠΡΑΞΕΙΣ ΜΕ ARRAYS
# ============================================================
# Η ΜΕΓΑΛΗ δύναμη του NumPy:
# → μπορείς να κάνεις πράξεις σε ΟΛΟΝ τον πίνακα ΤΑΥΤΟΧΡΟΝΑ!
# → με λίστα Python θα χρειαζόσουν for loop (ξέρουμε από 1.8!)
# → με NumPy γίνεται σε ΜΙΑ γραμμή!

print("\n📌 ΜΕΡΟΣ 2: Πράξεις με Arrays")
print("-" * 50)

# Δεδομένα PyGram
statistika_xristi_a = np.array([10, 20, 30, 40, 50])
# → likes χρήστη Α για 5 μέρες
statistika_xristi_b = np.array([5, 15, 25, 35, 45])
# → likes χρήστη Β για 5 μέρες

print(f"Χρήστης Α: {statistika_xristi_a}")
print(f"Χρήστης Β: {statistika_xristi_b}")

# ΠΡΟΣΘΕΣΗ arrays — προσθέτει ΑΝΤΙΣΤΟΙΧΑ στοιχεία
# → [10+5, 20+15, 30+25, 40+35, 50+45]
athroisma_likes = statistika_xristi_a + statistika_xristi_b
print(f"\nΆθροισμα likes:     {athroisma_likes}")
# → [15 35 55 75 95]

# ΑΦΑΙΡΕΣΗ arrays
diafora_likes = statistika_xristi_a - statistika_xristi_b
print(f"Διαφορά likes:      {diafora_likes}")
# → [5 5 5 5 5]

# ΠΟΛΛΑΠΛΑΣΙΑΣΜΟΣ με σταθερά
# → πολλαπλασιάζει ΚΑΘΕ στοιχείο με 2
diplasiasmenos = statistika_xristi_a * 2
print(f"Διπλάσια likes Α:   {diplasiasmenos}")
# → [20 40 60 80 100]

# ΣΥΓΚΡΙΣΗ arrays — επιστρέφει array από True/False!
# → ">" = μεγαλύτερο (ξέρουμε από 1.7!)
sinkrisi_30 = statistika_xristi_a > 30
# → ελέγχει κάθε στοιχείο: είναι > 30;
print(f"Likes > 30:         {sinkrisi_30}")
# → [False False False  True  True]
# → μόνο 40 και 50 είναι > 30

# ΦΙΛΤΡΑΡΙΣΜΑ με boolean array
# → νέο σύμβολο: array[boolean_array]
# → κρατάει ΜΟΝΟ τα στοιχεία όπου είναι True!
likes_pano_apo_30 = statistika_xristi_a[sinkrisi_30]
print(f"Μόνο likes > 30:    {likes_pano_apo_30}")
# → [40 50]

# ============================================================
# ΜΕΡΟΣ 3: ΣΤΑΤΙΣΤΙΚΕΣ ΣΥΝΑΡΤΗΣΕΙΣ
# ============================================================
# Αυτές είναι οι πιο ΧΡΗΣΙΜΕΣ συναρτήσεις για ανάλυση δεδομένων!

print("\n📌 ΜΕΡΟΣ 3: Στατιστικές Συναρτήσεις")
print("-" * 50)

# Δεδομένα PyGram — likes 30 ημερών
monthly_likes = np.array([
    45, 23, 67, 12, 89, 34, 56, 78, 90, 11,
    43, 65, 87, 32, 54, 76, 98, 21, 43, 65,
    12, 34, 56, 78, 90, 23, 45, 67, 89, 11
])
# → 30 τιμές = likes για κάθε μέρα του μήνα

print(f"Likes 30 ημερών: {monthly_likes}")

# np.sum() = αγγλικά "sum" = "άθροισμα"
# → αθροίζει ΟΛΕΣ τις τιμές
synolo_likes = np.sum(monthly_likes)
print(f"\n📊 Σύνολο likes:       {synolo_likes}")

# np.mean() = αγγλικά "mean" = "μέσος όρος"
# → αθροίζει και διαιρεί με το πλήθος
mesos_oros = np.mean(monthly_likes)
print(f"📊 Μέσος όρος/μέρα:   {mesos_oros:.1f}")
# ":.1f" = εμφάνισε με 1 δεκαδικό ψηφίο
# → νέο σύμβολο: ":.1f" μέσα σε f-string = μορφοποίηση αριθμού

# np.median() = αγγλικά "median" = "διάμεσος"
# → ο ΜΕΣΑΙΟΣ αριθμός όταν ταξινομηθούν
# → πιο αξιόπιστος από mean όταν υπάρχουν ακραίες τιμές!
diamesosv = np.median(monthly_likes)
print(f"📊 Διάμεσος:           {diamesosv:.1f}")

# np.max() = αγγλικά "maximum" = "μέγιστο"
# → η ΜΕΓΑΛΥΤΕΡΗ τιμή
megisti_timi = np.max(monthly_likes)
print(f"📊 Μέγιστα likes:      {megisti_timi}")

# np.min() = αγγλικά "minimum" = "ελάχιστο"
# → η ΜΙΚΡΟΤΕΡΗ τιμή
elaxisti_timi = np.min(monthly_likes)
print(f"📊 Ελάχιστα likes:     {elaxisti_timi}")

# np.std() = αγγλικά "standard deviation" = "τυπική απόκλιση"
# → δείχνει πόσο "διασκορπισμένες" είναι οι τιμές
# → μικρή std = σταθερές τιμές, μεγάλη std = μεγάλες διακυμάνσεις
typiki_apoklisi = np.std(monthly_likes)
print(f"📊 Τυπική απόκλιση:    {typiki_apoklisi:.1f}")

# np.argmax() = αγγλικά "argument of maximum" = "θέση μεγίστου"
# → επιστρέφει τη ΘΕΣΗ (index) της μεγαλύτερης τιμής
thesi_megistou = np.argmax(monthly_likes)
# → "thesi" = θέση — ξεκάθαρα διαφορετικό από "megisti_timi"!
print(f"📊 Καλύτερη μέρα:      Μέρα {thesi_megistou + 1} (index {thesi_megistou})")
# → +1 γιατί οι άνθρωποι μετράμε από 1, η Python από 0!

# np.argmin() = θέση ελαχίστου
thesi_elaxistou = np.argmin(monthly_likes)
print(f"📊 Χειρότερη μέρα:     Μέρα {thesi_elaxistou + 1} (index {thesi_elaxistou})")

# ============================================================
# ΜΕΡΟΣ 4: 2D ARRAYS (Δισδιάστατοι Πίνακες)
# ============================================================
# Μέχρι τώρα είχαμε 1D arrays (μία γραμμή αριθμών)
# Τώρα μαθαίνουμε 2D arrays (πίνακας με γραμμές ΚΑΙ στήλες)
# → σαν υπολογιστικό φύλλο Excel!
# → χρησιμοποιείται παντού στο Machine Learning!

print("\n📌 ΜΕΡΟΣ 4: 2D Arrays")
print("-" * 50)

# Δεδομένα PyGram — 3 χρήστες, 5 μέρες
# → κάθε ΓΡΑΜΜΗ = ένας χρήστης
# → κάθε ΣΤΗΛΗ = μια μέρα
# → np.array([[...], [...], [...]]) = λίστα από λίστες!
pinakas_xriston = np.array([
    [45, 23, 67, 12, 89],   # χρήστης Νίκος
    [32, 54, 21, 76, 43],   # χρήστης Μαρία
    [11, 98, 34, 56, 78]    # χρήστης Κώστας
])
# → shape (3, 5) = 3 γραμμές, 5 στήλες

print(f"Πίνακας likes (3 χρήστες, 5 μέρες):")
print(pinakas_xriston)

print(f"\nΔιαστάσεις: {pinakas_xriston.shape}")
# → (3, 5) = 3 γραμμές × 5 στήλες

# Πρόσβαση σε στοιχεία 2D array
# → [γραμμή, στήλη] — νέο σύμβολο!
# → θυμάσαι [0] για λίστες (1.5!); εδώ [0, 0] για 2D!
print(f"\nLikes Νίκου Δευτέρα: {pinakas_xriston[0, 0]}")
# → [0, 0] = γραμμή 0 (Νίκος), στήλη 0 (Δευτέρα)
print(f"Likes Μαρίας Παρασκευή: {pinakas_xriston[1, 4]}")
# → [1, 4] = γραμμή 1 (Μαρία), στήλη 4 (Παρασκευή)

# Ολόκληρη γραμμή (όλες οι μέρες ενός χρήστη)
# → [:] = αγγλικά "slice" = "κόψε/πάρε όλα"
# → [0, :] = γραμμή 0, ΟΛΕς οι στήλες
likes_nikou = pinakas_xriston[0, :]
print(f"Όλα τα likes Νίκου: {likes_nikou}")

# Ολόκληρη στήλη (όλοι οι χρήστες μια μέρα)
# → [:, 0] = ΟΛΕΣ οι γραμμές, στήλη 0
likes_deuteras = pinakas_xriston[:, 0]
print(f"Likes Δευτέρας (όλοι): {likes_deuteras}")

# Στατιστικά ανά άξονα
# axis=0 = "axis zero" = κατά ΣΤΗΛΗ (για κάθε μέρα)
# axis=1 = "axis one"  = κατά ΓΡΑΜΜΗ (για κάθε χρήστη)
# → "axis" = αγγλικά "άξονας"
mesos_oros_ana_xristi = np.mean(pinakas_xriston, axis=1)
# → axis=1 = υπολογίζει mean κατά γραμμή
print(f"\nΜέσος όρος ανά χρήστη: {mesos_oros_ana_xristi}")

mesos_oros_ana_mera = np.mean(pinakas_xriston, axis=0)
# → axis=0 = υπολογίζει mean κατά στήλη
print(f"Μέσος όρος ανά μέρα:   {mesos_oros_ana_mera}")

# ============================================================
# ΣΥΝΔΕΣΗ ΜΕ PYGRAM — Mini Ανάλυση
# ============================================================

print("\n" + "=" * 50)
print("   📱 ΑΝΑΛΥΣΗ ΔΕΔΟΜΕΝΩΝ PYGRAM")
print("=" * 50)

# Προσομοίωση δεδομένων PyGram για 7 χρήστες
onomata_xriston = ["@nikos", "@maria", "@kostas", "@giorgos",
                   "@elena", "@petros", "@sofia"]
# → λίστα Python (ξέρουμε από 1.5!) με ονόματα

# np.random.randint() = τυχαίοι ακέραιοι για προσομοίωση
# → seed(42) = "σπόρος" τυχαιότητας — κάνει τα τυχαία ΣΤΑΘΕΡΑ
# → ίδιοι αριθμοί κάθε φορά που τρέχεις! (για αναπαραγωγιμότητα)
np.random.seed(42)
# → "seed" = αγγλικά "σπόρος" — ορίζει την αφετηρία τυχαιότητας

synolo_posts = np.random.randint(10, 500, 7)
# → 7 τυχαίοι αριθμοί από 10 έως 499 (posts ανά χρήστη)
synolo_akolouthon = np.random.randint(50, 10000, 7)
# → 7 τυχαίοι αριθμοί από 50 έως 9999 (ακόλουθοι ανά χρήστη)
synolo_likes_ekvdomadas = np.random.randint(100, 5000, 7)
# → 7 τυχαίοι αριθμοί (likes εβδομάδας ανά χρήστη)

print(f"\n{'Χρήστης':<12} {'Posts':>8} {'Ακόλουθοι':>12} {'Likes/Εβδ':>12}")
# → f-string με στοίχιση:
# → "<12" = αριστερή στοίχιση σε 12 χαρακτήρες
# → ">8"  = δεξιά στοίχιση σε 8 χαρακτήρες
# → νέο σύμβολο: "<Ν" και ">Ν" μέσα σε f-string = στοίχιση κειμένου
print("-" * 46)

# enumerate() (ξέρουμε από 1.5!) για αριθμό + τιμή
for thesi, onoma in enumerate(onomata_xriston):
    print(f"{onoma:<12} {synolo_posts[thesi]:>8} "
          f"{synolo_akolouthon[thesi]:>12} {synolo_likes_ekvdomadas[thesi]:>12}")

print("-" * 46)
print(f"{'ΣΥΝΟΛΑ':<12} {np.sum(synolo_posts):>8} "
      f"{np.sum(synolo_akolouthon):>12} {np.sum(synolo_likes_ekvdomadas):>12}")
print(f"{'ΜΕΣΟΣ':<12} {np.mean(synolo_posts):>8.0f} "
      f"{np.mean(synolo_akolouthon):>12.0f} {np.mean(synolo_likes_ekvdomadas):>12.0f}")
# → ":.0f" = μορφοποίηση χωρίς δεκαδικά

# Βρίσκουμε τον πιο δημοφιλή χρήστη
thesi_top = np.argmax(synolo_akolouthon)
print(f"\n🏆 Πιο δημοφιλής: {onomata_xriston[thesi_top]} "
      f"με {synolo_akolouthon[thesi_top]} ακόλουθους!")

# Βρίσκουμε χρήστες με πάνω από 5000 ακόλουθους
thesi_popular = synolo_akolouthon > 5000
# → boolean array (True/False) για κάθε χρήστη
print(f"\n⭐ Χρήστες με >5000 ακόλουθους:")
for thesi, einai_popular in enumerate(thesi_popular):
    # enumerate() = δίνει θέση + τιμή (ξέρουμε από 1.5!)
    if einai_popular:
        # if True = αν είναι popular (ξέρουμε από 1.7!)
        print(f"   {onomata_xriston[thesi]}: {synolo_akolouthon[thesi]} ακόλουθοι")

print("\n" + "=" * 50)
print("   ✅ Μάθημα 2.1 — NumPy Εισαγωγή ΤΕΛΟΣ!")
print("=" * 50)