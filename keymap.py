from kmk.keys import KC
from kmk.handlers.sequences import simple_key_sequence, send_string


quary_layer = 0
lower_layer = 1
raise_layer = 2

____ = KC.TRANSPARENT

def query_keymap():
    raise_m = KC.MO(lower_layer)
    lower_m = KC.MO(raise_layer)
    left = [
        [KC.Q,      KC.W,       KC.E,       KC.R,       KC.T],
        [KC.A,      KC.S,       KC.D,       KC.F,       KC.G],
        [KC.Z,      KC.X,       KC.C,       KC.V,       KC.B],
        [KC.LSFT,   KC.TAB,     KC.LCTL,    lower_m,    KC.SPC,     KC.BSPC],
    ]
    right = [
        [           KC.Y,       KC.U,       KC.I,       KC.O,       KC.P],
        [           KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN],
        [           KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH],
        [KC.LALT,   KC.ENT,     raise_m,    KC.MINS,    KC.QUOT,    KC.PEQL],
    ]
    return [left, right]

def lower_keymap():
    left = [
        [KC.EXLM,   KC.AT,      KC.HASH,    KC.DLR,     KC.PERC],
        [KC.DELT,   KC.ESC,     ____,       ____,       ____],
        [KC.CAPS,   KC.VOLU,    ____,       KC.ENT,     ____],
        [____,      KC.VOLD,    KC.LGUI,    KC.LSFT,    KC.SPC,     KC.BSPC],
    ]
    right = [
        [           KC.CIRC,    KC.AMPR,    KC.ASTR,    KC.LPRN,    KC.RPRN],
        [           KC.PGDN,    KC.PGUP,    KC.PSCR,    ____,       ____],
        [           ____,       ____,       ____,       KC.UP,      ____],
        [KC.LALT,   KC.ENT,     ____,       KC.LEFT,    KC.DOWN,    KC.RGHT],
    ]
    return [left, right]

def raise_keymap():
    left = [
        [KC.N1,     KC.N2,      KC.N3,      KC.N4,      KC.N5],
        [KC.F1,     KC.F2,      KC.F3,      KC.F4,      KC.F5],
        [KC.F11,    KC.F12,     KC.LPRN,    KC.RPRN,    KC.AMPR],
        [KC.NO,     KC.INS,     KC.LGUI,    KC.LSFT,    KC.SPC,     KC.BSPC],
    ]
    right = [
        [           KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0],
        [           KC.F6,      KC.F7,      KC.F8,      KC.F9,      KC.F10],
        [           KC.GRV,     KC.LBRC,    KC.RBRC,    KC.PSLS,    KC.BSLS],
        [KC.LALT,   KC.ENT,     KC.TRNS,    KC.DOT,     KC.PMNS,    KC.EQL],
    ]
    return [left, right]

def get_keymap():
    return [
        query_keymap(),
        lower_keymap(),
        raise_keymap(),
        ]