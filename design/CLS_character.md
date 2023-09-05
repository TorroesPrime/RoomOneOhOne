# character

## fields

### char_id

a UUID compliant string. The individual ID is unique to the character and generated at the time the character is created. This allows the same
character to be imported and used in different adventures.

### imperial_messurements

A boolean indicating if the measurements used for this character were determined in imperial measurements or not.

### identity

a CharacterIdentity object.

### description

a CharacterDescription object

### core_stats

a CoreStats object

### condition

a CharacterCondition object

### skills

a CharacterSkills objects

### talents

a list of CharacterTalent objects

### expierience

a CharacterExpierence object.

### inventory

an Inventory object

### apparel

a CharacterApparel object.

### armor

a CharacterArmor object.

### known_characters

a dictionary that lists the char_id of every character this has interacted with as the key, with the value being an int with a value ranging between -255 and 255. A value of 255 means that the character is regarded as close family, an honored ally, and cherished comrade, while a value of -255 means that the character is utterly despised and revialed.

## methods

### get_first_name

### get_last_name

### get_full_name

### get_common_name

### get_age

### get_nick_name(asking_c)

### get_status

### change_status

### wound

### heal

### add_item(item)

### remove_item(item)

### equip_item(item,location)

### unequip_item(item)

### add_trait(trait)

### improve_trait(trait_name,amount)

### add_skill(skill)

### improve_skill(skill_name,amount)

### check_skill(skill or condition)

### check_talent(talent or condition)

### earn_xp(amount)

### reduce_xp(amount)

### add_fatigue(amount)

### reduce_fatigue(amount)

### stat_test(stat)

### get_char_sheet(options)
