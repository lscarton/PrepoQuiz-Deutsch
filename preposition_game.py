import random

# List of verbs with their correct prepositions, cases, and example sentences
verbs = [
    ("abhängen", "vom", "D", "Ob wir fahren, hängt __ dem Wetter ab."),
    ("achten", "auf", "A", "Bitte achte __ den neuen Mantel."),
    ("anfangen", "mit", "D", "Ich fange __ der Übung an."),
    ("ankommen", "auf", "A", "Es kommt __ den richtigen Preis an."),
    ("antworten", "auf", "A", "Bitte antworten Sie heute __ den Brief."),
    ("sich ärgern", "über", "A", "Wir ärgern uns __ den Regen."),
    ("aufhören", "mit", "D", "Er hört um 17.00 Uhr __ der Arbeit auf."),
    ("aufpassen", "auf", "A", "Ein Babysitter passt __ kleine Kinder auf."),
    ("sich aufregen", "über", "A", "Deutsche regen sich __ Unpünktlichkeit auf."),
    ("ausgeben", "für", "A", "Manche geben viel Geld __ Schuhe aus."),
    ("sich bedanken", "bei", "D", "Ich bedanke mich herzlich __ dir."),
    ("sich bedanken", "für", "A", "Martin bedankt sich __ das Geschenk."),
    ("beginnen", "mit", "D", "Wir beginnen pünktlich __ dem Deutschkurs."),
    ("sich bemühen", "um", "A", "Karla bemüht sich __ eine Arbeit."),
    ("berichten", "über", "A", "Der Reporter berichtet __ die Wahlen."),
    ("sich beschäftigen", "mit", "D", "Ich beschäftige mich gern __ Pflanzen."),
    ("sich beschweren", "bei", "D", "Der Gast beschwert sich __ dem Kellner."),
    ("bestehen", "aus", "D", "Eheringe bestehen __ Gold."),
    ("bestehen", "auf", "D", "Ich bestehe __ sofortiger Bezahlung des Autos."),
    ("sich beteiligen", "an", "D", "Viele Studenten beteiligen sich __ den Streiks."),
    ("sich bewerben", "bei", "D", "Er bewirbt sich __ einer Bäckerei."),
    ("sich bewerben", "um", "A", "Sie bewirbt sich __ eine Stelle als Sekretärin."),
    ("sich beziehen", "auf", "A", "Meine Frage bezieht sich __ Ihr Angebot."),
    ("bitten", "um", "A", "Der Redner bittet __ Aufmerksamkeit."),
    ("danken", "für", "A", "Sam dankt __ Ritas Hilfe."),
    ("denken", "an", "A", "Maria denkt oft __ den Urlaub."),
    ("diskutieren", "über", "A", "Das Kabinett diskutiert __ eine neue Steuer."),
    ("einladen", "zu", "D", "Ich lade dich __ meinem Geburtstag ein."),
    ("sich entscheiden", "für", "A", "Kinder entscheiden sich gern __ Schokolade."),
    ("sich entschließen", "zu", "D", "Karl entschließt sich __ einem Studium."),
    ("sich entschuldigen", "bei", "D", "Tom entschuldigt sich __ ihrem Mann."),
    ("sich entschuldigen", "für", "A", "Ich entschuldige mich __ das Verhalten meiner Katze."),
    ("sich erholen", "von", "D", "__ dem Schock muss ich mich erst erholen."),
    ("sich erinnern", "an", "A", "Wir erinnern uns gern __ unser erstes Ehejahr."),
    ("erkennen", "an", "D", "Man erkennt Pinocchio __ seiner langen Nase."),
    ("sich erkundigen", "nach", "D", "Oma erkundigt sich oft __ meinen Plänen."),
    ("erschrecken", "über", "A", "Der Koch erschrickt __ eine Maus."),
    ("erzählen", "über", "A", "Ein Ostberliner erzählt __ sein Leben in der ehemaligen DDR."),
    ("erzählen", "von", "D", "Der Bischoff erzählt __ der Reise nach Rom."),
    ("fragen", "nach", "D", "Die Journalistin fragt __ den Konsequenzen der Gesetzesänderung."),
    ("sich freuen", "auf", "A", "Kinder freuen sich __ die Ferien."),
    ("sich freuen", "über", "A", "Jeder freut sich __ eine Gehaltserhöhung."),
    ("gehen", "um", "A", "Immer geht es __ Geld."),
    ("gehören", "zu", "D", "Das Elsass gehört __ Frankreich."),
    ("sich gewöhnen", "an", "A", "Ich kann mich nicht __ die Zeitumstellung gewöhnen."),
    ("glauben", "an", "A", "Teenager glauben __ die große Liebe."),
    ("gratulieren", "zu", "D", "Wir gratulieren dir __ dem 18. Geburtstag."),
    ("halten", "für", "A", "Ich halte das __ keine gute Idee."),
    ("halten", "von", "D", "Kinder halten nicht viel __ Ordnung."),
    ("sich handeln", "um", "A", "Bei der Kopie handelt es sich nicht __ Originalsoftware."),
    ("handeln", "von", "D", "Märchen handeln __ Gut und Böse."),
    ("helfen", "bei", "D", "Kann ich dir __ dem Tischdecken helfen?"),
    ("hindern", "an", "D", "Ein langsamer Fahrer hindert Greta __ Überholen."),
    ("hoffen", "auf", "A", "Im März hoffen alle __ warme Frühlingstage."),
    ("hören", "von", "D", "Ich habe seit Sonntag nichts __ Piet gehört."),
    ("sich informieren", "über", "A", "Auf der Messe kann man sich __ die neue Technologie informieren."),
    ("sich interessieren", "für", "A", "Monika interessiert sich __ ein Smartphone."),
    ("klagen", "über", "A", "Tim klagt häufig __ Kopfschmerzen."),
    ("kämpfen", "für", "A", "Die Gewerkschaft kämpft __ höhere Löhne."),
    ("kommen", "zu", "D", "In der Besprechung kam es __ einem Streit."),
    ("sich konzentrieren", "auf", "A", "Karl konzentriert sich __ seine Hausaufgaben."),
    ("sich kümmern", "um", "A", "Im Pflegeheim kümmert man sich __ alte Leute, die krank sind."),
    ("lachen", "über", "A", "__ einen guten Witz muss man laut lachen."),
    ("leiden", "an", "D", "Jeder fünfte Manager leidet __ Burn-out."),
    ("leiden", "unter", "D", "Kaffeetrinker leiden __ Schlafproblemen."),
    ("nachdenken", "über", "A", "Beamte müssen nicht __ ihre Rente nachdenken."),
    ("protestieren", "gegen", "A", "Viele Menschen protestieren __ Atomkraft."),
    ("rechnen", "mit", "D", "Im Januar muss man __ Schnee rechnen."),
    ("reden", "über", "A", "Deine Mutter redet gern __ Krankheiten."),
    ("reden", "von", "D", "Großvater redet __ den guten alten Zeiten."),
    ("riechen", "nach", "D", "Hier riecht es __ Kuchen."),
    ("sagen", "über", "A", "Brigitte sagt __ Dietmar, dass er oft lügt."),
    ("sagen", "zu", "D", "Was sagst du __ meinem neuen Haarschnitt?"),
    ("schicken", "zu", "D", "Der Allgemeinmediziner schickt den Patienten __ einem Spezialisten."),
    ("schimpfen", "über", "A", "Alle schimpfen __ den Regen."),
    ("schmecken", "nach", "D", "Muscheln schmecken __ Meerwasser."),
    ("schreiben", "an", "A", "Bitte schreibe noch heute __ deine Mutter."),
    ("sich schützen", "vor", "D", "Den Computer muss man __ Hackern schützen."),
    ("sein", "für", "A", "Ich bin __ die Abschaffung der Kinderarbeit."),
    ("sein", "gegen", "A", "Viele sind __ Steuererhöhungen."),
    ("sorgen", "für", "A", "Kinder müssen im Alter __ ihre Eltern sorgen."),
    ("sprechen", "mit", "D", "Ich spreche noch einmal __ deinem Vater."),
    ("sprechen", "über", "A", "Lass uns __ deine Zukunft sprechen."),
    ("sterben", "an", "D", "Zwei Deutsche sind __ der Grippe gestorben."),
    ("streiten", "mit", "D", "Ich möchte nicht __ dir streiten."),
    ("streiten", "über", "A", "Die USA und Deutschland streiten __ eine neue Strategie."),
    ("teilnehmen", "an", "D", "Nordkorea nimmt __ der Fußball-WM teil."),
    ("telefonieren", "mit", "D", "Hast du schon __ dem Arzt telefoniert?"),
    ("sich treffen", "mit", "D", "Die Kanzlerin trifft sich täglich __ ihrem Pressesprecher."),
    ("sich treffen", "zu", "D", "Sie treffen sich nur __ einem kurzen Gespräch."),
    ("überreden", "zu", "D", "Kann ich dich __ einem Glas Wein überreden?"),
    ("sich unterhalten", "mit", "D", "Der Sänger unterhält sich __ dem Bassisten."),
    ("sich unterhalten", "über", "A", "Die Modedesigner unterhalten sich __ die neuesten Trends."),
    ("sich verabreden", "mit", "D", "Heute verabrede ich mich __ einer Freundin."),
    ("sich verabschieden", "von", "D", "Nun wollen wir uns __ euch verabschieden."),
    ("vergleichen", "mit", "D", "Vergleichen Sie München __ Berlin."),
    ("sich verlassen", "auf", "A", "__ mich kann man sich verlassen."),
    ("sich verlieben", "in", "A", "Britta hat sich __ das alte Bauernhaus verliebt."),
    ("sich verstehen", "mit", "D", "Daniel versteht sich gut __ seinem Chef."),
    ("verstehen", "von", "D", "Verstehst du etwas __ Elektrik?"),
    ("sich vorbereiten", "auf", "A", "Karl bereitet sich __ eine Präsentation vor."),
    ("warnen", "vor", "D", "Man hatte ihn __ den hohen Kosten für das alte Auto gewarnt."),
    ("warten", "auf", "A", "Hier wartet man lange __ einen Bus."),
    ("sich wenden", "an", "A", "Bitte wenden Sie sich __ die Buchhaltung."),
    ("werden", "zu", "D", "Unter null Grad wird Wasser __ Eis."),
    ("wissen", "von", "D", "Ich weiß nichts __ neuen Computern für unser Team."),
    ("sich wundern", "über", "A", "Viele Deutsche wundern sich __ die plötzlich so hohen Stromkosten."),
    ("zuschauen", "bei", "D", "Kann ich dir __ der Reparatur zuschauen?"),
    ("zusehen", "bei", "D", "Willst du mir __ dem Kochen zusehen?"),
    ("zweifeln", "an", "D", "John zweifelt __ , dass sein Sohn die Wahrheit gesagt hat."),
]

