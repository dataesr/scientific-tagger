import redis
from rq import Queue, Connection
from flask import render_template, Blueprint, jsonify, request, current_app

from project.server.main.tasks import create_task_classify, create_task_calibrate

main_blueprint = Blueprint("main", __name__,)
from project.server.main.logger import get_logger

logger = get_logger(__name__)


@main_blueprint.route("/", methods=["GET"])
def home():
    return render_template("main/home.html")

@main_blueprint.route("/classify", methods=["POST"])
def run_task_classify():
    args = request.get_json(force=True)
    with Connection(redis.from_url(current_app.config["REDIS_URL"])):
        q = Queue("tagger", default_timeout=21600)
        task = q.enqueue(create_task_classify, args)
    response_object = {
        "status": "success",
        "data": {
            "task_id": task.get_id()
        }
    }
    return jsonify(response_object), 202

@main_blueprint.route("/classify_one", methods=["POST"])
def run_task_classify_one():
    args = request.get_json(force=True)
    response_object = create_task_classify(args)
    return jsonify(response_object), 202


@main_blueprint.route("/calibrate", methods=["POST"])
def run_task_calibrate():
    args = request.get_json(force=True)
    logger.debug(args)
    with Connection(redis.from_url(current_app.config["REDIS_URL"])):
        q = Queue("tagger", default_timeout=216000)
        task = q.enqueue(create_task_calibrate, args)
    response_object = {
        "status": "success",
        "data": {
            "task_id": task.get_id()
        }
    }
    return jsonify(response_object), 202

@main_blueprint.route("/tasks/<task_id>", methods=["GET"])
def get_status(task_id):
    with Connection(redis.from_url(current_app.config["REDIS_URL"])):
        q = Queue("tagger")
        task = q.fetch_job(task_id)
    if task:
        response_object = {
            "status": "success",
            "data": {
                "task_id": task.get_id(),
                "task_status": task.get_status(),
                "task_result": task.result,
            },
        }
    else:
        response_object = {"status": "error"}
    return jsonify(response_object)
