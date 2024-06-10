pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'python3 -m venv venv'
                sh '#!/bin/bash'
                sh 'set -eux'
                sh '. venv/bin/activate && echo "Virtual environment activated"'
                // sh 'which python'
                // sh 'which pip'
                // sh 'pip install -r requirements.txt'
                // sh 'python -m build'
                // sh 'pip install dist/snake*.whl'
            }
        }
        // stage('Test') {
        //     steps {
        //         echo 'Testing...'
        //         sh 'python -m pytest tests/'
        //     }
        // }
        // stage('Deploy') {
        //     steps {
        //         echo 'Deploying...'
        //         // Add deployment steps here
            }
        }
    }
}
