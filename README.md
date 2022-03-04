# NumAtreus Keyboard KMK Firmware for Raspberry Pi Pico

Firmware code for the Raspberry Pi Pico version of NumAtreus. Raspberry Pi Pico 版の NumAtreus の Firmware コード

Rewrite keymap.py to freely [keymap ./keymap.py](./keymap.py) as you like. keymap.py を書き換えて、自在に[キーマップ ./keymap.py](./keymap.py)を変更して楽しんで下さい。

## Install

### Circuit Python

Download and install Circuit Python firmware for Raspberry Pi PICO. Raspberry Pi PICO 用の Circuit Python のファームウェアをダウンロードして、インストールします。

https://circuitpython.org/board/raspberry_pi_pico/

To install, connect the USB while pressing the button on the PICO, it will be recognized as a USB memory called RP2, place the uf2 firmware file in it. インストールには、PICO 上のボタンを押しながら USB を接続すると、RP2 という USB メモリとして認識するため、その中に uf2 のファイムウェアのファイルを置きます。

### Install KMK Firmware and necessary files (KMK Firmware と必要ファイルのインストール)

The two required libraries are included in this repository as submodules. 必要な 2 つのライブラリが、submodule としてこのリポジトリに含まれています。

- KMK Firmware: https://github.com/KMKfw/kmk_firmware

If it is not in the libs, run the following command to check it out. libs 内にない場合、以下のコマンドを実行してチェックアウトします。

```
git submodule update -i
```

When Circuit Python is booted, it will recognize it as a USB stick called CIRCUITPY, so place the following directory in libs/. Circuit Python がブートされると、CIRCUITPY という USB メモリとして認識するため、以下のディレクトリを libs/ 内に置きます。

- libs/kmk_firmware/kmk

### Install keymap and initial files for NumAtreus for Raspberry Pi Pico version (Raspberry Pi Pico 版の NumAtreus 用のキーマップと、初期ファイルの設置)

Place the following two files in the root directory of CIRCUITPY. 以下の 2 つのファイルを、CIRCUITPY のルートディレクトリに置きます。

- boot.py
- code.py
- keymap.py

The keyboard is automatically reloaded and can be used immediately as a keyboard. 自動で再ロードされるため、キーボードとしてすぐ利用できます。

## If it does not work after keymap change (キーマップ変更後動作しない場合)

Open the CIRCUIT PYTHON console using screen. screen を使って CIRCUIT PYTHON のコンソールを開きます。

```
# Linux
screen /dev/ttyACM0 115200

# MacOS
screen /dev/tty.usbmodem00000 115200
```

For Windows, see here. Windows の場合はこちらを参照して下さい。

https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-windows

Press CTRL-C and CTRL-D to reboot CIRCUIT PYTHON. Check the error and correct that part of the error. CTRL-C、CTRL-D を押すと、CIRCUIT PYTHON がリブートします。 エラー内容を確認して、その部分を修正します。

## Sample keymaps サンプルキーマップ

Rename the following file keymap.py and place it in CIRCUITPY. 以下のファイルを keymap.py というファイル名に変えて CIRCUITPY の中に入れて下さい。

- [./keymaps/numaterus-default.py](./keymaps/numaterus-default.py) NumAterus default keymap
- [./keymaps/aterus.py](./keymaps/aterus.py) Aterus official Keymaps
