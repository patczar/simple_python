pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
            // label 'main'
            // Opcjonalnie: mapowanie użytkownika, aby uniknąć problemów z uprawnieniami
            args '-u root:root'
        }
    }

    stages {
        stage('Instalacja zależności') {
            steps {
                sh 'pip install pytest'
                // Jeśli masz requirements.txt, odkomentuj linię poniżej:
                // sh 'pip install -r requirements.txt'
            }
        }

        stage('Testy') {
            steps {
                // Uruchomienie testów z pliku logc_test.py
                sh 'pytest logic_test.py --junitxml=test-results.xml'
            }
        }
    }

    post {
        always {
            junit 'test-results.xml'
        }
    }
}
