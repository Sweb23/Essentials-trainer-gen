import re
from tkinter import *
from tkinter import filedialog
import trainer_classes as tc
import random

window = Tk()



path_trtypes = filedialog.askopenfilename(defaultextension=".txt",initialfile="trainer_types.txt",parent=window,
                                             title="Open trainer types file",
                                                        filetypes=[("All files",""),("Text files",".txt")])


ID_regex = {"regexes":[".*BIRDKEEPER.*",".*BUGCATCHER.*",".*CHANNELER.*",".*FISHERMAN|SAILOR|SWIMMER.*",
                       ".*HIKER.*",
                       ".*ROCKER.*",".*BLACKBELT|CRUSHGIRL|CRUSHKIN.*",".*DRAGONTAMER.*",".*PSYCHIC.*",
                       ".*TEAMROCKET.*",
                       ".*AROMA.*",".*BIKER.*",".*BURGLAR.*",".*CUEBALL.*",".*REPORTER.*",
                       ".*WORKER.*",".*HIKER.*",".*SUPERNERD.*"],
            "types":[["FLYING"],["BUG"],["GHOST"],["WATER"],["ROCK","GROUND"],["ELECTRIC"],["FIGHTING"],
                     ["DRAGON"],
                     ["PSYCHIC"],["POISON"],
                     ["GRASS","POISON"],["FIGHTING","POISON","FIRE"],["POISON","FIRE"],
                     ["DARK","POISON","FIGHTING"],["FLYING","ELECTRIC"],
                     ["ROCK","GROUND","FIGHTING"],["ROCK","GROUND","FIGHTING"],["POISON","ELECTRIC"]]}

Legendaries = ["MEWTWO","ARTICUNO","ZAPDOS","MOLTRES","RAIKOU","ENTEI","SUICUNE","LUGIA","HOOH","REGIROCK",
               "REGICE","REGISTEEL","LATIAS","LATIOS","KYOGRE","GROUDON","RAYQUAZA","UXIE","MESPRIT","AZELF",
               "DIALGA","PALKIA","GIRATINA","HEATRAN","REGIGIGAS","CRESSELIA","COBALION","TERRAKION","VIRIZION",
               "TORNADUS","THUNDURUS","RESHIRAM","ZEKROM","LANDORUS","KYUREM","XERNEAS","YVELTAL","ZYGARDE",
               "TYPENULL","SILVALLY","COSMOG","COSMOEM","SOLGALEO","LUNALA","NECROZMA","TAPUKOKO","TAPULELE",
                "TAPUBULU", "TAPUFINI","ZACIAN","ZAMAZENTA","ETERNATUS","KUBFU","URSHIFU", "GLASTRIER",
               "SPECTRIER","CALYREX","REGIDRAGO","REGIELEKI","MEW","CELEBI","JIRACHI","DEOXYS","PHIONE",
               "MANAPHY","DARKRAI","SHAYMIN","ARCEUS","VICTINI","KELDEO","MELOETTA","GENESECT","DIANCIE",
               "HOOPA","VOLCANION","MAGEARNA","MARSHADOW","ZERAORA","METLAN","MELMETAL","ZARUDE"]
               
LoseTexts = ["...","A very good battle, indeed!","Breathtaking!","You're too good for me!","Defeated! Oh my!",
             "Washed out!","You didn't have to win so convincingly!","Our teamwork failed!"]

