# character

## fields
<dl>
<dt>char_id</dt>
<dd>a UUID compliant string. The individual ID is unique to the character and generated at the time the character is created. This allows the same character to be imported and used in different adventures.</dd>

<dt>imperial_messurements</dt>
<dd>A boolean indicating if the measurements used for this character were determined in imperial measurements or not.</dd>

<dt>identity</dt>
<dd>a CharacterIdentity object.</dd>

<dt>description</dt>
<dd>a CharacterDescription object</dd>

<dt>core_stats</dt>
<dd>a CoreStats object</dd>

<dt>condition</dt>
<dd>a CharacterCondition object</dd>

<dt>skills</dt>
<dd>a CharacterSkills objects</dd>

<dt>talents</dt>
<dd>a list of CharacterTalent objects</dd>

<dt>expierience</dt>
<dd>a CharacterExpierence object.</dd>

<dt>inventory</dt>
<dd>an Inventory object</dd>

<dt>apparel</dt>
<dd>a CharacterApparel object.</dd>

<dt>armor</dt>
<dd>a CharacterArmor object.</dd>

<dt>known_characters</dt>
<dd>a dictionary that lists the char_id of every character this has interacted with as the key, with the value being an int with a value ranging between -255 and 255. A value of 255 means that the character is regarded as close family, an honored ally, and cherished comrade, while a value of -255 means that the character is utterly despised and revialed.</dd>
</dl>
## methods
<dl>
<dt>get_first_name</dt>
<dd>returns the first name of the character as provided by the character's CharacterIdentity object.</dd>

<dt>get_last_name</dt>
<dd>returns the first name of the character as provided by the character's CharacterIdentity object.</dd>
<dt>get_full_name</dt>
<dd>returns the full name, comprised of [first name][middile name(s)][last name], of the character as provided by the character's CharacterIdentity object.</dd>
<dt>get_common_name</dt>
<dd>returns the common name of the character as provided by the character's CharacterIdentity object.</dd>
<dt>get_age</dt>
<dd>returns the age of the character as provided by the character's CharacterIdentity object.</dd>
<dt>get_nick_name(asking_c)</dt>
<dd>checks the <i>asking_c</i>'s reputation as recording in the character's known_character attribute. If the value is higher then 75,returns the nickname name of the character as provided by the character's CharacterIdentity object. Otherwise returns the result of the get_first_name method().</dd>
<dt>get_status()</dt>
<dd>returns the result of the character's condition's cur_status.</dd>
<dt>remove_status(status_effect)</dt>
<dd>removes the first instance of <i>status_effect</i> from character's conditon.</dd>
<dt>wound(amount)</dt>
<dd>adds <i>amount</i> of wounds to character's condition.</dd>
<dt>heal(amount)</dt>
<dd>removed <i>amount</i> of wounds from character's condition.</dd>
<dt>add_item(item)</dt>
<dd>adds <i>item</i> to character's inventory.</dd>
<dt>remove_item(item)</dt>
<dd>removes the first instance of <i>item</i> from character's inventory.</dd>

<dt>equip_item(item,location)</dt>
<dd>equips <i>item</i> to <i>location</i>, removing it from the character's inventory.</dd>
<dt>unequip_item(item)</dt>
<dd>unequips <i>item</i> from its current location and returns it to character's inventory.</dd>
<dt>add_trait(trait)</dt>
<dd>adds <i>trait</i> to character's traits.</dd>
<dt>improve_trait(trait_name,amount)</dt>
<dd>attempts to improve <i>trait_name</t> by <i>amount</i>. if a trait named <i>train_name</i> is not present, the trait is added with a amount of 1.</dd>
<dt>add_skill(skill)</dt>
<dd>adds <i>skill</i> to character's skills_C.</dd>
<dt>improve_skill(skill_name,amount)</dt>
<dd>attempts to improve a skill named <i>skill_name</i> by <i>amount</i>. if a skill named <i>skill_name</i> is not present, the skill is added with a amount of 1.</dd>
<dt>check_skill(skill or condition)</dt>
<dd>checks to see if <i>skill</i> or <i>condition</i> is present in character's skills_C or condition.</dd>
<dt>check_talent(talent or condition)</dt>
<dd>checks to see if <i>talent</i> or <i>condition</i> is present in character's talents or condition.</dd>
<dt>earn_xp(amount)</dt>
<dd>adds <i>amount</i> to character's expierence.</dd>
<dt>reduce_xp(amount)</dt>
<dd>removes <i>amount</i> from character's expierence.</dd>
<dt>add_fatigue(amount)</dt>
<dd>adds <i>amount</i> of fatigue to character's condition.</dd>
<dt>reduce_fatigue(amount)</dt>
<dd>removes <i>amount</i> of fatigue from character's condition.</dd>
<dt>stat_test(stat,mod)</dt>
<dd>performs a <a href=https://github.com/TorroesPrime/RoomOneOhOne/blob/main/general_concepts.md#skill-test>stat test</a> with the character's <i>stat</i> stat, modified by <i>mod</i> value.</dd>
<dt>get_char_sheet(options)</dt>
<dd>returns the character's compiled character sheet.</dd>
<dl>