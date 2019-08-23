from collections import defaultdict
import operator
c1 = {
  "head":[301.87,"Wastewalker Helm"], #T4 BIS
  "neck":[97.65,"Natasha's Choker"],
  "shoulder":[239.02,"Wastewalker Shoulderpads"], #T4 BIS
  "back":[96.22,"Cloak of the Inciter"],
  "chest":[160.48,"Auchenai Monk's Tunic"],
  "wrist":[97.84,"Nightfall Wristguards"], #T4 2nd BIS
  "hands":[150.26,"Fel Leather Gloves"], #T4 BIS
  "waist":[161.68,"Girdle of the Deathdealer"], #T4 BIS
  "legs":[204.09,"Fel Leather Leggings"],
  "feet":[157.19,"Edgewalker Longboots"], #T4 BIS
  "finger":[105.0,"Slayer's Mark of Redemption"],
  "trinket":[59.0,"Bloodlust Brooch"],
  "weapons":[276.0,"Vindicator's Brand"],
  "ranged":[63.62,"Mama's Insurance (Gun)"]
}
c2 = {
  "head":[126.08,"Voidheart Crown"],
  "neck":[54.09,"Brooch of Heightened Potential"],
  "shoulder":[75.05,"Frozen Shadoweave Shoulders"],
  "back":[44.5,"Sethekk Oracle Cloak"],
  "chest":[92.2,"Auchenai Anchorite's Robe"],
  "wrist":[44.5,"Crimson Bracers of Gloom"],
  "hands":[109.96,"Voidheart Gloves"],
  "waist":[66.75,"Girdle of Ruination"],
  "legs":[70.84,"Aran's Sorcerous Slacks"],
  "feet":[55.05,"79.35"],
  "finger":[46.37,"Violet Signet of the Archmage"],
  "trinket":[53.8,"Quagmirran's Eye"],
  "weapons":[136.5+46.72,"Continuum Blade; Lamp of Peaceful Raidiance"],
  "ranged":[34.16,"Tirisfal Wand of Ascendancy"]
}
c3 = {
  "head":[193.72,"Hallowed Crown"],
  "neck":[93.5,"Necklace of Resplendent Hope"],
  "shoulder":[132.38,"Primal Mooncloth Shoulders"],
  "back":[89.5,"Vicar's Cloak"],
  "chest":[146.55,"Void Slayer's Tunic"],
  "wrist":[87.8,"Whirlwind Bracers"], #BIS T4
  "hands":[112.7,"Fathomheart Gauntlets"],
  "waist":[151.84,"Primal Mooncloth Belt"],
  "legs":[200.55,"Cyclone Kilt"],
  "feet":[103.11,"Light-Woven Slippers"],
  "finger":[80.0,""],
  "trinket":[0.0,""],
  "weapons":[368.5+100,"Hand of Eternity; Aran's Soothing Sapphire"],
  "ranged":[10.0,"Totem of Spontaneous Regrowth; Totem of the Plains"]
}
c1_n = [
  ("head",301.87,"H OHF","Wastewalker Helm"), #T4 BIS
  ("shoulder",239.02,"H AC","Wastewalker Shoulderpads"), #T4 BIS
  ("back",106.82,"H AC","Auchenai Death Shroud"),
  ("chest",182.08,"H BF","Wastewalker Tunic"),
  ("wrist",97.84,"H OHF","Nightfall Wristguards"), #T4 2nd BIS
  ("waist",161.68,"H BM","Girdle of the Deathdealer"), #T4 BIS
  ("trinket",59.0,"H BM","Hourglass of the Unraveller"),
  ("trinket",59.0,"BM","Hourglass of the Unraveller"),
  ("trinket",54.0,"Mech","Abacus of Violent Odds"),
  ("trinket",50.0,"H BF","Icon of Unyielding Courage"),
  ("weapons",283.0,"H ShH","The Bladefist"),
] #(item_place, value, item_location, item_id)
c2_n = [
  ("neck",45.45,"H UB","Hydra-fang Necklace"),
  ("back",44.5,"SH","Sethekk Oracle Cloak"),
  ("chest",92.2,"AC","Auchenai Anchorite's Robe"),
  ("wrist",44.5,"H Ramps","Crimson Bracers of Gloom"),
  ("hands",94.29,"H Ramps", "Mana-Etched Gloves"),
  ("waist",66.75,"H Arc","Belt of Depravity"),
  ("legs",74.3,"H BM","Khadgar's Kilt of Abjuration"),
  ("legs",74.3,"BM","Khadgar's Kilt of Abjuration"),
  ("finger",45.71,"H OHF","Sparking Arcanite Ring"),
  ("finger",42.7,"H MT","Cobalt Band of Tyrigosa"),
  ("trinket",53.8,"H SP","Quagmirran's Eye"),
  ("trinket",44.5,"H OHF","Arcanist's Stone"),
  ("weapons",153.15+44.45,"SLabs","Greatsword of Horrid Dreams"),
  ("weapons",153.15+44.45,"H SLabs","Greatsword of Horrid Dreams"),
  ("ranged",27.05,"H Arc","Nether Core's Control Rod"),
  ("ranged",27.05,"Arc","Nether Core's Control Rod")
] #(item_place, value, item_location, item_id)
c3_n = [
  ("head",193.72,"Arc","Hallowed Crown"),
  ("head",193.72,"H Arc","Hallowed Crown"),
  ("neck",93.5,"H OHF","Necklace of Resplendent Hope"),
  ("shoulder",113.1,"H MT","Mantle of the Sea Wolf"),
  ("back",99.8,"BOJ","Bishop's Cloak"),
  ("hands",112.7,"SV","Fathomheart Gauntlets"),
  ("waist",118.75,"H OHF","Cord of Sanctification"),
  ("legs",144.51,"SH","Hallowed Trousers"),
  ("feet",115.95,"H SP","Wavefury Boots"),
  ("feet",108.1,"H ShH","Jeweled Boots of Sanctification"),
  ("feet",108.1,"ShH","Jeweled Boots of Sanctification"),
  ("feet",103.11,"SH","Light-Woven Slippers"),
  ("trinket",50.0,"Bot","Bangle of Endless Blessings"),
  ("weapons",413.2,"H SLabs","Shockwave Truncheon"),
  ("ranged",10.0,"H SP","Totem of Spontaneous Regrowth")
] #(item_place, value, item_location, item_id)

