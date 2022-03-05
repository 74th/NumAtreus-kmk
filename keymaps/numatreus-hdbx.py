"""
NumAtreus hdbx
https://github.com/yohewi/qmk_firmware/blob/master/keyboards/numatreus/keymaps/hdbx/keymap.c

WindowsでJIS配列として認識しているときに、オシャレなUS配列用キーキャップを使うためのキーマップです。
Google日本語入力の場合、以下のキー設定を行うとLower,Raiseのタップでそれぞれ半角入力と全角入力を切り替えできるようになります。
  ・Henkan（入力文字なし/直接入力）に「IMEを有効化」を割り当て
  ・Muhenkan（入力文字なし/直接入力）に「IMEを無効化」を割り当て
"""
from kmk.keys import KC
import keymap_jp as JP
from kmk.handlers.sequences import send_string, simple_key_sequence

qwery_layer = 0
hdbx_layer = 1
lower_layer = 2
raise_layer = 3
game_layer = 4
adjust_layer = 5

____ = KC.TRANSPARENT

# https://github.com/qmk/qmk_firmware/blob/master/quantum/keymap_extras/keymap_jp.h
jp_circ = KC.EQL
jp_tild = KC.LSFT(jp_circ)
jp_zkhk = KC.GRV

raise_m = KC.MO(raise_layer)
lower_m = KC.MO(lower_layer)
gui_esc = KC.MT(KC.ESC, KC.LGUI, prefer_hold=True)
sft_bs = KC.MT(KC.BSPC, KC.LSFT, prefer_hold=True)
ctl_ent = KC.MT(KC.ENT, KC.LCTL, prefer_hold=True)
ctl_tab = KC.MT(KC.TAB, KC.RCTL, prefer_hold=True)
sft_del = KC.MT(KC.DEL, KC.LSFT, prefer_hold=True)
alt_lbr = KC.MT(KC.LBRC, KC.LALT, prefer_hold=True)
sft_rbr = KC.MT(KC.LBRC, KC.RSFT, prefer_hold=True)
sft_spc = KC.LSFT(KC.SPC)
wn_caps = KC.LSFT(KC.CAPS)
game_to = KC.TO(game_layer)
adjust_to = KC.TO(adjust_layer)
qwery_to = KC.TO(qwery_layer)
hdbx_to = KC.TO(hdbx_layer)

wn_scln = JP.SCLN.clone()
def wn_scln_press(key, keyboard, *args):
    for pressed_key in keyboard.keys_pressed:
        if pressed_key == KC.LSFT or pressed_key == KC.RSFT:
            keyboard.process_key(pressed_key, False)
            keyboard._send_hid()
    keyboard.process_key(JP.SCLN, True)
    keyboard._send_hid()
    keyboard.process_key(JP.SCLN, False)
    keyboard._send_hid()
    return False
wn_scln.before_press_handler(wn_scln_press)
mcr1 = send_string("0123456789")
mcr2 = send_string("hogehoge\n")
mcr3 = send_string("hoge@hoge.hoge")
mcr4 = simple_key_sequence([send_string("\"\""), KC.LEFT])
mcr5 = simple_key_sequence([send_string("<>"), KC.LEFT])
dm_ply1 = ____
dm_ply2 = ____
dm_ply3 = ____
dm_ply4 = ____
dm_ply5 = ____

def query_keymap():
    """
    Qwerty配列
    ,----------------------------------.             ,----------------------------------.
    |   Q  |   W  |   E  |   R  |   T  |             |   Y  |   U  |   I  |   O  |   P  |
    |------+------+------+------+------|             |------+------+------+------+------|
    |   A  |   S  |   D  |   F  |   G  |             |   H  |   J  |   K  |   L  |   ;  |
    |------+------+------+------+------|             |------+------+------+------+------|
    |   Z  |   X  |   C  |   V  |   B  |             |   N  |   M  |   ,  |   .  |   /  |
    |------+------+------+------+------+-------------+------+------+------+------+------|
    |Alt/[ |WINESC|   ~  |Sft/Bs|Lower |CtlEnt|Space |Raise |CtrlTb|   -  |   '  |Sft/] |
    `-----------------------------------------------------------------------------------'
    """
    left = [
        [KC.Q,      KC.W,       KC.E,       KC.R,       KC.T],
        [KC.A,      KC.S,       KC.D,       KC.F,       KC.G],
        [KC.Z,      KC.X,       KC.C,       KC.V,       KC.B],
        [alt_lbr,   gui_esc,    JP.TILD,    sft_bs,     lower_m,    ctl_ent],
    ]
    right = [
        [           KC.Y,       KC.U,       KC.I,       KC.O,       KC.P],
        [           KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN],
        [           KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH],
        [KC.SPC,    raise_m,    ctl_tab,    KC.MINS,    JP.QUOT,    sft_rbr],
    ]
    return [left, right]

