pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'python3 -m venv venv'
                sh '''
                #!/bin/bash
                set -eux
                . venv/bin/activate && echo "Virtual environment activated"
                pip install -r requirements.txt
                python -m build
                pip install dist/snake*.whl
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh '''
                #!/bin/bash
                . venv/bin/activate && echo "Virtual environment activated"
                python -m pytest tests/
                '''
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
