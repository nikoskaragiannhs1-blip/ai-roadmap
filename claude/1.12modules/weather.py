# ============================================
# ΚΑΙΡΟΣ & ΩΡΑ ΑΠΟ API - Μάθημα 1.12
# ============================================

# import = "φόρτωσε αυτό το module"
# Το ξέρουμε από προηγούμενα μαθήματα!
import requests   # εξωτερικό module — μιλάει με το internet
import datetime   # ενσωματωμένο module — ημερομηνία & ώρα

# ---- ΣΥΝΑΡΤΗΣΕΙΣ ----
# def = ορισμός συνάρτησης (το ξέρουμε από 1.9!)

def pare_trehoysa_ora():
    # datetime.datetime.now() = παίρνει την τρέχουσα ώρα & ημερομηνία
    # Νέο: datetime.datetime.now() επιστρέφει ένα αντικείμενο με ώρα
    tora = datetime.datetime.now()

    # .strftime() = μορφοποιεί την ώρα σε κείμενο
    # Νέο σύμβολο: strftime (string format time)
    # "%H" = ώρα σε 24ωρο, "%M" = λεπτά, "%S" = δευτερόλεπτα
    # "%d/%m/%Y" = ημέρα/μήνας/χρόνος
    ora = tora.strftime("%H:%M:%S")
    imera = tora.strftime("%d/%m/%Y")

    # return = επιστρέφει τιμές πίσω (το ξέρουμε από 1.9!)
    # Επιστρέφουμε 2 τιμές μαζί — η Python τις βάζει σε tuple
    return ora, imera

def pare_kairo(poli="Aigio"):
    # try = δοκίμασε (το ξέρουμε από 1.10!)
    try:
        # Το API του wttr.in μας δίνει καιρό δωρεάν
        # f-string για να βάλουμε την πόλη στη διεύθυνση
        # ?format=j1 = ζητάμε τα δεδομένα σε JSON μορφή
        # Νέο: το "?" στο URL σημαίνει "παράμετροι αίτησης"
        url = f"https://wttr.in/{poli}?format=j1"

        # requests.get() = στέλνει αίτηση GET στο URL
        # Σαν να ανοίγεις μια ιστοσελίδα αλλά από Python!
        # timeout=5 = αν δεν απαντήσει σε 5 δευτερόλεπτα, σταμάτα
        # Νέο σύμβολο: timeout = χρονικό όριο αναμονής
        response = requests.get(url, timeout=5)

        # .json() = μετατρέπει την απάντηση από JSON σε dictionary Python
        # JSON = JavaScript Object Notation, μορφή δεδομένων του internet
        # Νέο: JSON μοιάζει με dictionary της Python!
        data = response.json()

        # Βγάζουμε τα δεδομένα από το dictionary
        # data["current_condition"] = λίστα με τρέχουσες συνθήκες
        # [0] = πρώτο (και μοναδικό) στοιχείο της λίστας
        # Το [0] το ξέρουμε από 1.5 — πρώτο στοιχείο λίστας!
        current = data["current_condition"][0]

        # Παίρνουμε θερμοκρασία σε Celsius
        # "temp_C" = κλειδί του dictionary (το ξέρουμε από 1.6!)
        thermokrasia = current["temp_C"]

        # Παίρνουμε περιγραφή καιρού
        # "weatherDesc" = άλλη λίστα μέσα στο dictionary
        # [0]["value"] = πρώτο στοιχείο, τιμή "value"
        perigafi = current["weatherDesc"][0]["value"]

        # Παίρνουμε υγρασία
        ygrasia = current["humidity"]

        # Παίρνουμε ταχύτητα ανέμου σε km/h
        anemos = current["windspeedKmph"]

        # Επιστρέφουμε dictionary με όλα τα στοιχεία
        # Φτιάχνουμε δικό μας dictionary (το ξέρουμε από 1.6!)
        return {
            "thermokrasia": thermokrasia,
            "perigafi": perigafi,
            "ygrasia": ygrasia,
            "anemos": anemos,
            "poli": poli
        }

    # except = αν κάτι πάει στραβά (το ξέρουμε από 1.10!)
    except requests.exceptions.ConnectionError:
        # ConnectionError = δεν υπάρχει σύνδεση internet
        print("❌ Δεν υπάρχει σύνδεση internet!")
        return None
    except requests.exceptions.Timeout:
        # Timeout = το API δεν απάντησε στα 5 δευτερόλεπτα
        print("❌ Το API δεν απάντησε — δοκίμασε ξανά!")
        return None
    except Exception as e:
        # Exception = οποιοδήποτε άλλο λάθος
        # "as e" = αποθηκεύει το μήνυμα λάθους (το ξέρουμε από 1.10!)
        print(f"❌ Σφάλμα: {e}")
        return None

# ---- ΚΥΡΙΟ ΠΡΟΓΡΑΜΜΑ ----

# "=" * 40 = εκτυπώνει 40 φορές το "=" (το ξέρουμε από 1.4!)
print("=" * 40)
print("     ΚΑΙΡΟΣ & ΩΡΑ 🌤️")
print("=" * 40)

# Καλούμε τη συνάρτηση — επιστρέφει 2 τιμές
# Τις αποθηκεύουμε σε 2 μεταβλητές ταυτόχρονα
# Νέο σύμβολο: a, b = συνάρτηση() = "αποσυσκεύασμα" 2 τιμών
ora, imera = pare_trehoysa_ora()

# f-string για εκτύπωση (το ξέρουμε από 1.4!)
print(f"\n🕐 Τρέχουσα ώρα:  {ora}")
print(f"📅 Σημερινή μέρα: {imera}")

print("\n" + "-" * 40)
print("🌍 Παρακολούθηση καιρού:")
print("-" * 40)

# Λίστα με πόλεις που θέλουμε να ελέγξουμε
# Λίστα = [] (το ξέρουμε από 1.5!)
poleis = ["Aigio", "Athens", "Thessaloniki"]

# for loop = περνάει από κάθε πόλη (το ξέρουμε από 1.8!)
for poli in poleis:
    print(f"\n📍 {poli}:")

    # Καλούμε τη συνάρτηση για κάθε πόλη
    kairos = pare_kairo(poli)

    # if = ελέγχουμε αν επέστρεψε δεδομένα (το ξέρουμε από 1.7!)
    # "if kairos" = αν kairos δεν είναι None
    if kairos:
        print(f"   🌡️  Θερμοκρασία: {kairos['thermokrasia']}°C")
        print(f"   ☁️  Καιρός:      {kairos['perigafi']}")
        print(f"   💧 Υγρασία:     {kairos['ygrasia']}%")
        print(f"   💨 Άνεμος:      {kairos['anemos']} km/h")

print("\n" + "=" * 40)