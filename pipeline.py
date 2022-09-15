pipeline {
    agent any
    stages {
        stage('run') {
            steps {
                echo 'Clarusway Way to Reinvent Yourself'
                sh 'python --version'
                sh 'python pipeline.py'
            }
        }
    }
}
