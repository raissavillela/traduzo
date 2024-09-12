from flask import Blueprint, make_response
from src.models.history_model import HistoryModel

history_controller = Blueprint('history_controller', __name__)


@history_controller.route("/", methods=["GET"])
def render_history_page():
    response = make_response(HistoryModel.list_as_json())
    return response
