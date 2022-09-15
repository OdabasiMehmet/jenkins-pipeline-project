pipeline {
    agent any
    stages {
        stage('run') {
            steps {
                echo 'Clarusway The  Way to Reinvent Yourself'
                sh 'python --version'
                sh 'python pipeline.py'
            }
        }
    }
}
