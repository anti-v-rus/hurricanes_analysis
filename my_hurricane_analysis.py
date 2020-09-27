# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,1338,603,138,3057,74]

######################################
#TASKS
######################################

from collections import defaultdict

# Task 1: update damages function 
def update_damages(damages_list):
  updated_damages = []
  convertion = {"M" : 1000000,"B" : 1000000000} 
  for damage in damages_list:
    if damage[-1] in convertion:
      mult = convertion[damage[-1]]
      damage = damage[:-1]
      calculate_damage = float(damage) * mult
      updated_damages.append(calculate_damage)
    else:
      updated_damages.append(damage)
  return updated_damages
updated_damages = update_damages(damages)

# Task 2: construct hurricane dictionary function:
def hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  hurricanes = {}
  
  for i in range(len(names)):
    hurricanes[names[i]] = {"Name": names[i], "Month": months[i],"Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": updated_damages[i], "Deaths": deaths[i]}
  return hurricanes

hurricanes_dictionary = hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

# Task 3: construct hurricane by year dictionary function:
def yearly_hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  yearly_hurricanes = {}
  
  for i in range(len(years)):
    yearly_hurricanes[years[i]] = {"Name": names[i], "Month": months[i],"Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": updated_damages[i], "Deaths": deaths[i]}
  return yearly_hurricanes

yearly_hurricanes_dictionary = yearly_hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

# Task 4: count affected areas function:
def count_a_areas(hurricanes_dictionary):
  counted_a_areas_dict = {}
  d = defaultdict(int)
  for hurricane in hurricanes_dictionary:
    for a_area in hurricanes_dictionary.get(hurricane, {}).get('Areas Affected'):
      d[a_area] += 1
  return dict(d.items())

counted_a_areas_dict = count_a_areas(hurricanes_dictionary)

# Task 5: find most affected area function:
def most_a_areas(dictionary):
  max_key = max(dictionary, key=dictionary.get)
  max_value = max(dictionary.values())
  return max_key, max_value

# Task 6: greatest number of deaths function:
def most_deaths(dictionary):
  d = defaultdict(int)
  for hurricane in dictionary:
    num_deaths = dictionary.get(hurricane, {}).get('Deaths')
    d[hurricane] += num_deaths

  max_key = max(d, key=d.get)
  max_value = max(d.values())
  return max_key, max_value

# Task 7: catgeorize by mortality function:
def mortality_rating(dictionary):
  mortality_scale = defaultdict(list)
  d = defaultdict(int)
  #getting the dict of hurricanes with most mortality
  for hurricane in dictionary:
    num_deaths = dictionary.get(hurricane, {}).get('Deaths')
    d[hurricane] += num_deaths
    mort_dict = dict(d.items())
  #create a rating dict for the most deadly hurricanes
  for key, value in mort_dict.items():
    if value == 0:
      mortality_scale[0].append(key)
    if 0 < value <= 100:
      mortality_scale[1].append(key)
    if 100 < value <= 500:
      mortality_scale[2].append(key)
    if 500 < value <= 1000:
      mortality_scale[3].append(key)
    if 1000 < value <= 10000:
      mortality_scale[4].append(key)
    else:
      mortality_scale[5].append(key)
  return dict(sorted(mortality_scale.items()))

# Task 8: greatest damage function:

#get the most_damage_dictionary
def most_damage(dictionary):
  most_damage_dict = {}
  for hurricane in dictionary:
    damage_cost = dictionary.get(hurricane, {}).get('Damage')
    most_damage_dict[hurricane] = damage_cost

  #get the max_key and max_value from float avoiding str (solution from StackOverflow)
  max_key = max(most_damage_dict.keys(), key=lambda x: most_damage_dict[x] if not isinstance(most_damage_dict[x], str) else float("-inf"))
  max_value = max(most_damage_dict.values(), key=lambda x: x if not isinstance(x, str) else float("-inf"))
  return max_key, max_value

# Task 9: catgeorize by damage function:
def damage_rating(dictionary):
  most_damage_dict = {}
  damage_scale = defaultdict(list)
  #get the dict with most damage
  for hurricane in dictionary:
    damage_cost = dictionary.get(hurricane, {}).get('Damage')
    most_damage_dict[hurricane] = damage_cost
  
  #create a rating dict for the hurricanes with the most damage
  for key, value in most_damage_dict.items():
    if not isinstance(value, str):
      if value == 0:
        damage_scale[0].append(key)
      if 0 < value <= 100000000:
        damage_scale[1].append(key)
      if 100000000 < value <= 1000000000:
        damage_scale[2].append(key)
      if 1000000000 < value <= 10000000000:
          damage_scale[3].append(key)
      if 10000000000 < value <= 100000000000:
        damage_scale[4].append(key)
      if 1000000000000 < value:
        damage_scale[5].append(key)
    else: 
      damage_scale['Damage not recorded'].append(key)

  return dict(damage_scale.items())
