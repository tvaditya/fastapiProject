import json
from sqlalchemy.orm import Session

def test_create_job(client, normal_user_token_headers):
    data = {
        "title": "Python Developer",
        "company": "Boogle",
        "company_url": "https://www.boogle.com",
        "location": "Brazil, SP",
        "description": "Lorem Ipsum",
        "date_posted": "2021-05-23"
    }

    response = client.post("/job/create-job", json.dumps(data), headers=normal_user_token_headers)
    assert response.status_code == 200
    assert response.json()["company_url"] == "https://www.boogle.com"
    assert response.json()["description"] == "Lorem Ipsum"
    assert response.json()["date_posted"] == "2021-05-23"


def test_retreive_job_by_id(client, normal_user_token_headers):
    data = {
        "title": "Python Developer",
        "company": "Boogle",
        "company_url": "https://www.boogle.com",
        "location": "Brazil, SP",
        "description": "Lorem Ipsum",
        "date_posted": "2021-05-23"
    }

    client.post("/job/create-job", json.dumps(data), headers=normal_user_token_headers)
    response = client.get("/job/get/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Python Developer"