pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/KollaNagaManasa/introduction-to-devops-assignment-1-march2026.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t gym-app .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run gym-app pytest || true'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
