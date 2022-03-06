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

        stage('Finalize') {
            steps {
                sh '''docker-compose down
                docker login -u twotrickspony -p 785694123
                # pipeline name was flask-test-wog
                docker tag flask-test-wog_web twotrickspony/wog-web-test:latest
                docker image push twotrickspony/wog-web-test:latest
                docker logout'''
            }
        }
    }
}
