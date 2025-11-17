import random
attempts = 11

words = [
"abacus","abandon","ability","abolish","absence","academy","account","achieve","acquire","actress",
"address","advance","advisory","against","airline","airport","alcohol","alleged","already","amazing",
"analyst","anatomy","ancient","android","anxiety","anybody","anymore","anytime","apology","appears",
"appoint","approval","archery","archive","arrange","arrival","article","artisan","assault","attempt",
"attitude","attract","auction","average","aviation","balance","balloon","bargain","barrier","battery",
"because","bedroom","believe","benefit","between","bicycle","binding","biology","birthday","blanket",
"blankly","blessing","blizzard","brother","browser","buckets","builder","butcher","cabinet","caffeine",
"calculate","calendar","campaign","carrier","caution","ceiling","central","certain","champion","channel",
"chapter","charity","charmer","checkup","chemical","chicken","circuit","citizen","clarify","classroom",
"climate","closely","clothing","cluster","collect","college","combine","comfort","command","comment",
"company","compare","compete","complete","complex","concert","conduct","confirm","connect","consist",
"contact","contain","context","control","convert","correct","courage","courier","creative","crucial",
"culture","curious","current","cutting","dancing","danger","darkness","database","daughter","decided",
"declare","decline","decorate","defense","deliver","density","deposit","describe","desktop","desire",
"dessert","destroy","develop","diamond","digital","dinner","directly","disabled","disagree","disaster",
"discover","discuss","disease","dismiss","display","distance","distinct","district","dividing","divorce",
"document","domestic","dominant","donation","doubtful","dramatic","drawing","driver","dynamic","earning",
"economy","educate","effective","eighth","elected","elevator","emerging","emotion","employ","emptying",
"ending","endorse","engaged","enhance","enjoyed","enough","enquiry","ensure","entirely","entrance",
"episode","equation","equipment","ethical","evidence","exactly","examined","example","exchange","excited",
"execute","exercise","explicit","exposure","factory","faculty","failure","familiar","fashion","favorite",
"feature","federal","feedback","feeling","festival","fiction","fifth","filling","finance","finding",
"finished","fishing","fitness","flexible","focused","football","forecast","foreign","forever","formula",
"fortune","forward","founder","fragile","freedom","freshman","friendly","frustrate","function","gallery",
"gateway","general","generate","genuine","gesture","graphic","greater","greatest","happiness","hardware",
"heading","healthy","hearing","heavily","heaviness","helpful","heritage","highway","history","holiday",
"honesty","honorable","hospital","housing","however","humanity","hundred","hungry","identity","illegal",
"illusion","imagine","imaging","immediate","immense","immigrant","immunity","impact","impaired","imperial",
"implement","implied","improve","include","incoming","increase","indeed","indicate","indoor","industry",
"influence","inform","initial","innocent","inquiry","insight","install","instance","instead","intense",
"interact","interest","internal","internet","interval","introduce","involved","isolate","journey","justice",
"justify","keeping","kitchen","knowing","knowledge","landing","largest","leading","learned","lecture",
"library","license","limited","logical","looking","loyalty","machine","manager","married","massive",
"material","maximum","meaning","measure","medical","meeting","mention","message","midnight","million",
"mineral","minimum","minister","mission","mistake","modern","modestly","moment","monetary","morning",
"musical","mystery","natural","nearest","neither","network","nothing","notable","notice","notify",
"objective","observe","obvious","offense","officer","ongoing","opening","operate","opinion","opposite",
"optical","organic","outcome","outside","overall","overcome","package","painting","partial","partner",
"passage","passion","patient","pattern","peaceful","penalty","pension","perform","perhaps","permission",
"physical","picture","plastic","pleased","pleasure","popular","portion","position","positive","possible",
"possibly","pottery","precise","predict","premise","prepare","present","prevent","primary","printed",
"private","problem","process","produce","product","profess","program","project","promise","promote",
"property","propose","protect","provide","purpose","qualify","quality","quarter","radical","railway",
"rapidly","reached","reaction","reading","realize","receive","recently","recovery","reflect","refuse",
"regards","regional","regular","relation","release","relevant","relying","remember","reminder","remove",
"replace","request","require","research","reserve","respect","respond","response","restful","reveal",
"reverse","review","revised","rewarded","rhetoric","rhythmic","romantic","roughly","routine","satisfy",
"science","season","second","section","security","sensible","sentence","separate","service","setting",
"several","shortly","shoulder","similar","simpler","simplest","situation","society","soldier","somehow",
"sometimes","southern","speaker","special","species","sponsor","stadium","standard","standing","started",
"starting","station","storage","strategy","strength","strictly","student","studied","subject","succeed",
"success","suddenly","suggest","summary","support","suppose","surface","surgery","surprise","surround",
"survey","suspect","swimming","teacher","teaching","tension","terrible","testing","theater","therapy",
"therefore","thought","through","tonight","totally","tourism","towards","traffic","training","transfer",
"transmit","traveled","treatment","triangle","trouble","ultimate","umbrella","uncovered","undergo","understand",
"uniform","universal","unknown","unless","unusual","upgrade","upwards","valuable","variable","variety",
"various","vehicle","venture","version","veteran","victory","village","violent","visible","visitor",
"waiting","walking","warning","wealthy","weather","wedding","weekend","welcome","western","whether",
"whereas","whisper","wildlife","winning","without","working","writing","yourself"
]
   
x = random.randint(1,588)

chosen_word = words[x]

chosen_word_length = len(chosen_word)

print(chosen_word_length)

line = [0] * chosen_word_length

for i in range(0,chosen_word_length):
    line[i] = "_"

print(line)

while attempts != 0:
    y = str(input("Letter:"))
    
    if y in chosen_word:
        # Loop through each index and reveal all occurrences
        for i in range(chosen_word_length):
            if chosen_word[i] == y:
                line[i] = y
        
        print(line)
    else:
        print("fail")
        attempts = attempts - 1
        print("Attempts remaining:", attempts)

print("The answer is:", chosen_word)