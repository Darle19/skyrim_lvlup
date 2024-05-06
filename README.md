# Skyrim Healing Leveling Script

This Python script automates the process of leveling up healing skills in Skyrim by simulating mouse and keyboard inputs to repeatedly cast a self-healing spell. It's designed to make the grind of increasing healing skills more efficient and less tedious.

## Installation

To use this script, you'll need Python installed on your computer, along with the `pynput` and `keyboard` packages. Here’s how you can set it up:

1. Ensure that Python is installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).
2. Install the required Python packages by running the following command in your command prompt or terminal:
`pip install pynput keyboard`

## Usage

Follow these steps to use the script:

1. Start Skyrim and load your game.
2. Position your character in mountain top where snow storm will damage you over time (it works only before meeting Paarthurnax, or any other env damaging places if you find one).
3. Run the script by executing the following command in your terminal or command prompt:
`python skyrim_magic_leveling.py`
4. Press the '\\' key to start the script. The script will simulate left and right mouse clicks to cast the healing spell while moving forward and backwards.
5. Make some iterations to find a best starting point.
6. To stop the script, press the '\\' key again. The script will cease operations and exit.

**Note:** The script uses the '\\' key to toggle its operation. Ensure this key is not bound to any critical functions in-game to avoid unintended behavior.

## Contributing

Contributions to the script are welcome. If you have improvements or bug fixes, feel free to fork the repository and submit a pull request.

## License

This script is released under the MIT License. See the `LICENSE` file in the repository for full details.
