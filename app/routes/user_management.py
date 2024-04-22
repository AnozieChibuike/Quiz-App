from app import app
from flask import request, jsonify, Response
from app.models.user import User


@app.post("/api/user")
def user() -> tuple[Response, int]:
    try:
        body: dict = request.json  # type: ignore[assignment]
        action: str | None = body.get("action")
        if not action:
            return jsonify({"status": "error", "message": "action is required"}), 401
        if action == "create":
            return create_user(body)
        elif action == "read":
            return read_user(body)
        else:
            return jsonify({"status": "error", "message": "invalid action"}), 401
    except Exception as e:
        return (
            jsonify({"status": "error", "message": "something went wrong" + str(e)}),
            401,
        )


def create_user(body: dict) -> tuple[Response, int]:
    try:
        if User.get(username=body.get("username")):
            return jsonify({"status": "error", "message": "user already exists"}), 401
        if User.get(email=body.get("email")):
            return jsonify({"status": "error", "message": "user already exists"}), 401
        required_fields: list[str] = ["fullname", "email", "username", "phone"]
        if not all(field in body for field in required_fields):
            return (
                jsonify(
                    {
                        "status": "error",
                        "message": f"missing required field: {required_fields}",
                    }
                ),
                401,
            )
        all_field: list[str] = [*required_fields, "image_url", "is_admin", "bio"]
        filtered_body: dict[str, str] = {
            key: value for key, value in body.items() if key in all_field
        }
        user: User = User(**filtered_body)
        user.set_password(body["password"])
        user.save()
        return (
            jsonify(
                {"status": "success", "message": "user created", "body": user.to_dict()}
            ),
            200,
        )
    except KeyError as e:
        return jsonify({"status": "error", "message": f"{e} missing in body"}), 401
    except TypeError as e:
        return jsonify({"status": "error", "message": str(e)}), 401
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 401

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