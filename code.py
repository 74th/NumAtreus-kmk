import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
modtap = ModTap()
keyboard.modules.append(modtap)

from keymap import get_keymap

keyboard.col_pins = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
]

keyboard.row_pins = [
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP14,
]
n_rows = len(keyboard.row_pins)
n_cols = len(keyboard.col_pins)

keyboard.diode_orientation = DiodeOrientation.ROW2COL

left_mapping = [
    [(0,0), (1,0),  (2,0),  (3,0),  (4,0)],
    [(0,1), (1,1),  (2,1),  (3,1),  (4,1)],
    [(0,2), (1,2),  (2,2),  (3,2),  (4,2)],
    [(0,3), (1,3),  (2,3),  (3,3),  (4,3),  (5,3)],
]
right_mapping = [
    [        (6,0),  (7,0),  (8,0),  (9,0), (10,0)],
    [        (6,1),  (7,1),  (8,1),  (9,1), (10,1)],
    [        (6,2),  (7,2),  (8,2),  (9,2), (10,2)],
    [(5,2),  (6,3),  (7,3),  (8,3),  (9,3), (10,3)],
]

def apply_to_map(
    keys: list[list[int]], keymap: list[list[tuple[int, int]]], to: list[int]
):
    for row_no, rows in enumerate(keymap):
        for col_no, _ in enumerate(rows):
            pos = keymap[row_no][col_no]
            to[pos[0] + pos[1] * n_cols] = keys[row_no][col_no]

layers = get_keymap()
keyboard.keymap = []

for n, layer in enumerate(layers):
    keymap = [KC.NO] * len(keyboard.col_pins) * len(keyboard.row_pins)
    apply_to_map(layer[0], left_mapping, keymap)
    apply_to_map(layer[1], right_mapping, keymap)
    keyboard.keymap.append(keymap)

# keyboard.keymap = [[]]

if __name__ == "__main__":
    keyboard.go()