class Member:
  def __repr__(self):
    return f"weights: {self.weights}\nupgrades: {self.upgrades}\ncurrent: {self.current}"

  '''
  weights will be the filename of a file containing tsv stat (name,weight) pairs for member M and is OTF (of-the-form):
    stat-name \t stat-weight
  upgrades will be the filename of file containing proposed item upgrades for M and is a series of entries OTF:
    item part \t location \t name \t number n
    followed by n pairs of tsv OTF:
       stat-name \t stat-weight
  current will be the filename of a file containing current items for M and is a series of entries OTF:
    item part \t name \t number n
    followed by n pairs of tsv's OTF:
       stat-name \t stat-quantity

  also these files may be given as a dict containing the same data
  '''
  def __init__(self, weights, upgrades, current, name):
    self.name = name
    # initialize weights
    w = type(weights)
    if w is str:
      # try to open the weights file and import weights
      try:
        with open(weights,"r") as w:
          self.weights = self.import_weights(w)
        if self.weights is None:
          self.upgrades = None
          self.current = None
          return
      except IOError:
        print(f"Input error: File '{weights}' does not exist.")
        self.weights = None
        self.upgrades = None
        self.current = None
        return
    elif w is dict:
      self.weights = weights # dict of (stat, weight) pairs

    #initialize upgrades
    u = type(upgrades)
    if u is str:
      # try to open the upgrades file and import upgrades
      try:
        with open(upgrades,"r") as u:
          self.upgrades = self.import_upgrades(u, self.weights)
        if self.upgrades is None:
          self.weights = None
          self.current = None
          return
      except IOError:
        print(f"Input error: File '{upgrades}' does not exist.")
        self.weights = None
        self.upgrades = None
        self.current = None
        return
    elif u is dict:
      self.upgrades = upgrades # list of (part, location, name, value) tuples

    c = type(current)
    if c is str:
      try:
        with open(current,"r") as c:
          self.current = self.import_current(c, self.weights)
        if self.current is None:
          self.weights = None
          self.upgrades = None
          return
      except IOError:
        print(f"Input error: File '{current}' does not exist.")
        self.current = None
        self.weights = None
        self.upgrades = None
        return
    elif c is dict:
      self.current = current # dict of (part, [name, value]) pairs

  # evaluate an item represented as a collection of stats as the sum of its weighted stats
  def evaluate(self, weights, stats):
    r = 0
    for stat,value in weights.items():
      if stat in stats:
        r += value*stats[stat]
    return r

  def priority(self):
    destinations = defaultdict(float)
    destination_items = defaultdict(list)
    for e in self.upgrades:
      part,location,name,value = e
      if part in self.current:
        d = value-self.current[part][1]
        if d>0:
          destinations[location] += d
          destination_items[location] += [(name, self.name, d)]
    return [(k,v,destination_items[k]) for k,v in sorted(destinations.items(),key=operator.itemgetter(1))]

  # the following import helper functions have their file structures defined above in Member (i.e. weight file a tsv OTF etc.)
  # import weights from file object w
  def import_weights(self, w):
    if w is None:
      print("Error: Missing weights file, can't import weights.")
      return None
    
    l = w.readline().rstrip().split('\t')
    weights = dict()
    if l == ['']:
      print("Input error: Empty weights file, ")
      return None
    while l != ['']:
      stat_name,stat_value = l
      weights[stat_name] = float(stat_value)
      l = w.readline().rstrip().split('\t')
    return weights

