pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    environment {
        IMAGE = "brelos/pizza-devops"
    }

    stages {
        stage('Test') {
            steps {
                sh '''
                    python3 -m py_compile app.py
                '''
            }
        }

        stage('Build image') {
            steps {
                sh '''
                    docker build -t "$IMAGE:$BUILD_NUMBER" -t "$IMAGE:latest" .
                '''
            }
        }

        stage('Push image') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub',
                        usernameVariable: 'USER',
                        passwordVariable: 'PASS'
                    )
                ]) {
                    sh '''
                        echo "$PASS" | docker login -u "$USER" --password-stdin
                        docker push "$IMAGE:$BUILD_NUMBER"
                        docker push "$IMAGE:latest"
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    export KUBECONFIG=/root/.kube/config
                    kubectl set image deployment/pizza-devops web="$IMAGE:$BUILD_NUMBER"
                    kubectl rollout status deployment/pizza-devops
                '''
            }
        }
    }

    post {
        always {
            sh 'docker logout || true'
        }
    }
}