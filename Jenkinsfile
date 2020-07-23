pipeline {
    options {
        // set a timeout of 60 minutes for this pipeline
        timeout(time: 60, unit: 'MINUTES')
    }
    agent {
      docker {
        image 'python:3.7.2'
       }
    }

    environment {
        DEV_PROJECT = "project-dev"
        PROD_PROJECT = "project-prod"
        APP_GIT_URL = "https://github.com/richardwalkerdev/deckofcards.git"
        APP_NAME = "deckofcards"
    }

    stages {

        stage('Install packages') {
            steps {
                echo '### Installing Python packages ###'
                sh '''
                          pip install -r requirements.txt
                   '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo '### Running unit tests ###'
                sh '''
                          python manage.py test
                   '''
            }
        }
    }
}