# import upgrades from file object u, using weights
  def import_upgrades(self, u, weights):
    if u is None:
      print("Error: Missing upgrades file, can't import upgrades.")
      return None
    if weights is None:
      print("Error: Missing weights, can't import upgrades.")
      return None
    
    l = u.readline().rstrip().split('\t')
    upgrades = []
    if l == ['']:
      print("Input error: Empty upgrades file, can't import upgrades.")
      return None
    while l != ['']:
      part,location,name,n = l
      stats = dict()
      for i in range(int(n)):
        l = u.readline().rstrip().split('\t')
        if l == ['']:
          print(f"Formatting error: expected {n} lines, had {i+1}, can't import upgrades.")
          return None
        stat_name,stat_value = l
        stats[stat_name] = float(stat_value)
      upgrades += [(part, location, name, self.evaluate(weights, stats))]
      l = u.readline().rstrip().split('\t')
    return upgrades

  # import current from file object c
  def import_current(self, c, weights):
    if c is None:
      print("Error: Missing current state file, can't import current state.")
      return None
    if weights is None:
      print("Error: Missing weights, can't import current state.")
      return None

    l = c.readline().rstrip().split('\t')
    current = dict()
    if l == ['']:
      print("Input error: Empty current state file, can't import current state.")
      return None
    while l != ['']:
      part,name,n = l
      stats = dict()
      for i in range(int(n)):
        l = c.readline().rstrip().split('\t')
        if l == ['']:
          print(f"Formatting error: expected {n} lines, had {i+1}, can't import current state.")
          return None
        stat_name,stat_value = l
        stats[stat_name] = float(stat_value)
      current[part] = [name, self.evaluate(weights, stats)]
      l = c.readline().rstrip().split('\t')
    return current

def close_files(files):
  for f in files:
    f.close()

'''
def hc_group_priority(group):
  destinations = defaultdict(float)
  destination_items = defaultdict(list)
  for member,upgrades in group:
    for e in upgrades:
      part,value,location,name = e
      if part in member:
        d = value-member[part][0]
        if(d>0):
          destinations[location] += d
          destination_items[location] += [name]
  return [(k,v,destination_items[k]) for k,v in sorted(destinations.items(),key=operator.itemgetter(1))]

#tests
# original test from hard-coded values, for priority calculator(s)
group = [(c1,c1_n),(c2,c2_n),(c3,c3_n)]
g = hc_group_priority(group)
g.reverse()
for m in g:
  location,value,items=m
  print(f"Value of {round(value)} gained from {location}")
  print(f"\tfrom: {items}")
'''

# group is a list of Members
def group_priority(group):
  destinations = defaultdict(float)
  destination_items = defaultdict(list)
  for member in group:
    for location,value,items in member.priority():
      destinations[location] += value
      destination_items[location] += items
  return [(k,v,destination_items[k]) for k,v in sorted(destinations.items(),key=operator.itemgetter(1))]

group = []
# test for import member from file
print("Creating members ...")
M = Member("weights.dat","upgrades.dat","current.dat","M")
N = Member("weights.dat","upgrades.dat","current.dat","N")
O = Member("weights.dat","upgrades.dat","current.dat","O")
if M is None:
  print("Error importing member data.")
else:
  group += [M,N,O]
  print(group_priority(group))

# TODO:
'''
add support for most important member sorting:
  member value weighting via group importance (value gained for one member > others)
most important item (presuming one item at a time)
most important location (presuming multiple items at a time)
'''
