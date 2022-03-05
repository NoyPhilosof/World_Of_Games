pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/NoyPhilosof/World_Of_Games.git'
            }
        }
        stage('Build Image') {
            steps {
                sh '''cd /var/lib/jenkins/workspace/test-flask
                docker build -t flask-app .'''
            }
        }
        //stage('Build Image') {
            //steps {
                //script {
                    //sh 'docker-compose build'
                //}
                
            //}
        //}
    }
}
