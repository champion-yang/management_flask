from . import account
from logger import logger
from flask import request, jsonify
from utils.response import Response


@account.route('/login', methods=['POST'])
def login():
    input_json = request.json
    logger.info(f"receive params is: {input_json}")
    res = Response()
    res.Code = 200
    res.Message = "login success"
    res.Result = {
        "data": None
    }
    return jsonify(res.object_to_dict()), 200

