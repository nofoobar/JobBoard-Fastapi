import json


def test_create_user(client):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20"
        }
    response = client.post("/jobs/create-job/",json.dumps(data))
    assert response.status_code == 200 
    assert response.json()["company"] == "doogle"
    assert response.json()["description"] == "python"