pipeline {
    agent { dockerfile true }

    node {
        checkout scm

        stage('Build'){
            steps{
                 def customImage = docker.build("monitoring-api:${env.BUILD_ID}")
            }
        }

        stage('Test'){

        }

        stage('Deploy'){

        }
    }
}