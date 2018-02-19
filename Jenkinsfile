pipeline {
    agent {
        docker { image 'mxnet/python' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
            }
        }
        stage('Build') {
            steps {
                sh 'printenv'
            }
        }
    }
}