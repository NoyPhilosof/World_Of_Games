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
                sh '/usr/local/bin/docker build -t flask-app .'
            }
        }
        
        stage('Run') {
            steps {
                sh '/usr/local/bin/docker-compose-v1 up -d'
            }
        }

        stage('Test') {
            steps {
                catchError(message: 'Failed e2e Test') {
                    script {
                        try{
                            sh '''pip3 install -r ./requirements.txt
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
                sh '''/usr/local/bin/docker-compose-v1 down
                /usr/local/bin/docker login -u twotrickspony -p 785694123
                # pipeline name was flask-test-wog
                /usr/local/bin/docker tag world_of_games_web twotrickspony/wog-web-test:latest
                /usr/local/bin/docker image push twotrickspony/wog-web-test:latest
                /usr/local/bin/docker logout'''
            }
        }
    }
}
