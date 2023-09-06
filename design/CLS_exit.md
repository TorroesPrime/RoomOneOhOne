# exit

An exit is used to transport the player from one [room](https://github.com/TorroesPrime/RoomOneOhOne/blob/main/design/CLS_room.md) to another. An exit from one room has a corresponding exit in the next room in the opposite direction, allowing the player to traverse between rooms as intended.

## fields

### id_num

A UUID compliant string that is created the first-time a given exit is instantiated for a particular play through of a particular adventure module. This string will be unique to each play through of the adventure the exit is used in.

### name

A descriptive name for the exit. Used to make it easier to refer to a given exit. If no name is supplied, a default name for the exit is created using the source room’s name and the direction of the exit.

### dir

a string denoting what direction this exit corresponds with.

### source

a room object representing what the room the player must be in to use this exit.

### destination

a room object representing what room the player will be moved to when they pass through this exit.

### is_locked

a Boolean that determines if an exit is locked or not. A locked exit cannot be traversed.

### is_hidden

a Boolean that determines if the exit is readily visible or not.

### action_library

a dictionary containing strings that are called for various descriptions. The keys for this dictionary are:
•	locking
•	already locked
•	unlocking
•	already locked
•	opening
•	closing
•	door description

## methods

### describe–

returns a description containing an exit and its associated destination.

###switchLock–

changes the isLocked attribute to its other state, false if already true and true is already false. 
