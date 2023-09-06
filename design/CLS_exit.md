# exit

An exit is used to transport the player from one [room](https://github.com/TorroesPrime/RoomOneOhOne/blob/main/design/CLS_room.md) to another. An exit from one room has a corresponding exit in the next room in the opposite direction, allowing the player to traverse between rooms as intended.

## fields
<dl>
<dt>id_num</dt>
<dd>A UUID compliant string that is created the first-time a given exit is instantiated for a particular play through of a particular adventure module. This string will be unique to each play through of the adventure the exit is used in.</dd>

<dt>name</dt>
<dd>A descriptive name for the exit. Used to make it easier to refer to a given exit. If no name is supplied, a default name for the exit is created using the source room’s name and the direction of the exit.</dd>

<dt>dir</dt>
<dd>a string denoting what direction this exit corresponds with.</dd>

<dt>source</dt>
<dd>a room object representing what the room the player must be in to use this exit.</dd>

<dt>destination</dt>
<dd>a room object representing what room the player will be moved to when they pass through this exit.</dd>

<dt>is_locked</dt>
<dd>a Boolean that determines if an exit is locked or not. A locked exit cannot be traversed.</dd>

<dt>is_hidden</dt>
<dd>a Boolean that determines if the exit is readily visible or not.</dd>

<dt>action_library</dt>
<dd>a dictionary containing strings that are called for various descriptions. The keys for this dictionary are:</dd>
<ul>
    <li>locking</li>
    <li>already locked</li>
    <li>unlocking</li>
    <li>already locked</li>
    <li>opening</li>
    <li>closing</li>
    <li>door description</li>
    </ul>
</dl>
## methods
<dl>
<dt>describe</dt>
<dd>returns a description containing an exit and its associated destination.</dd>

<dt>switchLock</dt>
<dd>changes the isLocked attribute to its other state, false if already true and true is already false. </dd>
</dl>
