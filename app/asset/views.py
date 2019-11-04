# -*- coding: UTF-8 -*-
__author__ = 'hunter'
from flask import render_template, session, redirect, url_for, current_app, jsonify
from .. import db
from app.models.asset import Asset
from ..email import send_email
from . import asset
from .forms import NameForm

from app.util.logger_util import logger
from app.util.response_util import json_response


@asset.route('/', methods=['GET', 'POST'])
def index():
    return "index"


@asset.route("/add", methods=["Post"])
def asset_add():
    return "2333"


@asset.route("/list")
@json_response
def asset_list():
    ret = [{
        "id": asset.id,
        "name": asset.name,
        "disk_size": asset.disk_size,
        "cpu": asset.cpu
    }for asset in Asset.list()]
    return jsonify(ret)


