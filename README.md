# Link Spider

Link Spider is a Python-based web scraping tool that extracts all links from a given set of URLs. The project is containerized using Docker and can be deployed to a Kubernetes cluster. The CI/CD pipeline is managed using Travis CI, ensuring automated builds and deployments.

## Features

- Extracts links from multiple URLs.
- Outputs links either as absolute URLs or as JSON with the base domain as the key and relative paths as values.
- Containerized using Docker.
- CI/CD pipeline using Travis CI.
- Deployable to Kubernetes.

## Requirements

- Python 3.8
- Docker
- Kubernetes
- Travis CI account
- Docker Hub account

## Usage

### Running Locally

1. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt

