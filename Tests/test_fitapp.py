import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
from app.app import app

def test_health():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200


def test_crud_workout():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    
    # create
    r = client.post("/api/workouts", json={"name": "Run", "duration": 30, "calories": 250})
    assert r.status_code == 201
    item = r.get_json()
    assert item["id"] == 1

    # list
    r = client.get("/api/workouts")
    assert r.status_code == 200
    items = r.get_json()
    assert len(items) == 1

    # get
    r = client.get("/api/workouts/1")
    assert r.status_code == 200
    assert r.get_json()["name"] == "Run"

    # delete
    r = client.delete("/api/workouts/1")
    assert r.status_code == 204

    # get 404
    r = client.get("/api/workouts/1")
    assert r.status_code == 404
