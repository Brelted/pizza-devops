pipeline {
    agent any
    environment {
        IMAGE = "brelos/pizza-devops"
    }
    stages {
        stage('Test') {
            steps { sh 'python3 -m py_compile app.py' }
        }
        stage('Build') {
            steps { sh 'docker build -t $IMAGE:$BUILD_NUMBER .' }
        }
        stage('Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub',
                        usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh 'docker push $IMAGE:$BUILD_NUMBER'
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'kubectl set image deployment/pizza-devops web=$IMAGE:$BUILD_NUMBER'
            }
        }
    }
}