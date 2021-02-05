from __future__ import annotations

import typing

from blessed import Terminal

class TBox(typing.NamedTuple):
    t: Terminal
    x: int
    y: int
    w: int
    h: int

class Tile(object):
    def __init__(self, title: str = ..., border_color: int = ..., color: int = ...): ...
    def _display(self, tbox: TBox, parent: Tile) -> None: ...
    def _draw_borders(self, tbox: TBox) -> None: ...
    def _draw_borders_and_title(self, tbox: TBox) -> Tbox: ...
    def _fill_area(self, tbox: TBox, char: str, *a, **kw) -> None: ...
    def display(self) -> None: ...
    def _draw_title(self, tbox: TBox, fill_all_width: bool) -> None: ...

class Split(Tile):
    def __init__(self, *items, **kw): ...
    def _display(self, tbox: TBox, parent: Tile) -> None: ...

class VSplit(Split): ...

class HSplit(Split): ...

class Text(Tile):
    def __init__(self, text: str, color: int = 0, *args, **kw): ...
    def _display(self, tbox: TBox, parent: Tile) -> None: ...

class Log(Tile):
    def __init__(self, *args, **kw): ...
    def _display(self, tbox: TBox, parent: Tile): ...
    def append(self, msg: str) -> None: ...

class HGauge(Tile):
    def __init__(self, label: typing.Optional[str] = ..., val: typing.Union[int, float] = ...,
                 color: int = ..., **kw): ...
    def _display(self, tbox: TBox, parent: Tile) -> None: ...

class VGauge(Tile):
    def __init__(self, val: typing.Union[int, float] = ..., color: int = ..., **kw): ...
    def _display(self, tbox: TBox, parent: Tile) -> None: ...

class ColorRangeVGauge(Tile):
    def __init__(self, val: typing.Union[int, float] = ...,
                 colormap: typing.Sequence[typing.Tuple[int, int]] = ..., **kw): ...
    def _display(self, tbox: TBox, parent: Tile) -> None: ...

class VChart(Tile):
    def __init__(self, val: typing.Union[int, float] = ..., **kw): ...
    def append(self, dp: typing.Union[int, float]) -> None: ...
    def _display(self, tbox: TBox, parent: Tile) -> None: ...

class HChart(Tile):
    def __init__(self, val: typing.Union[int, float] = ..., *args, **kw): ...
    def append(self, dp: typing.Union[int, float]) -> None: ...
    def _display(self, tbox: TBox, parent: Tile) -> None: ...

class HBrailleChart(Tile):
    def __init__(self, val: typing.Union[int, float] = ..., *args, **kw): ...
    def append(self, dp: typing.Union[int, float]) -> None: ...
    def _generate_braille(self, lmax: int, rmax: int) -> str: ...
    def _display(self, tbox: TBox, parent: Tile) -> None: ...

class HBrailleFilledChart(Tile):
    def __init__(self, val: typing.Union[int, float] = ..., *args, **kw): ...
    def append(self, dp: typing.Union[int, float]) -> None: ...
    def _generate_braille(self, lmax: int, rmax: int) -> str: ...
    def _display(self, tbox: TBox, parent: Tile) -> None: ...

