import json

def test_create_job(client):
    data = {
        "title": "Python Developer",
        "company": "Boogle",
        # "company_url": "https://www.boogle.com",
        "location": "Brazil, SP",
        "description": "Lorem Ipsum",
        "date_posted": "2021-05-23"
    }

    response = client.post("/job/create-job", json.dumps(data))
    assert response.status_code == 200
    # assert response.json()["company_url"] == "https://www.boogle.com"
    # assert response.json()["description"] == "Lorem Ipsum"
    # assert response.json()["date_posted"] == "2021-05-23"