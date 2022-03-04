"""
Aterus
https://atreus.technomancy.us/
"""
from kmk.keys import KC


letter_layer = 0
punction_digits_layer = 1
arrows_function_layer = 2

____ = KC.TRANSPARENT

def query_keymap():
    fn = KC.MO(punction_digits_layer)
    left = [
        [KC.Q,      KC.W,       KC.E,       KC.R,       KC.T],
        [KC.A,      KC.S,       KC.D,       KC.F,       KC.G],
        [KC.Z,      KC.X,       KC.C,       KC.V,       KC.B],
        [KC.ESC,    KC.TAB,     KC.LGUI,    KC.LSFT,    KC.BSPC,    KC.LCTL],
    ]
    right = [
        [           KC.Y,       KC.U,       KC.I,       KC.O,       KC.P],
        [           KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN],
        [           KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH],
        [KC.LALT,   KC.SPC,     fn,         KC.MINS,    KC.QUOT,    KC.ENT],
    ]
    return [left, right]

def punction_digits_keymap():
    l2 = KC.MO(arrows_function_layer)
    left = [
        [KC.EXLM,   KC.AT,      KC.UP,      KC.LCBR,    KC.RCBR],
        [KC.HASH,   KC.LEFT,    KC.DOWN,    KC.RIGHT,   KC.DLR],
        [KC.LBRC,   KC.RBRC,    KC.LPRN,    KC.RPRN,    KC.AMPR],
        [l2,        KC.INS,     KC.LGUI,    KC.LSFT,    KC.SPC,     KC.BSPC],
    ]
    right = [
        [           KC.PGUP,    KC.N7,      KC.N8,      KC.N9,      KC.ASTR],
        [           KC.PGDN,    KC.N4,      KC.N5,      KC.N6,      KC.PLUS],
        [           KC.GRV,     KC.N1,      KC.N2,      KC.N3,      KC.SLSH],
        [KC.LALT,   KC.ENT,     ____,       KC.DOT,     KC.N0,      KC.EQL],
    ]
    return [left, right]

def arrows_function_keymap():
    left = [
        [KC.INS,    KC.HOME,    KC.UP,      KC.END,     KC.PGUP],
        [KC.DEL,    KC.LEFT,    KC.DOWN,    KC.RIGHT,   KC.PGDN],
        [KC.NO,     KC.VOLU,    KC.NO,      KC.NO,      KC.RESET],
        [KC.NO,     KC.VOLD,    KC.LGUI,    KC.LSFT,    KC.SPC,     KC.BSPC],
    ]
    right = [
        [           KC.UP,      KC.F7,      KC.F8,      KC.F9,      KC.F10],
        [           KC.DOWN,    KC.F4,      KC.F5,      KC.F6,      KC.F11],
        [           KC.GRV,     KC.F1,      KC.F2,      KC.F3,      KC.F12],
        [KC.LALT,   KC.ENT,     KC.TRNS,    KC.NO,      KC.NO,      KC.NO],
    ]
    return [left, right]

def get_keymap():
    return [
        query_keymap(),
        punction_digits_keymap(),
        arrows_function_keymap(),
        ]