from pythonvilag_website import db
from pythonvilag_website.models import Assessment, Category, Lesson, Mentors


def setup_db() -> None:  # noqa: PLR0915
    # Category
    category_python = Category(
        category="python",
        subcategory="python_alapjai",
        title="Python alapjai",
        description="A Python alapjai sorozatban megismerjük miért is olyan népszerű a Python programozási nyelv. A szükséges előkészületek után megírjuk első programunkat és onnan lépésenként sajátítjuk el a szükséges ismereteket. Nem kell félni, ez a kurzus semmilyen előismeretet nem igényel.",
        image="python_alapjai.png",
    )
    db.session.add(category_python)

    category_extra = Category(
        category="extra",
        subcategory="erettsegi_feladatok",
        title="Érettségi feladatok",
        description="Érettségi feladatok kidolgozásai",
        image="python.png",
    )
    db.session.add(category_extra)

    category_project = Category(
        category="project",
        subcategory="pythonvilag_weboldal",
        title="Python Világ weboldal",
        description="A weboldal forráskódja",
        image="python.png",
    )
    db.session.add(category_project)

    # Lesson
    lesson_1_python = Lesson(
        order=0,
        date_posted="2022.08.17.",
        title="Bevezetés és kurzusinformációk",
        url="00_Bevezetes_es_kurzusinformaciok",
        description="Ebben a leckében ismerjük meg a programozó környezetet, a tananyag felépítését, illetve a leckék során használt jelölésrendszert.",
        secret_word="Alma",  # noqa: S106
        image="python_alapjai.png",
        category_id=1,
    )
    db.session.add(lesson_1_python)

    lesson_2_python = Lesson(
        order=1,
        date_posted="2022.08.18.",
        title="A Python programozási nyelvről",
        url="01_A_Python_programozasi_nyelvrol",
        description="Itt lesz szó arról, hogy miért olyan szuper a Python programozási nyelv, de a hiányosságokról is fogunk beszélni. Megértjük hogyan működik a futtatási folyamat nagy vonalakban, és hogy hol érdemes segítséget kérni ha elakadtál.",
        secret_word="Banán",  # noqa: S106
        image="python_alapjai.png",
        category_id=1,
    )
    db.session.add(lesson_2_python)

    lesson_3_python = Lesson(
        order=2,
        date_posted="2022.08.19.",
        title="Változók, típusok és műveleteik",
        url="02_Valtozok_tipusok_es_muveleteik",
        description="Bemutatásra kerülnek a változók, melyek az alapját képzik bármely programozásos feladatnak. Megtanulunk számokat/szöveget elmenteni a memóriába és különböző műveleteket végrehajtani rajtuk.",
        secret_word="Citrom",  # noqa: S106
        image="python_alapjai.png",
        category_id=1,
    )
    db.session.add(lesson_3_python)

    lesson_4_python = Lesson(
        order=3,
        date_posted="2022.08.19.",
        title="Komment, kiírás és bekérés",
        url="03_Komment_kiiras_bekeres",
        description="Kiegészítjük a kódunkat megértést segítő megjegyzésekkel és megtanulunk kommunikálni a külvilággal adatok bekérésén és eredmények kiírásán keresztül.",
        secret_word="Dió",  # noqa: S106
        image="python_alapjai.png",
        category_id=1,
    )
    db.session.add(lesson_4_python)

    lesson_5_python = Lesson(
        order=4,
        date_posted="2022.10.29.",
        title="Lista és dictionary",
        url="04_Lista_es_dictionary",
        description="A következő lépés, hogy megtanuljuk milyen formában tudunk több összetartozó adatot együtt tárolni. Megismerjük ezek között a fontos különbségeket, és hogy melyiket milyen körülmények között érdemes használni.",
        secret_word="Eper",  # noqa: S106
        image="python_alapjai.png",
        category_id=1,
    )
    db.session.add(lesson_5_python)

    # Assessment
    assessment_1_lesson_1_python = Assessment(
        order=1,
        question="Az alábbi módszerek közül, melyik NEM futtatja le a kód típusú cellát Google Colab-ban?",
        options="Lejátszás gomb a cella mellett\nEnter megnyomása\nShift és Enter megnyomása\nEnter megnyomása",
        answer="1",
        lesson_id=1,
    )
    db.session.add(assessment_1_lesson_1_python)

    assessment_2_lesson_1_python = Assessment(
        order=2,
        question="Kód cellában, milyen karakter segítségével futtathatunk Linux parancsokat?",
        options="!\n?\n#\n/",
        answer="1",
        lesson_id=2,
    )
    db.session.add(assessment_2_lesson_1_python)

    assessment_3_lesson_1_python = Assessment(
        order=3,
        question="Összesen hány leckéből áll a kurzus?",
        options="-1\n11\n13\n14",
        answer="14",
        lesson_id=3,
    )
    db.session.add(assessment_3_lesson_1_python)

    assessment_4_lesson_1_python = Assessment(
        order=4,
        question="Milyen karakterek közé vannak téve az általunk megadandó értékek a struktúrák jelölése során?",
        options="Zárójel ()\nSzögletes zárójel []\nKapcsos zárójel {}\nKacsacsőr <>",
        answer="Kacsacsőr <>",
        lesson_id=4,
    )
    db.session.add(assessment_4_lesson_1_python)

    assessment_1_lesson_2_python = Assessment(
        order=1,
        question="Mi történik,  ha hivatkozni próbálunk egy értékre,  melyet egy olyan cellában hoznuk létre, amit még nem futtatnunk le?",
        options="A másik cella is automatikusan lefut,  hogy ne kapjunk hibát\nHibát kapunk\nHibát kapunk",
        answer="2",
        lesson_id=5,
    )
    db.session.add(assessment_1_lesson_2_python)

    assessment_2_lesson_2_python = Assessment(
        order=2,
        question="A felsorolt tulajdonások közül melyik NEM igaz a Python programozási nyelvre?",
        options="Logikus és átlátható formázás\nRengeteg előre megírt kód\nEgyik leggyorsabb nyelv\nPlatform független",
        answer="Egyik leggyorsabb nyelv",
        lesson_id=6,
    )
    db.session.add(assessment_2_lesson_2_python)

    assessment_3_lesson_2_python = Assessment(
        order=3,
        question="Az alábbiak közül melyik területen nem optimális a Python használata?",
        options="Általános problémamegoldás\nFeladatok automatizálása\nGép tanulás\nMobil alkalmazás írása",
        answer="Mobil alkalmazás írása",
        lesson_id=7,
    )
    db.session.add(assessment_3_lesson_2_python)

    assessment_4_lesson_2_python = Assessment(
        order=4,
        question="Hogyan tudunk a Python kódban leírást kapni parancsokról?",
        options="segitseg()\nhelp()\nhelp_me()\nNem lehet leírást kapni a kódon belül",
        answer="help()",
        lesson_id=8,
    )
    db.session.add(assessment_4_lesson_2_python)

    assessment_1_lesson_3_python = Assessment(
        order=1,
        question="Miért használnuk változókat?",
        options="Hogy a kódot könnyen meg lehessen változtatni\nVáltozók használata nélkül hibát dob a programunk\nHogy a programunk gyorsabban fusson\nNem hasunálnuk változókat",
        answer="Hogy a kódot könnyen meg lehessen változtatni",
        lesson_id=9,
    )
    db.session.add(assessment_1_lesson_3_python)

    assessment_2_lesson_3_python = Assessment(
        order=2,
        question="Az alábbiak közül, melyik NEM létező típus?",
        options="float\nint\nnum\nstr",
        answer="num",
        lesson_id=10,
    )
    db.session.add(assessment_2_lesson_3_python)

    assessment_3_lesson_3_python = Assessment(
        order=3,
        question="Milyen karater használható, ha két szám osztási maradékára vagyunk kíváncsiak?",
        options="*\n%\n/\n//",
        answer="%",
        lesson_id=11,
    )
    db.session.add(assessment_3_lesson_3_python)

    assessment_4_lesson_3_python = Assessment(
        order=4,
        question="Hogyan tudunk egy szöveg utolsó karakterére hivatkozni?",
        options="string[-1]\nstring[0]\nstring[1]\nstring[inf]",
        answer="string[-1]",
        lesson_id=12,
    )
    db.session.add(assessment_4_lesson_3_python)

    assessment_5_lesson_3_python = Assessment(
        order=5,
        question="Milyen parancs használható egy szöveg hosszának meghatározására?",
        options="hossz()\nlength()\nlimit()\nlen()",
        answer="len()",
        lesson_id=13,
    )
    db.session.add(assessment_5_lesson_3_python)

    # Mentors
    mentors_corey_schafer = Mentors(
        order=1,
        channel_name="Corey Schafer",
        description="Developer and Designer who enjoys woodworking, kayaking, astronomy, and building stuff.",
        image="corey.png",
        youtube_link="https://www.youtube.com/c/Coreyms",
    )
    db.session.add(mentors_corey_schafer)

    mentors_sentdex = Mentors(
        order=2,
        channel_name="sentdex",
        description="I like to build things. Programming is neat.",
        image="sentdex.png",
        youtube_link="https://www.youtube.com/c/sentdex",
    )
    db.session.add(mentors_sentdex)

    mentors_networkchuck = Mentors(
        order=3,
        channel_name="NetworkChuck",
        description="Beard. Coffee. Tech. Youtube.",
        image="chuck.png",
        youtube_link="https://www.youtube.com/c/NetworkChuck",
    )
    db.session.add(mentors_networkchuck)

    mentors_paul_mcwhorter = Mentors(
        order=4,
        channel_name="Paul McWhorter",
        description="I am a former electrical engineer now working as a High School teacher.",
        image="paul.png",
        youtube_link="https://www.youtube.com/c/mcwhorpj",
    )
    db.session.add(mentors_paul_mcwhorter)

    db.session.commit()
