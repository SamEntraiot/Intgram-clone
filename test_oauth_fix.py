import requests
import json

# Test the new JWT token generation endpoint
# First, let's test if we can access the profile endpoint (which should work with session auth)
try:
    response = requests.get('http://127.0.0.1:8000/api/profile/me/', allow_redirects=False)
    print(f'Profile endpoint status: {response.status_code}')

    if response.status_code == 200:
        print('✅ Session authentication working')

        # Now test the new JWT token endpoint
        token_response = requests.post('http://127.0.0.1:8000/api/auth/get-jwt-token/', allow_redirects=False)
        print(f'JWT token endpoint status: {token_response.status_code}')

        if token_response.status_code == 200:
            tokens = token_response.json()
            print('✅ JWT token generation working!')
            print(f'Access token length: {len(tokens.get("access", ""))}')
            print(f'Refresh token length: {len(tokens.get("refresh", ""))}')

            # Test if the JWT token works for API calls
            headers = {'Authorization': f'Bearer {tokens["access"]}'}
            profile_test = requests.get('http://127.0.0.1:8000/api/profile/me/', headers=headers)
            print(f'JWT-authenticated profile request: {profile_test.status_code}')

            if profile_test.status_code == 200:
                print('✅ JWT token authentication working!')
            else:
                print(f'❌ JWT token authentication failed: {profile_test.text}')
        else:
            print(f'❌ JWT token generation failed: {token_response.text}')
    else:
        print(f'❌ Session authentication not working: {response.status_code}')

except Exception as e:
    print(f'❌ Error during testing: {e}')
