"""Stenography definition for Korean based on the 47-key Sorizava layout."""

from typing import Tuple, Dict, List, Optional

# fmt: off
# Consonant groups don't internally follow a steno order when constructing words.
KEYS: Tuple[str] = (
    # 초성 - Initial consonant
    'ㅊ-', 'ㅌ-', 'ㅋ-', 'ㅂ-', 'ㅍ-',
    'ㅅ-', 'ㄷ-', 'ㅈ-', 'ㄱ-', # '-ㅋ',
    'ㅁ-', 'ㄹ-', 'ㄴ-', 'ㅎ-', # 'ㅢ-',

    # 중성 - Medial vowel
    'ㅢ-',
    'ㅗ-', 'ㅏ-', 'ㅜ-',
    '-ㅡ', '-ㅓ', '-ㅣ',

    # 종성 - Final consonant
    '-ㄲ', '-ㅎ', '-ㅌ', '-ㅊ', '-ㅍ', '-ㅋ',
    '-ㄱ', '-ㄴ', '-ㄹ', '-ㅅ', '-ㅂ',
    '-ㅆ', '-ㅇ', '-ㅁ', '-ㄷ', '-ㅈ',

    # 숫자를 맨 뒤에 배치 (동시 입력 시 한글 뒤에 숫자가 붙음)
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',MY_ACTION_A
)

IMPLICIT_HYPHEN_KEYS: Tuple[str] = (
    'ㅢ-',
    'ㅗ-', 'ㅏ-', 'ㅜ-',
    '-ㅡ', '-ㅓ', '-ㅣ'
)

SUFFIX_KEYS: Tuple[str] = ()

# This system has explicit number keys, so there is no need for these.
NUMBER_KEY: str = None
NUMBERS: Dict[str, str] = {}

# Can be overridden or alternatives can be made in a dictionary.
UNDO_STROKE_STENO: str = ''

ORTHOGRAPHY_RULES: List[Tuple[str, str]] = []
ORTHOGRAPHY_RULES_ALIASES: Dict[str, str] = {}
ORTHOGRAPHY_WORDLIST: Optional[str] = None

KEYMAPS: Dict[str, Dict[str, Tuple[str]]] = {
    'Keyboard': {
        'ㅊ-': '1',
        'ㅌ-': '2',
        'ㅋ-': '3',
        'ㅂ-': '4',
        'ㅍ-': '5',

        'ㅅ-': 'q',
        'ㄷ-': 'w',
        'ㅈ-': 'e',
        'ㄱ-': 'r',
        '-ㅋ': 't',

        'ㅁ-': 'a',
        'ㄹ-': 's',
        'ㄴ-': 'd',
        'ㅎ-': 'f',
        'ㅢ-': 'g',

        'ㅗ-': 'x',
        'ㅏ-': 'c',
        'ㅜ-': 'v',


        '-ㅡ': 'n',
        '-ㅓ': 'm',
        '-ㅣ': ',',

        '-ㄲ': '6',
        '-ㅎ': '7',
        '-ㅌ': '8',
        '-ㅊ': '9',
        '-ㅍ': '0',

        '-ㄱ': 'y',
        '-ㄴ': 'u',
        '-ㄹ': 'i',
        '-ㅅ': 'o',
        '-ㅂ': 'p',

        '-ㅆ': 'h',
        '-ㅇ': 'j',
        '-ㅁ': 'k',
        '-ㄷ': 'l',
        '-ㅈ': ';',

        'arpeggiate': 'b',
        'no-op': ()
    },
    'Gemini PR': {
        'ㅊ-': '#2',
        'ㅌ-': '#3',
        'ㅋ-': '#4',
        'ㅂ-': '#5',
        'ㅍ-': '#6',

        'ㅅ-': 'S1-',
        'ㄷ-': 'T-',
        'ㅈ-': 'P-',
        'ㄱ-': 'H-',
        '-ㅋ': '*1',

        'ㅁ-': 'S2-',
        'ㄹ-': 'K-',
        'ㄴ-': 'W-',
        'ㅎ-': 'R-',
        'ㅢ-': '*3',

        'ㅗ-': 'Fn',
        'ㅏ-': 'A-',
        'ㅜ-': 'O-',


        '-ㅡ': '-E',
        '-ㅓ': '-U',
        '-ㅣ': 'pwr',

        '-ㄲ': '#7',
        '-ㅎ': '#8',
        '-ㅌ': '#9',
        '-ㅊ': '#A',
        '-ㅍ': '#B',

        '-ㄱ': '*2',
        '-ㄴ': '-F',
        '-ㄹ': '-P',
        '-ㅅ': '-L',
        '-ㅂ': '-T',

        '-ㅆ': '*4',
        '-ㅇ': '-R',
        '-ㅁ': '-B',
        '-ㄷ': '-G',
        '-ㅈ': '-S',

        'no-op': ('#1', '#C', 'res1', 'res2')
    }
}

DICTIONARIES_ROOT: str = 'asset:plover_korean:system/sorizava/dictionaries'
DEFAULT_DICTIONARIES: List[str] = [
    'ko_sorizava_base.py',
    'ko_sorizava_main.json'
]
