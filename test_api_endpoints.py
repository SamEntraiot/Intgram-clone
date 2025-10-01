"""
Test script to verify API endpoints are working correctly
Run this after starting the Django server
"""

import requests
import json

# Configuration
BASE_URL = "http://localhost:8000/api"
TEST_USERNAME = "testuser"  # Change this to your test user
TEST_PASSWORD = "testpass123"  # Change this to your test password

def test_login():
    """Test login and get access token"""
    print("=" * 50)
    print("Testing Login...")
    try:
        response = requests.post(f"{BASE_URL}/login/", json={
            "username": TEST_USERNAME,
            "password": TEST_PASSWORD
        })
        if response.status_code == 200:
            data = response.json()
            print("✅ Login successful!")
            return data.get('access')
        else:
            print(f"❌ Login failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def test_suggestions(token):
    """Test suggestions endpoint"""
    print("\n" + "=" * 50)
    print("Testing Suggestions...")
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{BASE_URL}/suggestions/", headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Suggestions loaded successfully!")
            print(f"   Found {len(data)} suggestions")
            if data:
                print(f"   First suggestion: {data[0].get('username')}")
        else:
            print(f"❌ Failed to load suggestions: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_stories(token):
    """Test stories endpoint"""
    print("\n" + "=" * 50)
    print("Testing Stories...")
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{BASE_URL}/stories/", headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Stories loaded successfully!")
            print(f"   Found {len(data)} stories")
            if data:
                story = data[0]
                print(f"   First story by: {story.get('username')}")
                print(f"   Avatar: {story.get('user_avatar')}")
        else:
            print(f"❌ Failed to load stories: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_feed(token):
    """Test feed endpoint"""
    print("\n" + "=" * 50)
    print("Testing Feed...")
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{BASE_URL}/feed/", headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            results = data.get('results', [])
            print(f"✅ Feed loaded successfully!")
            print(f"   Found {len(results)} posts")
            if results:
                post = results[0]
                print(f"   First post by: {post.get('author_username')}")
        else:
            print(f"❌ Failed to load feed: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_explore(token):
    """Test explore endpoint"""
    print("\n" + "=" * 50)
    print("Testing Explore...")
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{BASE_URL}/explore/", headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Explore loaded successfully!")
            print(f"   Found {len(data)} posts")
        else:
            print(f"❌ Failed to load explore: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Run all tests"""
    print("\n🧪 API ENDPOINT TESTING")
    print("=" * 50)
    print(f"Base URL: {BASE_URL}")
    print(f"Username: {TEST_USERNAME}")
    print()
    
    # Get access token
    token = test_login()
    
    if token:
        # Test all endpoints
        test_suggestions(token)
        test_stories(token)
        test_feed(token)
        test_explore(token)
        
        print("\n" + "=" * 50)
        print("✅ All tests completed!")
        print("=" * 50)
    else:
        print("\n❌ Cannot proceed without valid token")
        print("\nPlease make sure:")
        print("1. Django server is running (python manage.py runserver)")
        print("2. Test user exists with correct credentials")
        print("3. Update TEST_USERNAME and TEST_PASSWORD in this script")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
