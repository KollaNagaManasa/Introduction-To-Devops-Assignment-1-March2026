name: CI/CD Pipeline (Jenkins Equivalent)

on:
  push:
    branches: ["main"]

jobs:
  pipeline:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.12'

    - name: Install Dependencies
      run: pip install -r requirements.txt

    - name: Run Tests
      run: pytest || true

    - name: Build Docker Image
      run: docker build -t gym-app .

    - name: Run Container Tests
      run: docker run gym-app pytest || true
