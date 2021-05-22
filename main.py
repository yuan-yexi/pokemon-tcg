import database


class Pokemon:
    def __init__(self, uuid, name, super_type, sub_types, level, hp, types,
                 evolves_to, attacks, weaknesses, retreat_cost, conv_retreat_cost, card_set,
                 number, artist, rarity, flavor_text, pokedex_num, legalities,
                 images, tcg_player) -> None:
        self.uuid = uuid
        self.name = name
        self.super_type = super_type
        self.sub_types = sub_types
        self.level = level
        self.hp = hp
        self.types = types
        self.evolves_to = evolves_to
        self.attacks = attacks
        self.weaknesses = weaknesses
        self.retreat_cost = retreat_cost
        self.conv_retreat_cost = conv_retreat_cost
        self.card_set = card_set
        self.number = number
        self.artist = artist
        self.rarity = rarity
        self.flavor_text = flavor_text
        self.pokedex_num = pokedex_num
        self.legalities = legalities
        self.images = images
        self.tcg_player = tcg_player

    def get_attributes(self):
        print("Id:", self.uuid)
        print("Name:", self.name)
        print("Super Type:", self.super_type)
        print("Sub Types:", self.sub_types)
        print("Level:", self.level)
        print("HP:", self.hp)
        print("Types:", self.types)
        print("Evolves To:", self.evolves_to)
        print("Attacks:", self.attacks)
        print("Weaknesses:", self.weaknesses)
        print("Retreat Cost:", self.retreat_cost)
        print("Converted Retreat Cost:", self.conv_retreat_cost)
        print("card_set:", self.card_set)
        print("Number:", self.number)
        print("Artist:", self.artist)
        print("Rarity:", self.rarity)
        print("Flavor Text:", self.flavor_text)
        print("National Pokedex Number:", self.pokedex_num)
        print("Legalities:", self.legalities)
        print("Images:", self.images)
        print("TCG Player:", self.images)
    
    def get_attacks(self):
        name = self.name
        attacks = self.attacks
        print("+++++++++")
        print(name)
        for index, attack in enumerate(attacks):
            print("---------")
            print(f"{index + 1}: {attack['name']}")
            print(f"Cost: {attack['convertedEnergyCost']} {attack['cost']}")
            print(f"Damage: {attack['damage']}")
            if attack['text'] != '':
                print(f"{attack['text']}")
        print("+++++++++")


pikachu_data = database.pikachu['data']
machop_data = database.machop['data']

Pikachu = Pokemon(pikachu_data['id'], pikachu_data['name'], pikachu_data['supertype'],
                  pikachu_data['subtypes'], pikachu_data['level'], pikachu_data['hp'],
                  pikachu_data['types'], pikachu_data['evolvesTo'], pikachu_data['attacks'],
                  pikachu_data['weaknesses'], pikachu_data['retreatCost'], pikachu_data['convertedRetreatCost'],
                  pikachu_data['set'], pikachu_data['number'], pikachu_data['artist'], pikachu_data['rarity'],
                  pikachu_data['flavorText'], pikachu_data['nationalPokedexNumbers'], pikachu_data['legalities'],
                  pikachu_data['images'], pikachu_data['tcgplayer'])

Machop = Pokemon(machop_data['id'], machop_data['name'], machop_data['supertype'],
                  machop_data['subtypes'], machop_data['level'], machop_data['hp'],
                  machop_data['types'], machop_data['evolvesTo'], machop_data['attacks'],
                  machop_data['weaknesses'], machop_data['retreatCost'], machop_data['convertedRetreatCost'],
                  machop_data['set'], machop_data['number'], machop_data['artist'], machop_data['rarity'],
                  machop_data['flavorText'], machop_data['nationalPokedexNumbers'], machop_data['legalities'],
                  machop_data['images'], machop_data['tcgplayer'])

Pikachu.get_attacks()
Machop.get_attacks()
