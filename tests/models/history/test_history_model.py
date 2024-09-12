import json
from src.models.history_model import HistoryModel


def test_request_history():
    response = HistoryModel.list_as_json()
    response_data = json.loads(response)

    expected_entries = [
        {
            "text_to_translate": "Hi, would you like some ice cream?",
            "translate_from": "en",
            "translate_to": "pt"
        },
        {
            "text_to_translate": "What time does the attraction open?",
            "translate_from": "en",
            "translate_to": "pt"
        }
    ]

    assert len(response_data) == len(expected_entries)

    for expected_entry in expected_entries:
        assert any(
            entry["text_to_translate"] == expected_entry
            ["text_to_translate"] and
            entry["translate_from"] == expected_entry["translate_from"] and
            entry["translate_to"] == expected_entry["translate_to"]
            for entry in response_data
        )
