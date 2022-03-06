properties([githubProjectProperty(displayName: '', projectUrlStr: 'https://github.com/NoyPhilosof/World_Of_Games.git/')])

pipeline {
    agent any

    stages {
        
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'http://github.com/NoyPhilosof/World_Of_Games.git'
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }
        
        stage('Run') {
            steps {
                sh '/usr/local/bin/docker-compose up -d'
            }
        }

        stage('Test') {
            steps {
                catchError(message: 'Failed e2e Test') {
                    script {
                        try{
                            sh '''pip install -r ./requirements.txt
                            cd utils/
                            python3 e2e.py'''
                        }                
                        catch (e) {
                            echo "Failed e2e Test"
                        }
                    }                
                }
            }
        }

        stage('Terminating Container') {
            steps {
                sh '''docker-compose down
                docker login -u clearnoyz -p degba4-fazfoG-wyssij
                docker tag flask-app clearnoyz/wog-web-test:latest
                docker image push clearnoyz/wog-web-test:latest'''
            }
        }
    }
}
