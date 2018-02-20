pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
            }
        }
        stage('Build') {
            steps {
                sh 'python __init__.py'
                echo "${env.AWS_ACCESS_KEY_ID}"
                echo "${env.AWS_SECRET_ACCESS_KEY}"
            }
        }
    }
}