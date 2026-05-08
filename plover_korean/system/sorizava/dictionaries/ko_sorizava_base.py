"""Core functionality for the Sorizava-based Korean stenography system."""

from typing import Tuple, List
from plover.system import Stroke

import hgtk

LONGEST_KEY = 1
OPERATOR_ATTACH = "{^}"

INITIALS = {
  Stroke("ㄱ"): "ㄱ",
  Stroke("ㄱㅎ"): "ㄲ",
  Stroke("ㄴ"): "ㄴ",
  Stroke("ㄷ"): "ㄷ",
  Stroke("ㄷㄹ"): "ㄸ",
  Stroke("ㄹ"): "ㄹ",
  Stroke("ㅁ"): "ㅁ",
  Stroke("ㅂ"): "ㅂ",
  Stroke("ㅂㄱ"): "ㅃ",
  Stroke("ㅅ"): "ㅅ",
  Stroke("ㅅㅁ"): "ㅆ",
  Stroke(""): "ㅇ",
  Stroke("ㅈ"): "ㅈ",
  Stroke("ㅈㄴ"): "ㅉ",
  Stroke("ㅊ"): "ㅊ",
  Stroke("ㅋ"): "ㅋ",
  Stroke("ㅌ"): "ㅌ",
  Stroke("ㅍ"): "ㅍ",
  Stroke("ㅎ"): "ㅎ",
}

VOWELS = {
  Stroke("ㅏ"): "ㅏ",
  Stroke("ㅏㅣ"): "ㅐ",
  Stroke("ㅏㅡ"): "ㅑ",
  Stroke("ㅏㅓ"): "ㅒ",
  Stroke("ㅓ"): "ㅓ",
  Stroke("ㅓㅣ"): "ㅔ",
  Stroke("ㅡㅓ"): "ㅕ",
  Stroke("ㅏㅓㅣ"): "ㅖ",
  Stroke("ㅗ"): "ㅗ",
  Stroke("ㅗㅏ"): "ㅘ",
  Stroke("ㅗㅏㅣ"): "ㅙ",
  Stroke("ㅗㅣ"): "ㅚ",
  Stroke("ㅗㅡ"): "ㅛ",
  Stroke("ㅜ"): "ㅜ",
  Stroke("ㅜㅓ"): "ㅝ",
  Stroke("ㅜㅓㅣ"): "ㅞ",
  Stroke("ㅜㅣ"): "ㅟ",
  Stroke("ㅜㅡ"): "ㅠ",
  Stroke("ㅡ"): "ㅡ",
  Stroke("ㅢ"): "ㅢ",
  Stroke("ㅣ"): "ㅣ",
}

FINALS = {
  Stroke(""): "",
  Stroke("-ㄱ"): "ㄱ",
  Stroke("-ㄲ"): "ㄲ",
  Stroke("-ㄱㅅ"): "ㄳ",
  Stroke("-ㄴ"): "ㄴ",
  Stroke("-ㄴㅈ"): "ㄵ",
  Stroke("-ㅎㄴ"): "ㄶ",
  Stroke("-ㄷ"): "ㄷ",
  Stroke("-ㄹ"): "ㄹ",
  Stroke("-ㄱㄹ"): "ㄺ",
  Stroke("-ㄹㅁ"): "ㄻ",
  Stroke("-ㄹㅂ"): "ㄼ",
  Stroke("-ㄹㅅ"): "ㄽ",
  Stroke("-ㅌㄹ"): "ㄾ",
  Stroke("-ㅍㄹ"): "ㄿ",
  Stroke("-ㅎㄹ"): "ㅀ",
  Stroke("-ㅁ"): "ㅁ",
  Stroke("-ㅂ"): "ㅂ",
  Stroke("-ㅅㅂ"): "ㅄ",
  Stroke("-ㅅ"): "ㅅ",
  Stroke("-ㅆ"): "ㅆ",
  Stroke("-ㅇ"): "ㅇ",
  Stroke("-ㅈ"): "ㅈ",
  Stroke("-ㅊ"): "ㅊ",
  Stroke("-ㅋ"): "ㅋ",
  Stroke("-ㅌ"): "ㅌ",
  Stroke("-ㅍ"): "ㅍ",
  Stroke("-ㅎ"): "ㅎ",
}

INITIAL_KEYS = Stroke("ㅊㅌㅋㅂㅍㅅㄷㅈㄱㅁㄹㄴㅎ")
VOWEL_KEYS = Stroke("ㅢㅗㅏㅜㅡㅓㅣ")
FINAL_KEYS = Stroke("-ㄲㅎㅌㅊㅍㅋㄱㄴㄹㅅㅂㅆㅇㅁㄷㅈ")


def lookup(strokes: Tuple[str]) -> str:
  """Gets the text that the provided strokes would output.

  Args:
      strokes: A tuple of strokes to look up text for.

  Returns:
      The text text output for the stroke.

  Raises:
      KeyError: The lookup failed to find any matching text.
  """
  if len(strokes) != LONGEST_KEY:
    raise KeyError

  stroke = Stroke(strokes[0])
  initial, vowel, final = (
    stroke & INITIAL_KEYS,
    stroke & VOWEL_KEYS,
    stroke & FINAL_KEYS,
  )
  initial, vowel, final = (
    INITIALS.get(initial, ""),
    VOWELS.get(vowel),
    FINALS.get(final, ""),
  )
  if not vowel:
    raise KeyError

  try:
    hangul = hgtk.letter.compose(initial, vowel, final)
    return f"{OPERATOR_ATTACH}{hangul}{OPERATOR_ATTACH}"
  except:
    raise KeyError


def reverse_lookup(text: str) -> List[Tuple[str]]:
  """Gets the possible strokes that would result in the provided text.

  Args:
      text: The text to look up strokes for.

  Returns:
      A list of stroke tuples. An empty list will be returned if no possible
      strokes were found.
  """

  return []
