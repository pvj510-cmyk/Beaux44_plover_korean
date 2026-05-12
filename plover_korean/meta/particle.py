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
def undo_last_action(context: _Context, args: str) -> _Action:
    """방금 입력한 약어(단어)를 삭제합니다. 연속 실행 가능."""
    action: _Action = _Action()
    # Plover의 현재 컨텍스트에서 마지막 1단어를 가져옴
    last_words = context.last_words(1)
    
    if last_words:
        action.prev_replace = last_words[0]  # 마지막 단어를 치환 대상으로 설정
        action.text = ""                     # 빈 값으로 치환 (즉, 삭제)
        action.prev_attach = False           # 앞 단어와의 결합 해제 (안전 장치)
    return action

def apply_particle_terminal_n(context: _Context, args: str) -> _Action:
    """마지막 글자에 받침 'ㄴ'을 결합합니다. (-ㅋㄴㄹㅅ)"""
    rule_info = ParticleRuleInfo(
        vowel_particle='ㄴ',
        consonant_particle='', 
        exception_consonant=None
    )
    action: _Action = context.copy_last_action()
    last_word_list = context.last_words(1)
    
    if not last_word_list:
        return action

    original_text = last_word_list[0]
    stripped_text = original_text.rstrip()
    spaces = original_text[len(stripped_text):]

    if not stripped_text:
        return action

    processed_text = attach_particle(stripped_text, rule_info)
    
    if processed_text == stripped_text:
        return action

    action.prev_replace = original_text
    action.prev_attach = True
    action.text = processed_text + spaces
    
    return action
