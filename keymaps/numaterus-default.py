"""
NumAterus default
https://github.com/yohewi/qmk_firmware/blob/master/keyboards/numatreus/keymaps/default/keymap.c

Each layer gets a name for readability, which is then used in the keymap matrix below.
The underscores don't mean anything - you can have a layer called STUFF or any other name.
Layer names don't all need to be of the same length, obviously, and you can also skip them
entirely and just use numbers.
"""
from kmk.keys import KC


quary_layer = 0
lower_layer = 1
raise_layer = 2

____ = KC.TRANSPARENT

def query_keymap():
    raise_m = KC.MO(lower_layer)
    lower_m = KC.MO(raise_layer)
    """
    Q      W      E      R      T       ||      Y     U     I     O     P
    A      S      D      F      G       ||      H     J     K     L     ;
    Z      X      C      V      B       ||      N     M     ,     .     /
    SFT    TAB    CTL    LW   space bksp||ALT   Ent   RS    -     '     =
    """
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
    """
     1      2       3     4     5       ||      6    7     8     9     0
    F1     F2      F3    F4    F5       ||     F6   F7    F8    F9    F10
    F11    F12      (     )     &       ||      `    [     ]     +     \
    lower  insert super shift space bksp|| alt Ent  fn     .     -     =
    """
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

def raise_keymap():
    """
     !      @     #     $     %        ||       ^      &    *    (     )
    DEL    ESC                         ||      PGDN  PGUP PSCR
    CAPS  volup        ENT   reset     ||                       UP
          voldn  super shift space bspc|| alt  ent        LEFT DOWN  RGHT
    """
    left = [
        [KC.EXLM,   KC.AT,      KC.HASH,    KC.DLR,     KC.PERC],
        [KC.DEL,    KC.ESC,     ____,       ____,       ____],
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

def get_keymap():
    return [
        query_keymap(),
        lower_keymap(),
        raise_keymap(),
        ]