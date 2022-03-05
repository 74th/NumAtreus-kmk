# 組み込みの kmk_firmware/kmk/extensions/keymap_extras/keymap_jp.py は
# 既存の BSLS を破壊してしまうため、JP用にこちらを使う

# original
# https://github.com/qmk/qmk_firmware/blob/master/quantum/keymap_extras/keymap_jp.h
from kmk.keys import KC

# ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
# │Z↔︎H│ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │ 0 │ - │ ^ │ ¥ │   │
# ├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴───┤
# │     │ Q │ W │ E │ R │ T │ Y │ U │ I │ O │ P │ @ │ [ │     │
# ├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┐    │
# │ Eisū │ A │ S │ D │ F │ G │ H │ J │ K │ L │ ; │ : │ ] │    │
# ├──────┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴────┤
# │        │ Z │ X │ C │ V │ B │ N │ M │ , │ . │ / │ \ │      │
# ├─────┬──┴┬──┴──┬┴───┴┬──┴───┴──┬┴───┴┬──┴┬──┴┬──┴┬──┴┬─────┤
# │     │   │     │Muhen│         │ Hen │K↔H│   │   │   │     │
# └─────┴───┴─────┴─────┴─────────┴─────┴───┴───┴───┴───┴─────┘

# Row 1
ZKHK = KC.GRV  # Zenkaku ↔︎ Hankaku ↔ Kanji (半角 ↔ 全角 ↔ 漢字)
N1   = KC.N1    # 1
N2   = KC.N2    # 2
N3   = KC.N3    # 3
N4   = KC.N4    # 4
N5   = KC.N5    # 5
N6   = KC.N6    # 6
N7   = KC.N7    # 7
N8   = KC.N8    # 8
N9   = KC.N9    # 9
N0   = KC.N0    # 0
MINS = KC.MINS # -
CIRC = KC.EQL  # ^
YEN  = KC.INT3 # ¥

# Row 2
Q    = KC.Q    # Q
W    = KC.W    # W
E    = KC.E    # E
R    = KC.R    # R
T    = KC.T    # T
Y    = KC.Y    # Y
U    = KC.U    # U
I    = KC.I    # I
O    = KC.O    # O
P    = KC.P    # P
AT   = KC.LBRC # @
LBRC = KC.RBRC # [

# Row 3
EISU = KC.CAPS # Eisū (英数)
A    = KC.A    # A
S    = KC.S    # S
D    = KC.D    # D
F    = KC.F    # F
G    = KC.G    # G
H    = KC.H    # H
J    = KC.J    # J
K    = KC.K    # K
L    = KC.L    # L
SCLN = KC.SCLN # ;
COLN = KC.QUOT # :
RBRC = KC.NUHS # ]

# Row 4
Z    = KC.Z    # Z
X    = KC.X    # X
C    = KC.C    # C
V    = KC.V    # V
B    = KC.B    # B
N    = KC.N    # N
M    = KC.M    # M
COMM = KC.COMM # ,
DOT  = KC.DOT  # .
SLSH = KC.SLSH # /
BSLS = KC.INT1 # (backslash)

# Row 5
MHEN = KC.INT5 # Muhenkan (無変換)
HENK = KC.INT4 # Henkan (変換)
KANA = KC.INT2 # Katakana ↔ Hiragana ↔ Rōmaji (カタカナ ↔ ひらがな ↔ ローマ字)

# shifted symbols
# ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
# │   │ ! │ " │ # │ $ │ % │ & │ ' │ ( │ ) │   │ = │ ~ │ | │   │
# ├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴───┤
# │     │   │   │   │   │   │   │   │   │   │   │ ` │ { │     │
# ├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┐    │
# │ Caps │   │   │   │   │   │   │   │   │   │ + │ * │ } │    │
# ├──────┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴────┤
# │        │   │   │   │   │   │   │   │ < │ > │ ? │ _ │      │
# ├─────┬──┴┬──┴──┬┴───┴┬──┴───┴──┬┴───┴┬──┴┬──┴┬──┴┬──┴┬─────┤
# │     │   │     │     │         │     │   │   │   │   │     │
# └─────┴───┴─────┴─────┴─────────┴─────┴───┴───┴───┴───┴─────┘

# Row 1
EXLM = KC.LSFT(N1)    # !
DQUO = KC.LSFT(N2)    # "
HASH = KC.LSFT(N3)    # #
DLR  = KC.LSFT(N4)    # $
PERC = KC.LSFT(N5)    # %
AMPR = KC.LSFT(N6)    # &
QUOT = KC.LSFT(N7)    # '
LPRN = KC.LSFT(N8)    # (
RPRN = KC.LSFT(N9)    # )
EQL  = KC.LSFT(MINS) # =
TILD = KC.LSFT(CIRC) # ~
PIPE = KC.LSFT(YEN)  # |

# Row 2
GRV  = KC.LSFT(AT)   # `
LCBR = KC.LSFT(LBRC) # {

# Row 3
CAPS = KC.LSFT(EISU) # Caps Lock
PLUS = KC.LSFT(SCLN) # +
ASTR = KC.LSFT(COLN) # *
RCBR = KC.LSFT(RBRC) # }

# Row 4
LABK = KC.LSFT(COMM) # <
RABK = KC.LSFT(DOT)  # >
QUES = KC.LSFT(SLSH) # ?
UNDS = KC.LSFT(BSLS) # _