prepositions = {
    "für", "um", 
    "aus", "bei", "mit", "nach", "seit", "von", "zu", 
    "an", "auf", "in", "über", "vor"
    }

cases_dict = {"A": "Accusative", "D": "Dative", "G": "Genitive"}
# Function to play the game in mode 1
def get_user_choice(options):
    """Helper function to handle user input."""
    while True:
        user_input = input(f"Your choice (1 - {len(options)}): ").strip()
        if user_input.lower() == 'q':
            return None
        if user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= len(options):
                return options[choice - 1]
        print("Invalid choice. Please try again.")

def mode_1():
    """Mode where the user guesses only the preposition."""
    verb, correct_preposition, _, sentence = random.choice(verbs)
    print(f"\nVerb: {verb}")
    print(f"Example sentence: {sentence}")

    options = list(random.sample(prepositions, 4)) + [correct_preposition]
    random.shuffle(options)

    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")

    user_choice = get_user_choice(options)
    if user_choice is None:
        return False

    if user_choice == correct_preposition:
        print("✅ Correct! Well done.")
    else:
        print(f"❌ Oops! The correct preposition is '{correct_preposition}'.")
    
    return True

def mode_2():
    """Mode where the user guesses the preposition and the grammatical case."""
    verb, correct_preposition, correct_case, sentence = random.choice(verbs)
    print(f"\nVerb: {verb}")
    print(f"Example sentence: {sentence}")

    options_preposition = list(random.sample(prepositions, 4)) + [correct_preposition]
    random.shuffle(options_preposition)

    for idx, option in enumerate(options_preposition, 1):
        print(f"{idx}. {option}")

    preposition_choice = get_user_choice(options_preposition)
    if preposition_choice is None:
        return False

    if preposition_choice == correct_preposition:
        print(f"✅ Correct preposition: '{preposition_choice}'")
        
        case_options = list(cases_dict.values())
        random.shuffle(case_options)

        for idx, option in enumerate(case_options, 1):
            print(f"{idx}. {option}")

        case_choice = get_user_choice(case_options)
        if case_choice is None:
            return False

        if case_choice == cases_dict[correct_case]:
            print("✅ Correct case! Well done.")
        else:
            print(f"❌ Oops! The correct case is '{cases_dict[correct_case]}'.")
    else:
        print(f"❌ Oops! The correct preposition is '{correct_preposition}'.")
    
    return True

def main():
    """Main function to start the game."""
    print("\n🎮 Welcome to the German Verb-Preposition Game!")
    print("1️⃣  Guess only the preposition")
    print("2️⃣  Guess the preposition and case")
    print("Press 'q' to quit at any time.")

    while True:
        mode = input("\nChoose a mode (1 or 2): ").strip()
        if mode == '1':
            while mode_1():
                pass
        elif mode == '2':
            while mode_2():
                pass
        elif mode.lower() == 'q':
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    print("\n👋 Thanks for playing! Bis bald!")

if __name__ == "__main__":
    main()
