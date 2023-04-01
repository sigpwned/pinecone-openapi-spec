# pinecone-openapi-spec

The excellent vector database [Pinecone](https://www.pinecone.io/) has [a very useful API](https://docs.pinecone.io/reference/describe_index_stats_post), but client support is sparse. While the API and its clients are in theory [based off of an OpenAPI spec](https://www.pinecone.io/learn/pinecone-v2/#rest-api-and-python-client), [no one seems to be able to find it](https://community.pinecone.io/t/openapi-spec-for-api-reference-is-not-found/827).

Therefore, I reverse engineered (read: copy and pasted from the documentation) [this OpenAPI spec](openapi.yml).

It is very new and so should be considered very experimental. If you use it and find a bug, please open an issue, or even better submit a pull request!

Bug fixes will be released as tags so that users can reference a specific version of the spec and have confidence it won't change. Release tags will use the format `YYYYMMDD.N`.
