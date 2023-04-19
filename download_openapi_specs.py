import requests
import yaml

URLS_AND_PATHS = [
    (
        "https://docs.pinecone.io/reference/upsert?json=on",
        "vector_openapi.yml",
    ),
    (
        "https://docs.pinecone.io/reference/list_collections?json=on",
        "index_openapi.yml",
    ),
]


def download_openapi_spec(url: str):
    sess = requests.Session()
    response = sess.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        raise Exception(f"Failed to download OpenAPI specs from {url}")
    return data["oasDefinition"]


def write_openapi_spec(spec: dict, path: str):
    with open(path, "w") as f:
        f.write(yaml.dump(spec))


if __name__ == "__main__":
    for url, path in URLS_AND_PATHS:
        spec = download_openapi_spec(url)
        write_openapi_spec(spec, path)
