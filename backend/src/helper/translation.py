def translate_if_target_lang(translator, message, target_lang) -> str:
    """
    Translate a message if a target language is specified.

    Args:
        translator: The translator to use.
        message: The message to translate.
        target_lang: The target language to translate to.

    Returns:
        str: The translated message.
    """
    if target_lang is None or translator is None:
        return message
    return translator.translate_text(message, target_lang=target_lang).text
