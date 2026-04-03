pipeline {
    agent any

    stages {
        stage('Build Docker') {
            steps {
                sh 'docker build -t aceest-app .'
            }
        }

        stage('Deploy K8s') {
            steps {
                sh 'k3s kubectl apply -f k3s/manifests/deployment.yaml'
                sh 'k3s kubectl apply -f k3s/manifests/service.yaml'
            }
        }
    }
}
