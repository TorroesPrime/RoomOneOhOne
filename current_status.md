# Current Status

## September 3, 2023

> "A journey of a thousand miles begins with a single step"
*Laozi*

At this point, the project has only just started and is largely conceptual. My intention at this is point is documenting my plans for the project, and defining all the concepts for it. See below for the 'planning' section.

## Planning

### Phase 1

**Objective: Be able to walk around a map and perform basic interactions with the map.**

Tasks to be completed in this phase:

* [ ] create location class
* [ ] create room class
* [ ] create exit class
* [ ] create GameState class
* [ ] create interpreter class
* [ ] create command class
* [ ] create CommandFactory class
* [ ] create Move command
* [ ] create Look command
* [ ] create help command
* [ ] test move, look, and help commands

### Phase 2

### Objective: extend the interactivity from phase 1 to include interacting with items.

Tasks to be completed in this phase:

* [ ] create GameItem class
* [ ] impliment test character system
* [ ] create take command
* [ ] create drop command
* [ ] test take, and drop commands

### Phase 3

### Objective: impliment basic character system

Tasks to be completed in this phase:
* [ ] create basic character class.
* [ ] create basic CharacterIdentity class
* [ ] create basic CharacterDescription class
* [ ] create CoreStats class
* [ ] impliment NPC characters
* [ ] test basic NPC character functionality for identification
* [ ] test basic CoreStats functionality.

### Phase 4

### Objective: Complete a basic GUI based application that will permit the creation of adventure modules.

Tasks to be completed in this phase:
* [ ] Create 'Adventure Builder' system.
* [ ] impliment file reading, adventure instantiation, game state saving and game state restoration in the core system.

### Phase 5

### Objective: expand on the room, and exit classes to include lighting level, and enviroment types with rooms, and lock status and visible attributes on the exits.

Tasks to be completed in this phase:
* [ ] add lighting level and enviroment types to room class
* [ ] add visible and lock status to exit class
* [ ] create lock command
* [ ] create unlock command
* [ ] test new attribute functionality on room and exit objects.

### Phase 6

### Objective: expand on the item class to include verb:action system

Tasks to be completed in this phase:
* [ ] add verb:action to item class
* [ ] test verb:action functionality

### Phase 7

### Objective: expand on the character class to incorporate equipping and removing items of clothing, and in-game effects such as modification to health and other statuses.

Tasks to be completed in this phase:
* [ ] create CharacterCondition class
* [ ] expand on the character class to incorporate a CharacterCondition object.
* [ ] test the functionality of the expanded character class by ensuring current wounds, current fatigue, and status can be changed and their changed reflected in the game interface.

### Phase 8

**Objective: Impliment talent and enviromental modifiers.**

Tasks to be completed in this phase:
* [ ] create talent class
* [ ] impliment test instances of talents
* [ ] ensure functionality of character class when new talent(s) are added to an existing character.
* [ ] test effects of each talent in test instance library
* [ ] test enviromental modifer effects on core stat test functionality.
