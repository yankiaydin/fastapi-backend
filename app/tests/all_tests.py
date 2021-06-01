from starlette.testclient import TestClient
from app.run import app

client = TestClient(app)

def test_token_succesful():
    response = client.post("/token", files= dict(username= "hakan", password= "pass1"))
    assert response.status_code == 200
    assert "acces_token" in response.json()