def hdbx_keymap():
    """
    HDBX配列 デフォルトレイヤーをこの配列にしたい場合は、AdjustレイヤーでK (Lower + Raise + K)
    ,----------------------------------.             ,----------------------------------.
    |   Q  |   W  |   E  |   ,  |   .  |             |   Y  |   D  |   P  |   F  |   :  |
    |------+------+------+------+------|             |------+------+------+------+------|
    |   A  |   I  |   O  |   U  |   G  |             |   M  |   N  |   T  |   R  |   S  |
    |------+------+------+------+------|             |------+------+------+------+------|
    |   Z  |   X  |   C  |   V  |   B  |             |   H  |   J  |   K  |   L  |   /  |
    |------+------+------+------+------+-------------+------+------+------+------+------|
    |Alt/[ |WINESC|   ~  |Sft/Bs|Lower |CtlEnt|Space |Raise |CtrlTb|   -  |   '  |Sft/] |
    `-----------------------------------------------------------------------------------'
    """
    left = [
        [KC.Q,      KC.W,       KC.E,       KC.COMM,    KC.DOT],
        [KC.A,      KC.I,       KC.O,       KC.U,       KC.G],
        [KC.Z,      KC.X,       KC.C,       KC.V,       KC.B],
        [alt_lbr,   gui_esc,    JP.TILD,    sft_bs,     lower_m,    ctl_ent],
    ]
    right = [
        [           KC.Y,       KC.D,       KC.P,       KC.F,       KC.SCLN],
        [           KC.M,       KC.N,       KC.T,       KC.R,       KC.S],
        [           KC.H,       KC.J,       KC.K,       KC.L,       KC.SLSH],
        [KC.SPC,    raise_m,    ctl_tab,    KC.MINS,    JP.QUOT,    sft_rbr],
    ]
    return [left, right]

def lower_keymap():
    """
    ,----------------------------------.             ,----------------------------------.
    |  F1  |  F2  |  F3  |  F4  |  F5  |             |   7  |   8  |   9  |   .  | Bspc |
    |------+------+------+------+------|             |------+------+------+------+------|
    |  F6  |  F7  |  F8  |  F9  |  F10 |             |   4  |   5  |   6  |   +  |   *  |
    |------+------+------+------+------|             |------+------+------+------+------|
    |Zen/Ha|ScLock|Pause |  F11 |  F12 |             |   1  |   2  |   3  |   -  |   /  |
    |------+------+------+------+------+-------------+------+------+------+------+------|
    | Alt  | WIN  |   `  |SftDel|Lower | Ctrl |SftSpc|Raise |   0  |   ,  |   =  |Enter |
    `-----------------------------------------------------------------------------------'
    """
    left = [
        [KC.F1,     KC.F2,      KC.F3,      KC.F4,      KC.F5],
        [KC.F6,     KC.F7,      KC.F8,      KC.F9,      KC.F10],
        [KC.GRV ,   KC.SLCK,    KC.PAUSE,   KC.F11,     KC.F12],
        [KC.LALT,   KC.LGUI,    KC.GRV,     sft_del,    ____,       KC.LCTL],
    ]
    right = [
        [           KC.N7,      KC.N8,      KC.N9,      KC.DOT,     KC.BSPC],
        [           KC.N4,      KC.N5,      KC.N6,      KC.PPLS,    KC.PAST],
        [           KC.N1,      KC.N2,      KC.N3,      KC.PMNS,    KC.PSLS],
        [sft_spc,   adjust_to,  KC.N0,      KC.COMM,    KC.EQL,     KC.ENT],
    ]
    return [left, right]

