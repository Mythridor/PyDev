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
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                echo "${env.AWS_ACCESS_KEY_ID}"
                echo "${env.AWS_SECRET_ACCESS_KEY}"
            }
        }
    }
}