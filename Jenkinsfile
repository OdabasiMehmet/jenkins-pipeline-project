pipeline {
    agent any
    stages {
        stage('run') {
            steps {
                echo 'Modified text'
                sh 'python --version'
                sh 'python pipeline.py'
            }
        }
    }
}