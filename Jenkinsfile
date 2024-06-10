pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building2...'
                sh 'pip install -r requirements.txt'
                sh 'python -m build'
                sh 'pip install dist/snake*.whl'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing2...'
                sh 'python -m pytest tests/'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying2...'
                // Add deployment steps here
            }
        }
    }
}
