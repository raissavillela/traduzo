from flask import Blueprint, jsonify
from src.models.history_model import HistoryModel


history_controller = Blueprint('history_controller', __name__)


@history_controller.route('/history/', methods=['GET'])
def get_history():
    try:
        history_data = HistoryModel.list_as_json()
        return jsonify(history_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
