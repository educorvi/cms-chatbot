def translate_if_source_lang(translator, message, source_lang) -> str:
    if source_lang is None or translator is None:
        return message
    return translator.translate_text(message, target_lang=source_lang).text
