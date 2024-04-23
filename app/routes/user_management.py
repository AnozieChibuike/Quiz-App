from app import app
from flask import request, jsonify, Response
from app.models.user import User
from utils.schemas.user import UserSchema, Email
from datetime import timedelta
from flask_jwt_extended import get_jwt_identity, jwt_required, create_access_token
from utils.mail import *
from utils.tokens import *

user_schema: UserSchema = UserSchema()

origin = app.config.get("ORIGIN")


@app.post("/api/user")
def user() -> tuple[Response, int]:
    try:
        body: dict = request.json  # type: ignore[assignment]
        action: str | None = body.get("action")
        if not action:
            return jsonify({"status": "error", "message": "action is required"}), 400
        if action == "create":
            return create_user(body)
        elif action == "read":
            return read_user(body)
        else:
            return jsonify({"status": "error", "message": "invalid action"}), 400
    except Exception as e:
        return (
            jsonify({"error": "something went wrong" + str(e)}),
            500,
        )


def create_user(body: dict) -> tuple[Response, int]:
    try:
        errors: dict[str, list[str]] = user_schema.validate(body)
        if errors:
            return jsonify({"error": errors}), 400
        if User.get(username=body.get("username")):
            return jsonify({"error": {"username":["user exists with username"]}}), 400
        if User.get(email=body.get("email")):
            return jsonify({"error": {"email":["email already exists"]}}), 400
        user: User = User(**user_schema.load(body))
        user.email_verified = True
        user.save()
        access_token = create_access_token(body['email'])
        return (
            jsonify(
                {"status": "success", "message": "user created", "body": user.to_dict(),"token":access_token}
            ),
            200,
        )
    except Exception as e:
        return jsonify({"error":str(e)}), 400


def read_user(body: dict) -> tuple[Response, int]:
    email = body.get("email")
    user_id = body.get("id")
    username = body.get("username")
    if user_id:
        user = User.get_or_404(id=user_id)
        return jsonify({"data": user.to_dict()}), 200
    if email:
        user = User.get_or_404(email=email)
        return jsonify({"data": user.to_dict()}), 200
    if username:
        user = User.get_or_404(username=username)
        return jsonify({"data": user.to_dict()}), 200
    all_users: list[dict] = [i.to_dict() for i in User.all()]
    return jsonify(all_users), 200


@app.post("/api/magic_link")
def magic_link() -> tuple[Response, int]:
    try:
        body: dict = request.json  # type: ignore[assignment]
        email = body["email"]
        error = Email().validate({"email": email})
        if error:
            return jsonify({"status": "error", "message": error}), 400
        token = generate_token(email)
        subject = "Magic Link"
        email_body = f"""
            <p>Here is your magic link:</p>
            <p>
                <a href="{origin}/verify?token={token}">Click Me</a>
            </p>
        """
        message, code, status = send_mail(subject, email, html=email_body)
        if not status:
            data = {"message": message, "status": "pending"}
        else:
            data = {"message": message, "status": "success"}
        return jsonify(data), code
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


@app.post("/api/magic_link/verify")
def verify_magic_link() -> tuple[Response, int]:
    token = request.json.get("token")
    if not token:
        return jsonify({"message": "token is required"}), 400
    data, code, status = verify_token(token)
    if not status:
        return jsonify(data), code
    email = data["payload"]["email"]
    user: User | None = User.get(email=email)
    if not user:
        return jsonify({"email": email}), 404
    access_token = create_access_token(email)
    return jsonify({"token": access_token}), 200


@app.route("/pro")
@jwt_required()
def pro() -> tuple[Response, int]:
    current_user = get_jwt_identity()
    return jsonify({"message": "You are a pro user", "user": current_user}), 200
