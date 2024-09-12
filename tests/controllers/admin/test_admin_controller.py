from src.models.history_model import HistoryModel
from src.models.user_model import UserModel

ADMIN_USER = {"name": "Anna", "level": "admin", "token": "token_7712"}

HISTORY_ENTRY = {
    "text_to_translate": "Hello, I feel cold today.",
    "translate_from": "en",
    "translate_to": "pt",
}


def setup_admin_user():
    user = UserModel(ADMIN_USER)
    user.save()


def setup_history_entry():
    history_entry = HistoryModel(HISTORY_ENTRY)
    history_entry.save()


def test_history_delete(app_test):
    setup_admin_user()
    setup_history_entry()

    history_registry_id = HistoryModel.find_one({"translate_from": "en"}).data[
        "_id"
    ]

    response = app_test.delete(
        f"/admin/history/{history_registry_id}",
        headers={"Authorization": "token_7712", "User": "Anna"},
    )
    assert response.status_code == 204

    deleted_entry = HistoryModel.find_one({"_id": history_registry_id})
    assert deleted_entry is None
