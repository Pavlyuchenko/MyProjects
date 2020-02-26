string = """* Vyměnit žárovku.   Change the bulb.
* Zabít hřebík.   Nail the nail.
* Bagr   Excavator
* sekačka   lawn mower
* kladivo   hammer
* kleště    pliers
* šroubovák   screwdriver
* Kape kohoutek. x2   The tap/faucet is dripping.
* Nechat si spravit tekoucí střechu.    Have the leaking roof fixed.
* Vynést odpadky.   Go with garbage.
* Slepit zlomené kousky kachliček dohromady.    Stick broken pieces of tiles together.
* spravit x2    fix, repair
* vyměnit povlečení    change bedlinen
* ustlat postel    make the bed
* utřít prach    do the dusting
* vytřít podlahu    mop the floor
* vysát koberec   vacuum the carpet
* umýt nádobí x2    wash the dishes/do the washing up
* dobře vybavený    well-equipped
* spotřebič   appliance
* plovoucí podlaha  floating floor
* vyjednávat cenu   negotiate the price
* lustr    chandelier
* lehátko, křeslo   deckchair
* houpací křeslo    rocking armchair
* poschoďová postel    bunk bed
* záclona   curtain
* žaluzie   blind
* knihovnička    bookcase
* regálová knihovnička   bookshelf
* noční stolek  bedside  table
* zásuvka   socket
* zastrčit něco do zásuvky   plug sth in the socket
* nájemník   tenant
* majitel domu x2    landlord/landlady
* měsíční nájem(né)   monthly rent
* vyplatit hypotéku   pay off mortgage
* úroky   interests
* dostat půjčku   get a loan
* skončit v dluzích   end up in debts
* být v mínusu    be in the red
* stavební spořitelna   building society
* našetřit peníze   save up money
* být úlevou pro někoho   be a relief for sb
* pronajmout si byt   rent a flat
* studentská kolej x3   student's hall of residence, dorm, dortmitories
* omšelý, zchátralý   shabby
* odlehlý   remote
* zanedbaný     neglected
* zaneřáděný    messy
* příjezdová cesta, vjezd x2     driveaway, drive
* krytý vchod, veranda    porch
* točité schodiště   spiral staircase
* madlo zábradlí x2    banister, railings
* došková střecha     thatched roof
* obývací pokoj, salónek    lounge
* vstupní hala,   předsíň hall
* karavan    caravan
* chata, bouda, vrátnice     lodge
* domov důchodců    retirement home
* dětský domov   foster home
* znečištěný vzduch     polluted air
* smog visící nad městem     smog hanging above the city
* zelené prostředí   green spaces
* dopravní zácpa     traffic jam
* dojíždění do práce     commute to work
* drby se šíří   gossips are spreading
* závistivý   jealous
* pěstovat ovoce a zeleninu   grow fruit and vegetables
* sekat trávník   mow the lawn
* sekat dřevo    chop wood
* plít x2     weed out/eliminate the weed
* Idiom: velmi bezpečný    safe as houses
* Idiom: vycházet (s někým) dobře    get on like a house on fire
* Idiom: Sníst u někoho hodně jídla   Eat someone out of house and home
* Idiom: Starej se sám o sebe!    Get your own house in order!
* Idiom: být na účet podniku (v restauraci)   be on the house
* Idiom: Mít střechu nad hlavou   Have roof over your head
* Idiom: Mít nereálné sny.   Build castles in the air.
* Idiom: podvést někoho   lead someone up the garden path
* Idiom: vzít vše    take everything but the kitchen sink
* Idiom: plýtvat penězi   throw money down the drain
* Idiom: mít nepříjemné tajemství x2    have skeleton in the cupboard/closet
* Idiom: Všude dobře, domá nejlíp.  There's no place like home.
* Idiom: uspět v něčem a neočekávat žádné další komplikace    be home and dry
* Idiom: udělat si pohodlí    make yourself at home
* Idiom: nepříjemný fakt      home truth
* zalévat kytky   water the flowers
* získat    obtain
* finančně zachránit    bail out
* rozpadnout se   fall apart
* odpad, kanál, stoka   drain
* Střecha byla odfouknuta.   The roof was blown off/away.
* skládka x2    dump, landfill
* normální domek    detached house
* pomyslná/smyšlená situace   imaginary situation
* statkářův dům   farmhouse
* hausbót   houseboat
* panství   mansion
* mobilní dům   mobile home
* dvojdomek   semi-detached house
* řadovka   terraced house
* chata (došková)   thatched cottage
* velký dům   villa
* podkroví  attic
* balkón    balcony
* suterén   basement
* sklep   cellar
* skleník    conservatory
* přístavba  extension
* plot   fence
* záhon   flower bed
* vstupní branka    gate
* živý plot   hedge
* odpočívadlo   landing
* trávník   lawn
* cestička  path
* terasa, nádvoří   patio
* okenice    shutters
* posouvací dveře    sliding doors
* realitní makléř    estate agent
* krásně zrekonstruovaný     beatifully restored
* okouzlující   charming
* současný, moderní   contemporary
* příznivě položený   conveniently located
* útulný    cosy
* namačkaný   cramped
* zruinovaný    dilapidated
* masivní    substantial
* živá oblast   lively area
* nedaleko, poblíž   nearby
* izolovat/zateplit   insulate
* na předměstí x2    on the outskirts, in the suburbs
* nemovitost     property
* slogan     slogan
* pomoci někomu    give somebody a hand
* ignorovat něco    turn a blind eye to something
* hodně se snažit   make a big effort
* užívat si něco    to have the time of your life
* promluvit si s někým    to have a word with somebody
* skontaktovat se s někým   to get in touch with somebody
* úryvek, výňatek/vyjmout, vybrat    excerpt
* navrhnout něco    make a proposal
* získat zaměstnání   gain employment
* sebeúcta, hrdost   self-esteem
* záchvat   seizure
* spát pod širákem   sleep rough
* číslo, údaj   figure
* ubytování   accommodation
* poprat se s něčím to   tackle sth
* městská rada   city council"""
import pyperclip

arr = string.split("\n")
new = []

for word in arr:
    new.append(word.replace("* ", "").replace("     ", "-").replace("    ", "-").replace("   ", "-").replace("  ", "-") + ";")


res = ""
for i in new:
    res += i

pyperclip.copy(res)
