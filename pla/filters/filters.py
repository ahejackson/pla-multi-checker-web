# Filters
def is_shiny(pokemon):
    return pokemon['shiny'] == True

def is_square_shiny(pokemon):
    return pokemon['square'] == True

def is_alpha(pokemon):
    return pokemon['alpha'] == True

def is_perfect(pokemon):
    return pokemon['ivs'] == [31, 31, 31, 31, 31, 31]

def is_perfect_physical(pokemon):
    ivs = pokemon['ivs']
    return ivs[0] == 31 and ivs[1] == 31 and ivs[2] == 31 and ivs[4] == 31 and ivs[5] == 31 

def is_perfect_special(pokemon):
    ivs = pokemon['ivs']
    return ivs[0] == 31 and ivs[2] == 31 and ivs[3] == 31 and ivs[4] == 31 and ivs[5] == 31

def no_attack(pokemon):
    return pokemon['ivs'][1] == 0

def no_speed(pokemon):
    return pokemon['ivs'][5] == 0

def num_perfect_ivs(pokemon):
    return sum(1 for iv in pokemon['ivs'] if iv == 31)

def num_30plus_ivs(pokemon):
    return sum(1 for iv in pokemon['ivs'] if iv >= 30)
    
def has_3ivs(pokemon):
    return num_perfect_ivs(pokemon) >= 3
    
def has_4ivs(pokemon):
    return num_perfect_ivs(pokemon) >= 4
    
def has_5ivs(pokemon):
    return num_perfect_ivs(pokemon) >= 5

def is_shiny_6iv(pokemon):
    return is_shiny(pokemon) and is_perfect(pokemon)

def is_shiny_alpha(pokemon):
    return is_shiny(pokemon) and is_alpha(pokemon)

def has_no_attack_5iv(pokemon):
    return no_attack(pokemon) and has_5ivs(pokemon)

def has_6iv_over_30(pokemon):
    return num_30plus_ivs(pokemon) == 6