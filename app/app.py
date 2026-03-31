from flask import Flask, jsonify, request, abort, render_template

def create_app():
    app = Flask(__name__)
    app.config["JSON_SORT_KEYS"] = False

    # In-memory storage
    state = {
        "workouts": [],
        "next_id": 1
    }

    # ✅ UI Route (ONLY ONE "/" ROUTE)
    @app.get("/")
    def home():
        return render_template("index.html")

    # ✅ Health check
    @app.get("/healthz")
    def healthz():
        return "ok", 200

    # ✅ Create workout
    @app.post("/api/workouts")
    def create_workout():
        data = request.get_json(force=True, silent=True) or {}

        if "name" not in data or "duration" not in data:
            abort(400, "Missing 'name' or 'duration'")

        workout = {
            "id": state["next_id"],
            "name": data["name"],
            "duration": int(data["duration"]),
            "calories": int(data.get("calories", 0))
        }

        state["next_id"] += 1
        state["workouts"].append(workout)

        return jsonify(workout), 201

    # ✅ Get all workouts
    @app.get("/api/workouts")
    def list_workouts():
        return jsonify(state["workouts"]), 200

    # ✅ Get single workout
    @app.get("/api/workouts/<int:wid>")
    def get_workout(wid):
        for w in state["workouts"]:
            if w["id"] == wid:
                return jsonify(w), 200
        abort(404)

    # ✅ Delete workout
    @app.delete("/api/workouts/<int:wid>")
    def delete_workout(wid):
        before = len(state["workouts"])
        state["workouts"] = [w for w in state["workouts"] if w["id"] != wid]

        if len(state["workouts"]) == before:
            abort(404)

        return "", 204

    return app


# Run app directly
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080)