def launch():
    AllTrTypes = []
    with open(path_trtypes,'r',encoding='utf-8') as f:
        print("Retrieving and formatting trainer types...")
        s = f.read()
        
        tr_types = s.split("[")
        
        tr_types = tr_types[1:]
        
        
        #print(tr_types)

        for t in tr_types:
            # Split along \n
            ind_type = t.split("\n")
            
            #Trainer ID
            ind_type[0] = ind_type[0][:len(ind_type[0])-1]
            preferredTypes = []
            #Exclude Pokemon Trainers, rivals, leaders, elite4 and champion
            
            if (not specialTr.get()) and re.search(r"POKEMONTRAINER.*|RIVAL.*|LEADER.*|ELITEFOUR.*|CHAMPION.*",ind_type[0]) != None:
                continue
            else:
                #Look for preferred types
                for i in range(len(ID_regex["regexes"])):
                    if re.search(ID_regex["regexes"][i],ind_type[0]) != None:
                        preferredTypes = ID_regex["types"][i]
                g = None
                #Look for gender
                i = 1
                while i < len(ind_type) and g == None:
                    if re.search("Male$",ind_type[i]) != None:
                        g = "M"
                    elif re.search("Female$",ind_type[i]) != None:
                        g = "F"
                    i += 1
                
                AllTrTypes += [tc.TrType(ind_type[0],g,preferredTypes)]
                
        for t in AllTrTypes:
            print(t)
            
    path_pokemon = filedialog.askopenfilename(defaultextension=".txt",initialfile="pokemon.txt",parent=window,
                                                 title="Open pokemon file",
                                                            filetypes=[("All files",""),("Text files",".txt")])

    AllPokemon = []

    def trim_brackets(s):
        return s[1:len(s)-1]

    def types_formatting(s):
        s = s.split("Types = ")
        s = s[1]
        s = s.split(",")
        n = len(s)
        s[n-1] = s[n -1][:len(s[n-1]) - 1]
        return s

    def buildType(type):
        Types = [True if type in AllTypes[i] else False for i in range(len(AllTypes))]
        Types = [AllPokemon[i] for i in range(len(AllPokemon)) if Types[i]]
        return Types

    with open(path_pokemon,'r',encoding='utf-8') as f:
        print("Retrieving and formatting Pokémon data (this may take a while)...")
        s = f.read()
        
        AllPokemon = re.findall(r"\[.+\]",s)
        
        AllPokemon = list(map(trim_brackets,AllPokemon))
        
        AllTypes = re.findall(r"Types =.+\n",s)
        AllTypes = list(map(types_formatting,AllTypes))
        
        if not toggleLeg.get():
            # Filter out legendaries
            index_del = []
            for p in AllPokemon:
                if p in Legendaries:
                    index_del.append(AllPokemon.index(p))
                    
                    
            AllPokemon = [AllPokemon[i] for i in range(len(AllPokemon)) if i not in index_del]
            AllTypes = [AllTypes[i] for i in range(len(AllTypes)) if i not in index_del]
        
        print(len(AllPokemon))
        
        
        
        print(len(AllTypes))
        
        WaterTypes = buildType("WATER")
        GrassTypes = buildType("GRASS")
        FireTypes = buildType("FIRE")
        NormalTypes = buildType("NORMAL")
        FightingTypes = buildType("FIGHTING")
        FlyingTypes = buildType("FLYING")
        PoisonTypes = buildType("POISON")
        GroundTypes = buildType("GROUND")
        RockTypes = buildType("ROCK")
        BugTypes = buildType("BUG")
        GhostTypes = buildType("GHOST")
        SteelTypes = buildType("STEEL")
        ElectricTypes = buildType("ELECTRIC")
        PsychicTypes = buildType("PSYCHIC")
        IceTypes = buildType("ICE")
        DragonTypes = buildType("DRAGON")
        DarkTypes = buildType("DARK")
        FairyTypes = buildType("FAIRY")
        
    #N = int(input("Enter the number of trainers to generate : "))
    N = spinval.get()

    path_output = filedialog.asksaveasfilename(defaultextension=".txt",initialfile="Output",parent=window,
                                                 title="Save generated trainers",
                                                            filetypes=[("All files",""),("Text files",".txt")])

    def choose_pkmn(type):
        # Big else/if tower : very ugly but faster (I think)
        if type == "WATER":
            return random.choice(WaterTypes)            
        elif type == "GRASS":
            return random.choice(GrassTypes)
        elif type == "FIRE":
            return random.choice(FireTypes)
        elif type == "NORMAL":
            return random.choice(NormalTypes)
        elif type == "FIGHTING":
            return random.choice(FightingTypes)
        elif type == "FLYING":
            return random.choice(FlyingTypes)
        elif type == "POISON":
            return random.choice(PoisonTypes)
        elif type == "GROUND":
            return random.choice(GroundTypes)
        elif type == "ROCK":
            return random.choice(RockTypes)
        elif type == "BUG":
            return random.choice(BugTypes)
        elif type == "GHOST":
            return random.choice(GhostTypes)
        elif type == "STEEL":
            return random.choice(SteelTypes)
        elif type == "ELECTRIC":
            return random.choice(ElectricTypes)
        elif type == "PSYCHIC":
            return random.choice(PsychicTypes)
        elif type == "ICE":
            return random.choice(IceTypes)
        elif type == "DRAGON":
            return random.choice(DragonTypes)
        elif type == "DARK":
            return random.choice(DarkTypes)
        elif type == "FAIRY":
            return random.choice(FairyTypes)
            

    with open(path_output,'w') as f:
        print("Writing output (this may take a while)...")
        f.write("# Copy/paste the contents of this file in the trainers.txt file\n")
        # Generate N random trainers
        trainers = [""]*N
        for i in range(N):
            trainers[i] = tc.IndividualTrainer(random.choice(AllTrTypes))
        
        # Write each trainer into output file
        for i in range(N):
            f.write("#----------------\n")
            f.write(f"[{trainers[i].type.ID},{trainers[i].name}]\n")
            f.write(f"LoseText = {random.choice(LoseTexts)}\n")
            pkNb = random.randint(1,6)
            if not toggleLvl.get():
                levelRange = random.randint(3,98)

                
            for j in range(pkNb):
                # Choose a random Pokémon among one of the trainer's types chosen at random
                if trainers[i].type.preferredTypes != []:
                    pkmn = choose_pkmn(random.choice(trainers[i].type.preferredTypes))
                else:
                    pkmn = random.choice(AllPokemon)
                if not toggleLvl.get():
                    pkmnLevel = levelRange + random.randint(-2,2)
                else:
                    pkmnLevel = random.randint(spinMin.get(),spinMax.get())
                    
                f.write(f"Pokemon = {pkmn},{pkmnLevel}\n")
        print("Done!")


