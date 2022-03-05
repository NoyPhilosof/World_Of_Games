properties([githubProjectProperty(displayName: '', projectUrlStr: 'https://github.com/NoyPhilosof/World_Of_Games.git/')])

pipeline {
    agent any

    stages {
        
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'http://github.com/NoyPhilosof/World_Of_Games.git'
            }
        }
        
        stage('Build Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }
        
        stage('Run Container') {
            steps {
                sh '/usr/local/bin/docker-compose up -d'
            }
        }
        
        stage('Selenium Test') {
            steps {
                sh '''pip install -r ./requirements.txt
                cd /utils
                python3 e2e.py'''
            }
        }
    }
}
