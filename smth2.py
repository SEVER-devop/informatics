import requests

layers = [
    "sha256:1f7ce2fa46ab3942feabee654933948821303a5a821789dddab2d8c3df59e227",
    "sha256:58051c654d85097b5c13fd6388fc407ca26517e6c94ac2a11a439a9a2940c68d"
]

token = "ваш_токен_авторизации"  # Bearer token из API
registry = "https://registry-1.docker.io/v2"
repo = "dshtrigel/top_secret"

for layer in layers:
    url = f"{registry}/{repo}/blobs/{layer}"
    response = requests.get(
        url,
        headers={"Authorization": f"Bearer {token}"},
        stream=True
    )
    with open(f"{layer.replace('sha256:', '')}.tar.gz", "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    print(f"Downloaded: {layer}")