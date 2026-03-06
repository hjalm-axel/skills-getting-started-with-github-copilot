def test_user_can_signup_for_activity_successfully(client):
    """Test that a user can successfully sign up for an available activity."""
    response = client.post("/activities/Chess Club/signup?email=test@example.com")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "signed up" in data["message"].lower()


def test_signup_increases_participant_count(client):
    """Test that signing up for an activity increases the participant count."""
    # Get initial count
    response = client.get("/activities")
    initial_activities = response.json()
    initial_count = len(initial_activities["Chess Club"]["participants"])

    # Sign up
    client.post("/activities/Chess Club/signup?email=newuser@example.com")

    # Check count increased
    response = client.get("/activities")
    updated_activities = response.json()
    updated_count = len(updated_activities["Chess Club"]["participants"])
    assert updated_count == initial_count + 1


def test_duplicate_email_signup_returns_error(client):
    """Test that attempting to sign up with the same email twice returns an error."""
    # First signup
    client.post("/activities/Chess Club/signup?email=duplicate@example.com")

    # Second signup with same email
    response = client.post("/activities/Chess Club/signup?email=duplicate@example.com")
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert "already signed up" in data["detail"].lower()


def test_signup_for_nonexistent_activity_returns_not_found(client):
    """Test that signing up for a nonexistent activity returns a 404 error."""
    response = client.post("/activities/Nonexistent Activity/signup?email=test@example.com")
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "not found" in data["detail"].lower()