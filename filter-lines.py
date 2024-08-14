# A script to filter lines that not includes a keyword
def filter_lines(text):
    lines = text.split('\n')
    filtered_lines = [line for line in lines if "İzmir" in line]
    paragraph = "\n".join(filtered_lines)
    return paragraph

# The text to be filtered
text = """
Kampanyanın Geçerli Olduğu Seçili Hatlar:

9€+vergilerle olan hatlar:

İstanbul Sabiha Gökçen - Aktau

İstanbul Sabiha Gökçen - Alexandria (EG) - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Atina (GR) - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Bakü - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Basel - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Batum - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Berlin - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Bratislava - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Brüksel

İstanbul Sabiha Gökçen - Budapeşte

İstanbul Sabiha Gökçen - Bükreş - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Cenevre - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Dortmund - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Duesseldorf - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Erivan - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Frankfurt - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Gence

İstanbul Sabiha Gökçen - Hamburg - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Hannover - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Kahire  - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Kişinev

İstanbul Sabiha Gökçen - Kopenhag - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Köln - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Kutaisi

İstanbul Sabiha Gökçen - Kuveyt - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Münih - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Nürnberg - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Prag - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Priştine - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Saraybosna - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Sofya - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Stuttgart - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Tiflis - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Tiran

İstanbul Sabiha Gökçen - Tuzla - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Üsküp - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Viyana - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Zagrep - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Zürih - İstanbul Sabiha Gökçen

Rotterdam - İstanbul Sabiha Gökçen

Ankara - Duesseldorf - Ankara

Ankara - Frankfurt - Ankara

Ankara - Hamburg - Ankara

Ankara - Köln - Ankara

Ankara - Stuttgart - Ankara

Ankara - Viyana - Ankara

Antalya - Basel

Antalya - Berlin

Antalya - Beyrut - Antalya

Antalya - Cenevre

Antalya - Dresden

Antalya - Duesseldorf

Antalya - Frankfurt

Antalya - Hamburg

Antalya - Kişinev

Antalya - Leipzig

Antalya - Münih

Antalya - Nürnberg

Antalya - Paris

Antalya - Tiflis - Antalya

Antalya - Zürih

Amman - Ankara

Amman - Antalya

İzmir - Bakü - İzmir

İzmir - Berlin

İzmir - Duesseldorf

İzmir - Frankfurt

İzmir - Üsküp - İzmir

Çukurova - Köln

Gaziantep - Köln

Kayseri - Köln

Duesseldorf - Çukurova

Duesseldorf - Gaziantep

Duesseldorf - Kayseri

Duesseldorf - Samsun

Duesseldorf - Trabzon

Kopenhag - Konya

Köln - Çukurova

Köln - Elazığ

Köln - Gaziantep

Köln - Kayseri

Rotterdam - Kayseri

19€ + vergilerle olan hatlar:

İstanbul Sabiha Gökçen - Amsterdam - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Bahreyn - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Birmingham - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Bologna - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Edinburg - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Eindhoven - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Helsinki - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Hurghada - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - İmam Humeyni

İstanbul Sabiha Gökçen - Londra (GB) - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Lyon - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Madrid - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Manchester - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Marsilya - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Milan - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Oslo - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Roma - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Rotterdam

İstanbul Sabiha Gökçen - Sharm El Sheikh - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Stockholm - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Venedik - İstanbul Sabiha Gökçen

Abu Dabi - İstanbul Sabiha Gökçen

Aktau - İstanbul Sabiha Gökçen

Beyrut - İstanbul Sabiha Gökçen

Dammam (SA) 00 - İstanbul Sabiha Gökçen

Erbil - İstanbul Sabiha Gökçen

Gence - İstanbul Sabiha Gökçen

Kişinev  - İstanbul Sabiha Gökçen

Paris - İstanbul Sabiha Gökçen

Şarja - İstanbul Sabiha Gökçen

Ankara - İmam Humeyni

Ankara - Krakow - Ankara

Ankara - Londra (GB) - Ankara

Ankara - Stockholm - Ankara

Ankara - Varşova - Ankara

Antalya - Krakow - Antalya

Antalya - Londra (GB)

Antalya - Manchester

Antalya - Saraybosna - Antalya

Antalya - Varşova - Antalya

Erbil - Ankara

Kişinev  - Antalya

Talin - Antalya

Çukurova - Duesseldorf

Gaziantep - Duesseldorf

İzmir - Krakow - İzmir

İzmir - Londra (GB) - İzmir

İzmir - Varşova - İzmir

Kayseri - Duesseldorf

Konya - Kopenhag

Samsun - Duesseldorf

Trabzon - Duesseldorf

29€ + vergilerle olan hatlar:

İstanbul Sabiha Gökçen - Abu Dabi

İstanbul Sabiha Gökçen - Bağdat - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Barcelona - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Beyrut

İstanbul Sabiha Gökçen - Dammam (SA) 00

İstanbul Sabiha Gökçen - Erbil

İstanbul Sabiha Gökçen - Paris

İstanbul Sabiha Gökçen - Şarja

İstanbul Sabiha Gökçen - Tebriz

Brüksel - İstanbul Sabiha Gökçen

Dubai (AE) 00 - İstanbul Sabiha Gökçen

Kutaisi - İstanbul Sabiha Gökçen

Maskat - İstanbul Sabiha Gökçen

Riyad - İstanbul Sabiha Gökçen

Ankara - Amman

Ankara - Erbil

İmam Humeyni - Ankara

Kayseri - Rotterdam

39€ + vergilerle olan hatlar:

İstanbul Sabiha Gökçen - Dubai (AE) 00

İstanbul Sabiha Gökçen - Maskat

İstanbul Sabiha Gökçen - Riyad

Amman - İstanbul Sabiha Gökçen

Budapeşte - İstanbul Sabiha Gökçen

Cidde - İstanbul Sabiha Gökçen

İmam Humeyni - İstanbul Sabiha Gökçen

Ankara - Almatı

Antalya - Amman

Antalya - Çimkent

49€ + vergilerle olan hatlar:

İstanbul Sabiha Gökçen - Basra - İstanbul Sabiha Gökçen

İstanbul Sabiha Gökçen - Cidde

İstanbul Sabiha Gökçen - Çimkent

Tebriz - İstanbul Sabiha Gökçen

Almatı - Ankara

Dubai (AE) 00 - Antalya

59€ + vergilerle olan hatlar:

İstanbul Sabiha Gökçen -  Oš

İstanbul Sabiha Gökçen - Almatı

İstanbul Sabiha Gökçen - Bişkek

Antalya - Almatı

Antalya - Bişkek

Antalya - Petersburg

Çimkent - Antalya

69€ + vergilerle olan hatlar:

İstanbul Sabiha Gökçen - Nursultan

 Oš - İstanbul Sabiha Gökçen

Almatı - İstanbul Sabiha Gökçen

Bişkek - İstanbul Sabiha Gökçen

Doha - İstanbul Sabiha Gökçen

Çimkent - İstanbul Sabiha Gökçen

Antalya - Moskova

Antalya - Nursultan

Bişkek - Antalya

İzmir - Moskova

Nursultan  - Antalya

79€ + vergilerle olan hatlar:

Nursultan  - İstanbul Sabiha Gökçen

Kazablanka - İstanbul Sabiha Gökçen

Moskova - İzmir

Petersburg - Antalya

İstanbul Sabiha Gökçen - Amman

89€ + vergilerle olan hatlar:

İstanbul Sabiha Gökçen - Kazablanka

İstanbul Sabiha Gökçen - Doha

Moskova - Antalya

Moskova – Antalya

DİĞER:

Frankfurt - Antalya(1€+vergilerle)

Antalya - Köln(1€+vergilerle)

Brüksel - Antalya(1€+vergilerle)

Kahire  - Antalya(1€+vergilerle)

Sharm El Sheikh - Antalya(1€+vergilerle)

Zürih - Antalya(1€+vergilerle)

Viyana - Antalya(1€+vergilerle)

Münih - Antalya(1€+vergilerle)

İzmir - Köln(2€+vergilerle)

Antalya - Hannover(2€+vergilerle)

Antalya - Brüksel(2€+vergilerle)

Bremen - Antalya(2€+vergilerle)

Antalya - Aalborg(2€+vergilerle)

Antalya - Sofya(2€+vergilerle)

Antalya - Billund(2€+vergilerle)

Cenevre - Antalya(2€+vergilerle)

Antalya - Münster / Osnabrück(2€+vergilerle)

Frankfurt - İzmir(2€+vergilerle)

Antalya - Paderborn / Lippstadt(3€+vergilerle)

İzmir - Stuttgart(3€+vergilerle)

Antalya - Stuttgart(3€+vergilerle)

Paris - Antalya(3€+vergilerle)

Manchester - Antalya(3€+vergilerle)

Antalya - Üsküp(3€+vergilerle)

Hurghada - Antalya(3€+vergilerle)

Antalya - Priştine(3€+vergilerle)

Antalya - Tiran(3€+vergilerle)

Duesseldorf - İzmir(3€+vergilerle)

Duesseldorf - Antalya(3€+vergilerle)

Hamburg - Antalya(3€+vergilerle)

Bükreş - Antalya(4€+vergilerle)

Berlin - İzmir(4€+vergilerle)

Berlin - Antalya(4€+vergilerle)

Hannover - Antalya(4€+vergilerle)

Dresden - Antalya(5€+vergilerle)

Leipzig - Antalya(5€+vergilerle)

Antalya - Helsinki(5€+vergilerle)

Antalya - Norrköping(5€+vergilerle)

Stuttgart - İzmir(5€+vergilerle)

Stuttgart - Antalya(5€+vergilerle)

Münster / Osnabrück - Antalya(6€+vergilerle)

Sofya - Antalya(6€+vergilerle)

Antalya - Bükreş(6€+vergilerle)

Helsinki - Antalya(6€+vergilerle)

Antalya - Stockholm(8€+vergilerle)

Üsküp - Antalya(8€+vergilerle)

Antalya - Goteborg(8€+vergilerle)

Priştine - Antalya(8€+vergilerle)

Tiran - Antalya(8€+vergilerle)

Antalya - Viyana(8€+vergilerle)

Antalya - Bremen(8€+vergilerle)

Köln - Antalya(11€+vergilerle)

Londra (GB) - Antalya(11€+vergilerle)

Nürnberg - Antalya(11€+vergilerle)

Köln - İzmir(11€+vergilerle)

Antalya - Hurghada(11€+vergilerle)

Antalya - Kahire (11€+vergilerle)

Antalya - Sharm El Sheikh(11€+vergilerle)

Stockholm - Antalya(12€+vergilerle)

Antalya - Talin(12€+vergilerle)

Goteborg - Antalya(13€+vergilerle)

Tiran - İstanbul Sabiha Gökçen(14€+vergilerle)

Elazığ - Köln(14€+vergilerle)

Aalborg - Antalya(14€+vergilerle)

Basel - Antalya(14€+vergilerle)

Kopenhag - Antalya(14€+vergilerle)

Billund - Antalya(15€+vergilerle)

Antalya - Kopenhag(16€+vergilerle)

Norrköping - Antalya(16€+vergilerle)

Paderborn / Lippstadt - Antalya(22€+vergilerle)

Antalya - Dubai (AE) 00(60€+vergilerle)

Antalya - Kazan(92€+vergilerle)

Kazan - Antalya(110€+vergilerle)

"""

result = filter_lines(text)

print(result)
