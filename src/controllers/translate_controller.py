from flask import Blueprint, render_template, request
from controllers.history_controller import HistoryModel
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel

translate_controller = Blueprint("translate_controller", __name__)


@translate_controller.route('/', methods=['GET'])
def home():
    languages = LanguageModel.list_dicts()
    translate_from = request.args.get('translate_from', 'pt')
    translate_to = request.args.get('translate_to', 'en')
    text_to_translate = "O que deseja traduzir?"
    translated = "What do you want to translate?"

    return render_template(
        'index.html',
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated
    )


@translate_controller.route('/', methods=['POST'])
def translate():
    text_to_translate = request.form.get('text-to-translate')
    translate_from = request.form.get('translate-from')
    translate_to = request.form.get('translate-to')
    if not text_to_translate or not translate_from or not translate_to:
        return render_template('index.html',
                               languages=LanguageModel.list_dicts(),
                               text_to_translate=text_to_translate,
                               translate_from=translate_from,
                               translate_to=translate_to,
                               translated="Erro: dados insuficientes")
    try:
        translated = GoogleTranslator(
            source=translate_from, target=translate_to
            ).translate(text_to_translate)

        history_entry = {
            'text_to_translate': text_to_translate,
            'translated_text': translated,
            'translate_from': translate_from,
            'translate_to': translate_to,
        }
        HistoryModel._collection.insert_one(history_entry)

    except Exception as e:
        translated = f"Erro ao traduzir o texto: {str(e)}"
    return render_template(
        'index.html',
        languages=LanguageModel.list_dicts(),
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated
    )


@translate_controller.route('/reverse', methods=['POST'])
def reverse_translate():
    text_to_translate = request.form.get('text-to-translate')
    translate_from = request.form.get('translate-from')
    translate_to = request.form.get('translate-to')

    if not text_to_translate or not translate_from or not translate_to:
        return render_template('index.html',
                               languages=LanguageModel.list_dicts(),
                               text_to_translate=text_to_translate,
                               translate_from=translate_to,
                               translate_to=translate_from,
                               translated="Erro: dados insuficientes")

    try:
        original_text = GoogleTranslator(
            source=translate_from, target=translate_to
            ).translate(text_to_translate)
    except Exception as e:
        text_to_translate = f"Erro ao traduzir o texto: {str(e)}"

    return render_template(
        'index.html',
        languages=LanguageModel.list_dicts(),
        text_to_translate=original_text,
        translated=text_to_translate,
        translate_from=translate_to,
        translate_to=translate_from
    )
