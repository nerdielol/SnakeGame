pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt'
                sh 'python -m build'
                sh 'pip install dist/snake*.whl'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'python -m pytest tests/'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Add deployment steps here
            }
        }
    }
}
