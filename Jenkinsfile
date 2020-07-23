pipeline {
    options {
        // set a timeout of 60 minutes for this pipeline
        timeout(time: 60, unit: 'MINUTES')
    }
    agent {
      node {
        label 'jenkins-slave-python'
      }
    }

    environment {
        DEV_PROJECT = "project-dev"
        PROD_PROJECT = "project-prod"
        APP_GIT_URL = "https://github.com/richardwalkerdev/deckofcards.git"
        APP_NAME = "deckofcards"
        BUILD_CFG = "project-pipeline"
    }

    stages {

        stage('Install packages') {
            steps {
                echo '### SQLite Version'
                sh '''
                          sqlite3 --version
                          cat /etc/redhat-release
                   '''
                echo '### Installing Python packages ###'
                sh '''
                          pip install -r requirements.txt
                   '''
            }
        }

//         stage('Run Unit Tests') {
//             steps {
//                 echo '### Running unit tests ###'
//                 sh '''
//                           python manage.py test
//                    '''
//             }
//         }
//
//         stage('Run Lint') {
//             steps {
//                 echo '### Running unit tests ###'
//                 sh '''
//                           pylint --load-plugins pylint_django main/
//                           pylint --load-plugins pylint_django deckofcards/
//                    '''
//             }
//         }

        stage('Start new app in DEV env') {
            steps {
                echo '### Cleaning existing resources in DEV env ###'
                sh '''
                        oc new-build . --docker-image=quay.io/richardwalkerdev/cards --name=${APP_NAME} -n ${DEV_PROJECT}
                        sleep 180
                   '''
                echo '### Creating a new app in DEV env ###'
                   script {
                       openshift.withCluster() {
                           openshift.withProject(env.DEV_PROJECT) {
                               openshift.newApp("${APP_NAME}:latest", "--name=${APP_NAME}").narrow('svc').expose()
                           }
                       }
                   }
            }
        }
    }
}


//                         oc delete is ${APP_NAME} -n ${DEV_PROJECT}
//                         oc delete bc ${APP_NAME} -n ${DEV_PROJECT}
//                         sleep 5