specialTr = IntVar()
check = Checkbutton(window, text='Include special trainers (Gym leaders, Elite4,...)', variable=specialTr,
        onvalue=1, offvalue=0)

toggleLeg = IntVar()
check2 = Checkbutton(window, text='Include legendaries & mythicals', variable=toggleLeg,
        onvalue=1, offvalue=0)

spinMin = IntVar()
spinMax = IntVar()
spinMin.set(1)
spinMax.set(100)

def updateLimits():
    spboxMin.configure(to=spinMax.get() - 1)
    spboxMax.configure(from_=spinMin.get() + 1)

Label(window,text="Min").grid(row=4,column=0)
spboxMin = Spinbox(window, from_=1.0, to=100, textvariable=spinMin, state='readonly',
                   disabledbackground="#a6a6a6", width=3, command=updateLimits)
spboxMin.grid(row=4,column=1)
Label(window,text="Max").grid(row=4,column=2)
spboxMax = Spinbox(window, from_=1, to=100, textvariable=spinMax, state='readonly',
                   disabledbackground="#a6a6a6", width=3, command=updateLimits)
spboxMax.grid(row=4,column=3)

def LvlVisibility():
    if toggleLvl.get() == 0:
        spboxMin.configure(state="disabled")
        spboxMax.configure(state="disabled")
    else:
        spboxMin.configure(state="readonly")
        spboxMax.configure(state="readonly")



toggleLvl = IntVar()
toggleLvl.set(1)
check3 = Checkbutton(window, text='Toggle level range', variable=toggleLvl, onvalue=1, offvalue=0,
                     command=LvlVisibility)



Label(window,text="Number of trainers to generate").grid(row=2,column=0)
spinval = IntVar()
lvlSpin = Spinbox(window, from_=1.0, to=100.0, textvariable=spinval, state='readonly', width=3)
lvlSpin.grid(row=2,column=1)



launchButton = Button(window, text="Generate", command=launch)

check.grid(row=0,column=0)
check2.grid(row=1,column=0)
check3.grid(row=3,column=0)
launchButton.grid(row=10,column=0)
Button(window,text="Quit", command=window.destroy).grid(row=11,column=0)



window.mainloop()