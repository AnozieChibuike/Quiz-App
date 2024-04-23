from flask import jsonify, request, Response, abort
from app import app
from lib.utils.tokens import *
from lib.utils.mail import *
import os
from app.models.user import User
from flask_jwt_extended import create_access_token

base_url = os.getenv("BASE_URL")

@app.post("/api/send-mail")
def send_email() -> tuple[Response, int]:
    data: dict = request.json # type: ignore[assignment]
    try:
        email = data["email"]
    except:
        return jsonify({"error": "Missing required data in body: email"}), 400
    
    subject: str = data.get("subject") # Email subject
    email_body = data.get("body") or data.get("template") or abort(401)  # email body
    
    message, code, status = send_mail(subject, email, body=email_body)
    if not status:
        data = {"message": message, "status": "pending"}    
    else:
        data = {"message": message, "status": "success"}
    return jsonify(data), code
