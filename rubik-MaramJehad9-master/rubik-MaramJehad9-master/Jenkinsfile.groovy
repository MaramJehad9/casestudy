pipeline {
    agent any
    stages {
        stage('Pull Docker Image') {
            steps {
                // Pull the Docker image
                sh 'docker pull python:3.10'
            }
        }
        stage('Scan for Vulnerabilities') {
            steps {
                // Run the Python script to scan Docker image
                script {
                    def result = sh(script: "python scan_docker_image.py", returnStdout: true).trim()
                    echo "Scan Result: ${result}"
                }
            }
        }
        stage('Deploy if Secure') {
            when {
                expression { result == 'Secure' }
            }
            steps {
                echo "Image is secure. Proceeding with deployment..."
                // Proceed with deployment
            }
        }
        stage('Halt if Insecure') {
            when {
                expression { result == 'Insecure' }
            }
            steps {
                error "Image is insecure. Halting the pipeline."
            }
        }
    }
}
