import requests
import base64
import json

# Docker Hub credentials (if private repo)
username = "your_username"
password = "your_password"
  

auth_token = base64.b64encode(f"{username}:{password}".encode()).decode()
headers = {
    "Authorization": f"Basic {auth_token}",
    "Accept": "application/vnd.docker.distribution.manifest.v2+json"
}

# Fetch the image manifest
registry_url = "https://registry-1.docker.io/v2"
repo = "dshtrigel/top_secret"
tag = "42"

# Step 1: Get auth token (for Docker Hub)
auth_response = requests.get(
    f"https://auth.docker.io/token?service=registry.docker.io&scope=repository:{repo}:pull"
)
token = auth_response.json().get("token")
headers = {"Authorization": f"Bearer {token}"}

# Step 2: Get the manifest
manifest_url = f"{registry_url}/{repo}/manifests/{tag}"
response = requests.get(manifest_url, headers=headers)
manifest = response.json()

print("Layers to download:")
for layer in manifest.get("layers", []):
    print(layer["digest"])