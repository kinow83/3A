
import logging
from flask import Response, current_app, render_template, request, make_response, redirect, jsonify, send_file
from flask_restful import Resource

@main_bp.route('/')
def index():
    return {"aaaaaaa": 1}