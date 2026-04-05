#!/usr/bin/python3
from abc import ABC, abstractmethod
from dataclasses import dataclass

# these data classes are RECEIVERS that get new content/states via the CONCRETE COMMANDS
@dataclass
class Light:
    _on: bool = False

    @property
    def on(self):
        return self._on

    @on.setter
    def on(self, new_value: bool) -> None:
        self._on = new_value

@dataclass
class Fan:
    _speed: int = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_value: int) -> None:
        self._speed = new_value

@dataclass
class MusicPlayer:
    _song: str = None

    @property
    def song(self):
        return self._song

    @song.setter
    def song(self, new_value: str) -> None:
        self._song = new_value

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

## The INVOKER calls these CONCRETE COMMANDS to update the RECIEVERS
class LightOnCommand(RevertableCmd):
    def __init__(self, light: Light) -> None:
        self._light = light
        self._prev_state = None

    def execute(self) -> None:
        # turn on only if the light was off
        if not self._light.on:
            self._prev_state = self._light.on 
            self._light.on = True
            return True
        return False

    def unexecute(self) -> None:
        self._light.on = self._prev_state

    def __str__(self):
        return f"Setting light on"

class LightOffCommand(RevertableCmd):
    def __init__(self, light: Light) -> None:
        self._light = light
        self._prev_state = None

    def execute(self) -> None:
        # turn off only if the light was on
        if self._light.on:
            self._prev_state = self._light.on 
            self._light.on = False
            return True
        return False

    def unexecute(self) -> None:
        self._light.on = self._prev_state

    def __str__(self):
        return f"Setting light off"

class SetFanSpeedCommand(RevertableCmd):
    def __init__(self, fan: Fan, speed: int) -> None:
        self._fan = fan
        self._prev_state = None
        self._payload = speed

    def execute(self) -> None:
        # only change speed if its different
        if self._fan.speed != self._payload:
            self._prev_state = self._fan.speed
            self._fan.speed = self._payload
            return True
        return False

    def unexecute(self) -> None:
        self._fan.speed = self._prev_state

    def __str__(self):
        return f"Setting fan speed {self._payload}"

class PlaySongCommand(RevertableCmd):
    def __init__(self, music_player: MusicPlayer, song: str) -> None:
        self._music_player = music_player
        self._prev_state = None
        self._payload = song

    def execute(self) -> None:
        # since its reasonable someone would want to re-listen to a song, no comparison for this one
        self._prev_state = self._music_player.song
        self._music_player.song = self._payload
        return True

    def unexecute(self) -> None:
        self._music_player.song = self._prev_state

    def __str__(self):
        return f"Playing song {self._payload}"

class StopSongCommand(RevertableCmd):
    def __init__(self, music_player: MusicPlayer) -> None:
        self._music_player = music_player
        self._prev_state = None

    def execute(self) -> None:
        # stop the song only if there was a song playing
        if self._music_player.song:
            cmd_success = True
            self._prev_state = self._music_player.song
            self._music_player.song = None
            return True
        return False 

    def unexecute(self) -> None:
        self._music_player.song = self._prev_state

    def __str__(self):
        return f"Stopping song {self._prev_state}"

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

# The INVOKER which calls the CONCRETE COMMANDS to makes changes to the RECEIVERS (dataclasses)
class RemoteControl():
    def __init__(self):
        self._name = "my remote"
        self._history = History()

    def submit(self, cmd):
        if cmd.execute():
            print(f"+Executed Command:\t{cmd}")
            self._history.push(cmd)
        else:
            print(f"-Did not execute:\t{cmd}")

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
    print("...turn light on, set fan to 3 twice, play \"blue train\"")
    remote.submit(LightOnCommand(light))
    remote.submit(SetFanSpeedCommand(fan, 3))
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