def raise_keymap():
    """
    ,----------------------------------.             ,----------------------------------.
    |   !  |   @  |   #  |   $  |   %  |             | Home | App  | Ins  | Calc |PrtScr|
    |------+------+------+------+------|             |------+------+------+------+------|
    |   ^  |   &  |   *  |   \  |   |  |             | Left | Down |  Up  |Right |   ;  |
    |------+------+------+------+------|             |------+------+------+------+------|
    |   `  |   {  |   }  |   <  |   >  |             | End  | Mute |  (   |   )  |   ?  |
    |------+------+------+------+------+------+------+------+------+------+------+------|
    | Alt  | WIN  |   `  | Del  |Lower | Ctrl | Caps |Raise | Ctrl |   _  |   "  |Shift |
    `-----------------------------------------------------------------------------------'
    """
    left = [
        [KC.EXLM,   JP.AT,      KC.HASH,    KC.DLR,     KC.PERC],
        [JP.CIRC,   JP.AMPR,    JP.ASTR,    JP.YEN,     JP.PIPE],
        [JP.GRV,    JP.LCBR,    JP.RCBR,    KC.LABK,    KC.RABK],
        [KC.LALT,   KC.LGUI,    JP.GRV,     KC.DEL,     adjust_to,  KC.LCTL],
    ]
    right = [
        [           KC.HOME,    KC.APP,     KC.INS,     ____,       KC.PSCR],
        [           KC.LEFT,    KC.DOWN,    KC.UP,      KC.RGHT,    KC.SCLN],
        [           KC.END,     KC.MUTE,    KC.LPRN,    KC.RPRN,    KC.QUES],
        [wn_caps,   ____,       KC.RCTL,    KC.UNDS,    KC.DQT,     KC.RSFT],
    ]
    return [left, right]

def game_keymap():
    """
    GAME ゲームやテンキー固定で使用するレイヤーです。AdjustレイヤーでGを押下して遷移。戻るときはtoBaseから。
    ,----------------------------------.             ,----------------------------------.
    |   Q  |  Up  |   E  |   R  |   T  |             |   7  |   8  |   9  |   .  | Bspc |
    |------+------+------+------+------|             |------+------+------+------+------|
    | Left | Down |Right |   F  |   G  |             |   4  |   5  |   6  |   +  |   *  |
    |------+------+------+------+------|             |------+------+------+------+------|
    |   Z  |   X  |   C  |   V  |   B  |             |   1  |   2  |   3  |   -  |   /  |
    |------+------+------+------+------+-------------+------+------+------+------+------|
    | Alt  | Esc  |  Tab |Shift |Space | Ctrl |toBase|   \  |   0  |   ,  |   =  |Enter |
    `-----------------------------------------------------------------------------------'
    """
    left = [
        [KC.Q,      KC.UP,      KC.E,       KC.R,       KC.T],
        [KC.LEFT,   KC.DOWN,    KC.RIGHT,   KC.F,       KC.G],
        [KC.Z,      KC.X,       KC.C,       KC.V,       KC.B],
        [KC.LALT,   KC.ESC,     KC.TAB,     KC.LSFT,    KC.SPC,     KC.LCTL],
    ]
    right = [
        [           KC.N7,      KC.N8,      KC.N9,      KC.DOT,     KC.BSPC],
        [           KC.N4,      KC.N5,      KC.N6,      KC.PPLS,    KC.PAST],
        [           KC.N1,      KC.N2,      KC.N3,      KC.PMNS,    KC.PSLS],
        [adjust_to, JP.YEN,     KC.N0,      KC.COMM,    JP.EQL,     KC.ENT],
    ]
    return [left, right]

def adjust_keymap():
    """
    Adjust (Lower + Raise)
    ,----------------------------------.             ,----------------------------------.
    | MCR1 | MCR2 | MCR3 | MCR4 | MCR5 |             |DyMcr1|DyMcr2|RcMcr1|RcMcr2|StpRec|
    |------+------+------+------+------|             |------+------+------+------+------|
    |      |      |      |      |ToGAME|             |      |Qwerty| HDBX |      |      |
    |------+------+------+------+------|             |------+------+------+------+------|
    |      |      |      |      |      |             |      |      |      |      |      |
    |------+------+------+------+------+-------------+------+------+------+------+------|
    |RESET |      |      |      |      |      |      |      |      |      |      |      |
    `-----------------------------------------------------------------------------------'
    """
    left = [
        [mcr1,      mcr2,       mcr3,       mcr4,       mcr5],
        [____,      ____,       ____,       ____,       game_to],
        [____,      ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____,       ____,       ____],
    ]
    right = [
        [           dm_ply1,    dm_ply2,    dm_ply3,    dm_ply4,    dm_ply5],
        [           ____,       qwery_to,   hdbx_to,    ____,       ____],
        [           ____,       ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____,       ____,       ____],
    ]
    return [left, right]

def get_keymap():
    return [
        query_keymap(),
        hdbx_keymap(),
        lower_keymap(),
        raise_keymap(),
        game_keymap(),
        adjust_keymap(),
        ]