pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Create a virtual environment
                sh 'python3 -m venv venv'
                
                // Activate the virtual environment and install dependencies
                sh '''
                #!/bin/bash
                source venv/bin/activate
                pip install -r requirements.txt
                '''
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
