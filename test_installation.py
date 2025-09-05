#!/usr/bin/env python3
"""
AI-Alpha Installation Test Script
Tests that the AI-Alpha application is working correctly.
"""

import requests
import time
import sys
import json
from urllib.parse import urljoin


def test_endpoint(base_url, endpoint, expected_keys=None):
    """Test a single API endpoint."""
    url = urljoin(base_url, endpoint)
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        print(f"✅ {endpoint}: {response.status_code}")
        
        if expected_keys:
            for key in expected_keys:
                if key not in data:
                    print(f"⚠️  Missing expected key '{key}' in response")
                    return False
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ {endpoint}: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ {endpoint}: Invalid JSON response - {e}")
        return False


def main():
    """Main test function."""
    print("🧪 AI-Alpha Installation Test")
    print("=============================")
    
    base_url = "http://localhost:8000"
    
    # Wait for server to start
    print("⏳ Waiting for server to start...")
    for i in range(30):  # Wait up to 30 seconds
        try:
            response = requests.get(base_url, timeout=1)
            if response.status_code == 200:
                break
        except requests.exceptions.RequestException:
            pass
        time.sleep(1)
        if i % 5 == 4:
            print(f"   Still waiting... ({i+1}s)")
    else:
        print("❌ Server did not start within 30 seconds")
        print("💡 Make sure the AI-Alpha application is running on port 8000")
        sys.exit(1)
    
    print("🚀 Server is running, starting tests...")
    print("")
    
    # Test endpoints
    tests = [
        ("/", ["message", "version", "status"]),
        ("/health", ["status"]),
        ("/api/v1/agent", ["agent_name", "agent_type", "capabilities"]),
    ]
    
    passed = 0
    total = len(tests)
    
    for endpoint, expected_keys in tests:
        if test_endpoint(base_url, endpoint, expected_keys):
            passed += 1
    
    print("")
    print("📊 Test Results")
    print("===============")
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed! AI-Alpha is working correctly.")
        print("")
        print("🌐 You can now access:")
        print(f"   • Main API: {base_url}")
        print(f"   • Health Check: {base_url}/health")
        print(f"   • Agent Info: {base_url}/api/v1/agent")
        print(f"   • API Docs: {base_url}/docs")
        sys.exit(0)
    else:
        print("💥 Some tests failed. Please check the application.")
        sys.exit(1)


if __name__ == "__main__":
    main()