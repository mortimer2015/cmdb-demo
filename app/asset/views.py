# -*- coding: UTF-8 -*-
__author__ = 'hunter'
from flask import jsonify

from app.models.asset import Asset
from . import asset as asset_bp
from app.util.response_util import json_response


@asset_bp.route('/', methods=['GET', 'POST'])
def index():
    return "index"


@asset_bp.route("/add", methods=["Post"])
def asset_add():
    return "2333"


@asset_bp.route("/list")
@json_response
def asset_list():
    ret = [{
        "id": asset.id,
        "name": asset.name,
        "disk_size": asset.disk_size,
        "cpu": asset.cpu
    }for asset in Asset.list()]
    return jsonify(ret)
