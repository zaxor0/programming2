#!/usr/bin/python3

from abc import ABC, abstractmethod
from dataclasses import dataclass

## WRITTEN ANSWER
"""
1. This is a command pattern, which gives us an interface for commands, which can be revertable.
2. Class explanations:
    - We have a few data classes that represent objects in our house that have "states" such as being on or performing an action
    - The we have several command classes, which depend on the dataclasses to exist, that change the settings for data class
        - This _might_ seem bad, but its actually good, because it lets our commands have a single responsibility
        - That would let us build out macro commands easier, such as setting a scene with one "button"
    - Next we have the history, this is used in the remote and command classes. It is a basic stack that we need for "undo" type actions
    - Last we have the remote, this is our reciever, that we pass commands to it and it simply invokes them.
3. This design, besides removed conditionals, accomplishses the following:
    - The command functions are single responsibility
    - The whole script is open, as we can easly add more commands and data types without changine the core classes
    - We can now create composition / macro commands if we want
"""


@dataclass
class Light:
    on: bool = False

@dataclass
class Fan:
    speed: int = 0

@dataclass
class MusicPlayer:
    song: str = None

## INTERFACE 
class Cmd(ABC):
    @abstractmethod
    def execute(self) -> None:
        """execute the command"""
        pass

class RevertableCmd(Cmd):
    @abstractmethod
    def unexecute(self) -> None:
        """Undo the effect of execute()."""
        pass

## CONCRETE COMMANDS 
class LightOnCommand(RevertableCmd):
    def __init__(self, light: Light) -> None:
        self._light = light
        self._history = History()
        self._prev_state = None

    def execute(self) -> None:
        # turn on and add to history only if the light was off, no need to fill the history "on commands"
        if not self._light.on:
            self._prev_state = self._light.on 
            self._light.on = True
            self._history.push(self)

    def unexecute(self) -> None:
        self._light.on = self._prev_state

class LightOffCommand(RevertableCmd):
    def __init__(self, light: Light) -> None:
        self._light = light
        self._history = History()
        self._prev_state = None

    def execute(self) -> None:
        # turn off and add to history only if the light was on, no need to fill the history "off commands"
        if self._light.on:
            self._prev_state = self._light.on 
            self._light.on = False
            self._history.push(self)

    def unexecute(self) -> None:
        self._light.on = self._prev_state

class SetFanSpeedCommand(RevertableCmd):
    def __init__(self, fan: Fan, speed: int) -> None:
        self._fan = fan
        self._history = History()
        self._prev_state = None
        self._payload = speed

    def execute(self) -> None:
        # only change speed if its different
        if self._fan.speed != self._payload:
            self._prev_state = self._fan.speed
            self._fan.speed = self._payload
            self._history.push(self)

    def unexecute(self) -> None:
        self._fan.speed = self._prev_state

class PlaySongCommand(RevertableCmd):
    def __init__(self, music_player: MusicPlayer, song: str) -> None:
        self._music_player = music_player
        self._history = History()
        self._prev_state = None
        self._payload = song

    def execute(self) -> None:
        # since its reasonable someone would want to re-listen to a song, no comparison for this one
        self._prev_state = self._music_player.song
        self._music_player.song = self._payload
        self._history.push(self)

    def unexecute(self) -> None:
        self._music_player.song = self._prev_state

class StopSongCommand(RevertableCmd):
    def __init__(self, music_player: MusicPlayer) -> None:
        self._music_player = music_player
        self._history = History()
        self._prev_state = None

    def execute(self) -> None:
        # stop the song and add it to history only if there was a song playing
        if self._music_player.song:
            self._prev_state = self._music_player.song
            self._music_player.song = None
            self._history.push(self)

    def unexecute(self) -> None:
        self._music_player.song = self._prev_state

# STACK FOR UNDO OPERATIONS
class History:
    def __init__(self) -> None:
        self._commands: list[RevertableCmd] = []

    def push(self, cmd: RevertableCmd) -> None:
        self._commands.append(cmd)

    def pop(self) -> RevertableCmd:
        return self._commands.pop()

    def __len__(self) -> int:
        return len(self._commands)

# RECEIVER
class RemoteControl():
    def __init__(self):
        self._name = "my remote"
        self._history = History()

    def submit(self, cmd):
        self._history.push(cmd)
        cmd.execute()

    def undo(self):
        if len(self._history) > 0:
            last_cmd = self._history.pop()
            last_cmd.unexecute()

# CLIENT CODE
def main():
    # create data classes
    light = Light()
    fan = Fan()
    player = MusicPlayer()

    remote = RemoteControl()
    
    print("## INITIAL VALUES")
    print(light)
    print(fan)
    print(player)

    print("\n## RUNNING COMMANDS")
    print("...turn light on, set fan to 3, play \"blue train\"")
    remote.submit(LightOnCommand(light))
    remote.submit(SetFanSpeedCommand(fan, 3))
    remote.submit(PlaySongCommand(player, "Blue Train"))

    print("\n## NEW VALUES")
    print(light)
    print(fan)
    print(player)

    print("\n## RUNNING COMMANDS") 
    print("...turn light off, stop the music")
    remote.submit(LightOffCommand(light))
    remote.submit(StopSongCommand(player))
    print("\n## NEW VALUES")
    print(light)
    print(fan)
    print(player)

    print("\n## CALL UNDO TWICE")
    remote.undo()
    remote.undo()

    print("\n## NEW VALUES")
    print(light)
    print(fan)
    print(player)

    print("\n## CALL UNDO SIX TIMES")
    remote.undo()
    remote.undo()
    remote.undo()
    remote.undo()
    remote.undo()
    remote.undo()

    print("\n## FINAL VALUES")
    print(light)
    print(fan)
    print(player)


if __name__ == "__main__":
    main()
