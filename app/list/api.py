from flask import jsonify, request, json, session, redirect

from app.api.db_service import execute_query
from . import list


@list.route('/api/list/getTest', methods=['GET'])
def getTest():
    try:
        select_country = """
            SELECT * from table;
            """
        country_result = execute_query(select_country, 'db1')
        return jsonify({"status": "ok", "output": country_result}), 200
        
    except Exception as err:
        return jsonify({"status": "failed", "message": str(err)}), 200
