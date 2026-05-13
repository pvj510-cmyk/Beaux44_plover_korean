"""Meta plugins for Korean particles."""

from typing import Optional

from plover.formatting import _Context, _Action

from plover_korean.hangeul import (
    ParticleRuleInfo,
    load_raw_rule,
    attach_particle
)


def apply_particle(context: _Context,
                   rule_info: Optional[ParticleRuleInfo]) -> _Action:
    """Creates an action based on the particle rule info.

    The action will replace the last word in the context with the word plus
    the chosen particle based on the particle rule info.

    Args:
        context: The context of actions in Plover.
        rule_info: The particle rule information to use.

    Returns:
        An action with a particle attached to the last word in the context.
        If the rule info is invalid, a blank new action will be returned.
    """

    action: _Action = context.copy_last_action()

    if rule_info is None:
        return action

    last_word = ''.join(context.last_words(1))
    action.prev_replace = last_word
    action.prev_attach = True
    action.next_attach = False
    action.word = None
    action.text = attach_particle(last_word, rule_info)

    return action


def apply_particle_generic(context: _Context, args: str) -> _Action:
    """Creates an action based on the raw particle rule info.

    Args:
        context: The context of actions in Plover.
        args: The arguments containing the raw particle rule info.
            Format is a comma-delimited string corresponding to
            ParticleRuleInfo like 'vowel,consonant,except_consonant'.
            Both vowel and consonant must be provided.

    Returns:
        The next action for Plover to perform.
    """

    try:
        rule_info = load_raw_rule(args)
    except ValueError:
        pass

    return apply_particle(context, rule_info)


def apply_particle_neun(context: _Context, args: str) -> _Action:
    """Creates an action for the 는/은 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='는',
        consonant_particle='은',
        exception_consonant=None
    ))

def apply_particle_ga(context: _Context, args: str) -> _Action:
    """Creates an action for the 가/이 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='가',
        consonant_particle='이',
        exception_consonant=None
    ))


def apply_particle_reul(context: _Context, args: str) -> _Action:
    """Creates an action for the 를/을 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='를',
        consonant_particle='을',
        exception_consonant=None
    ))


def apply_particle_da(context: _Context, args: str) -> _Action:
    """Creates an action for the 다/이다 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='다',
        consonant_particle='이다',
        exception_consonant=None
    ))


def apply_particle_ra(context: _Context, args: str) -> _Action:
    """Creates an action for the 라/이라 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='라',
        consonant_particle='이라',
        exception_consonant=None
    ))


def apply_particle_ya(context: _Context, args: str) -> _Action:
    """Creates an action for the 야/아 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='야',
        consonant_particle='아',
        exception_consonant=None
    ))


def apply_particle_wa(context: _Context, args: str) -> _Action:
    """Creates an action for the 와/과 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='와',
        consonant_particle='과',
        exception_consonant=None
    ))


def apply_particle_rang(context: _Context, args: str) -> _Action:
    """Creates an action for the 랑/이랑 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='랑',
        consonant_particle='이랑',
        exception_consonant=None
    ))


def apply_particle_na(context: _Context, args: str) -> _Action:
    """Creates an action for the 나/이나 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='나',
        consonant_particle='이나',
        exception_consonant=None
    ))


def apply_particle_ro(context: _Context, args: str) -> _Action:
    """Creates an action for the 로/으로 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='로',
        consonant_particle='으로',
        exception_consonant='ㄹ'
    ))


def apply_particle_myeo(context: _Context, args: str) -> _Action:
    """Creates an action for the 며/이며 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='며',
        consonant_particle='이며',
        exception_consonant=None
    ))


# 파일 맨 아래에 붙여넣기
import unicodedata

def undo_last_action(context: _Context, args: str) -> _Action:
    """화면에서 즉시 마지막 입력을 지우도록 강제합니다."""
    action: _Action = _Action()
    
    # 마지막 단어 1개를 가져옵니다.
    last_word_list = context.last_words(1)
    
    if last_word_list and last_word_list[0]:
        target = last_word_list[0]
        
        # 1. 화면에 있는 글자를 '즉시' 지우도록 설정
        action.prev_replace = target
        
        # 2. 새로운 텍스트는 아무것도 입력하지 않음 (삭제 효과)
        action.text = ""
        
        # 3. Plover 버퍼에서 완전히 도려내기 위해 결합 속성 부여
        action.prev_attach = True
        
        # 4. 중요: 다음 입력이 이 삭제된 자리에 영향을 주지 않도록 상태 초기화
        action.word = None
        
        return action

    return action

def apply_particle_terminal_n(context: _Context, args: str) -> _Action:
    """마지막 글자에 받침 'ㄴ'을 합성합니다. (예: 나라 -> 나란)"""
    action: _Action = context.copy_last_action()
    last_word_list = context.last_words(1)
    if not last_word_list: return action

    original_text = last_word_list[0]
    if not original_text: return action

    # 마지막 글자 하나만 추출 (예: '나라'에서 '라')
    last_char = original_text[-1]
    
    # 한글인지 확인하고 받침 'ㄴ' 합성
    if '가' <= last_char <= '힣':
        char_code = ord(last_char) - 0xAC00
        jong = char_code % 28
        
        # 받침이 없을 때만 'ㄴ'(코드 4)을 추가하여 합성
        if jong == 0:
            new_char = chr(ord(last_char) + 4)
            action.prev_replace = original_text
            # 앞부분은 그대로 두고 마지막 글자만 바뀐 글자로 교체 (예: '나' + '란')
            action.text = original_text[:-1] + new_char
            action.prev_attach = True
            return action

    # 한글이 아니거나 이미 받침이 있으면 변환 없이 그대로 반환
    return action
