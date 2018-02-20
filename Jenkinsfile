pipeline {
    agent {
        docker { image 'mxnet/python' }
    }
    environment {
        AWS_ACCESS_KEY_ID     = credentials('jenkins-aws-secret-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('jenkins-aws-secret-access-key')
    }
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
            }
        }
        stage('Build') {
            steps {
                sh 'echo $AWS_ACCESS_KEY_ID'
                sh 'echo $AWS_SECRET_ACCESS_KEY'
            }
        }
    }
}