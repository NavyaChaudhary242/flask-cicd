pipeline {
    agent any
    stages {
        stage('Checkout') { steps { git branch: 'main', url: 'https://github.com/NavyaChaudhary242/flask-cicd.git' } }
        stage('Test') { steps { sh 'python3 -m venv venv && . venv/bin/activate && pip install -q -r requirements.txt && pytest -v' } }
        stage('Docker Build') { steps { sh 'docker build -t flask-cicd:${BUILD_NUMBER} -t flask-cicd:latest .' } }
        stage('Deploy') {
            steps {
                sh 'docker rm -f flaskapp || true'
                sh 'docker run -d --name flaskapp -p 5000:5000 flask-cicd:latest'
            }
        }
    }
}