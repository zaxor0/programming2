#!/usr/bin/python3

from abc import ABC, abstractmethod
from dataclasses import dataclass

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
        self.execute()

    def execute(self) -> None:
        # only turn on and add to history if the light was off, no need to fill the history "on commands"
        if not self._light.on:
            self._prev_state = self._light.on 
            self._light.on = True
            self._history.push(self)

    def unexecute(self) -> None:
        self._light.on = self._prev_state

class SetFanSpeedCommand(RevertableCmd):
    def __init__(self, fan: Fan, speed: int) -> None:
        self._fan = fan
        self._history = History()
        self._prev_state = None
        self.execute(speed)

    def execute(self, speed) -> None:
        # only change speed if its different
        if self._fan.speed != speed:
            self._prev_state = self._fan.speed
            self._fan.speed = speed
            self._history.push(self)

    def unexecute(self) -> None:
        self._fan.speed = self._prev_state

class PlaySongCommand(RevertableCmd):
    def __init__(self, music_player: MusicPlayer(), song: str) -> None:
        self._music_player = music_player
        self._history = History()
        self._prev_state = None
        self.execute(song)

    def execute(self, song) -> None:
        # since its reasonable someone would want to re-listen to a song, no comparison for this one
        self._prev_state = self._music_player.song
        self._music_player.song = song
        self._history.push(self)

    def unexecute(self) -> None:
        self._music_player.song = self._prev_state

class History:
    def __init__(self) -> None:
        self._commands: list[RevertableCmd] = []

    def push(self, cmd: RevertableCmd) -> None:
        self._commands.append(cmd)

    def pop(self) -> RevertableCmd:
        return self._commands.pop()

    def __len__(self) -> int:
        return len(self._commands)


class RemoteControl():
    def __init__(self):
        self._name = "my remote"
        self._history = History()

    def submit(self, cmd):
        self._history.push(cmd)

    def undo(self):
        if len(self._history) > 0:
            last_cmd = self._history.pop()
            last_cmd.unexecute()


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
    remote.submit(LightOnCommand(light))
    remote.submit(SetFanSpeedCommand(fan, 3))
    remote.submit(PlaySongCommand(player, "Take Five"))

    print("\n## NEW VALUES")
    print(light)
    print(fan)
    print(player)

    print("\n## CALL UNDO")
    remote.undo()
    remote.undo()

    print("\n## NEW VALUES")
    print(light)
    print(fan)
    print(player)

    remote.undo()
    remote.undo()
    remote.undo()
    remote.undo()

if __name__ == "__main__":
    main()
