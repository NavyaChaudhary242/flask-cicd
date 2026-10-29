from app import app, add

def test_add():
    assert add(2, 3) == 5

def test_home():
    assert app.test_client().get("/").status_code == 200