pipeline {
    agent any

    stages {
        stage('Przygotowanie środowiska') {
            steps {
                // Tworzenie wirtualnego środowiska (venv)
                sh 'python3 -m venv venv'

                // Aktualizacja pip wewnątrz venv
                sh '. venv/bin/activate && pip install --upgrade pip'
            }
        }

        stage('Instalacja zależności') {
            steps {
                script {
                    // Sprawdzamy czy istnieje requirements.txt, jeśli nie - instalujemy tylko pytest
                    if (fileExists('requirements.txt')) {
                        sh '. venv/bin/activate && pip install -r requirements.txt'
                    } else {
                        sh '. venv/bin/activate && pip install pytest'
                    }
                }
            }
        }

        stage('Testy (Pytest)') {
            steps {
                // Uruchomienie konkretnego pliku testowego logc_test.py
                // Flaga --junitxml generuje raport dla Jenkinsa
                sh '. venv/bin/activate && pytest logic_test.py --junitxml=test-results.xml'
            }
        }
    }

    post {
        always {
            // Publikacja wyników testów (wymaga wtyczki JUnit w Jenkinsie)
            junit 'test-results.xml'
        }
        cleanup {
            // Sprzątanie po testach
            sh 'rm -rf venv'
        }
    }
}
