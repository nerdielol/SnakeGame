pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Install pipx if not already installed
                sh 'apt-get install -y pipx'
                
                // Create a virtual environment and install dependencies using pipx
                sh '''
                #!/bin/bash
                python3 -m venv venv
                source venv/bin/activate
                pipx install -r requirements.txt
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
