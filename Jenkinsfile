pipeline {
    agent any
    
    echo 'getting enviroment vars'
    environment  {
        // aws
        ACCOUNT_ID = credentials('aws-account-id')
        ECR_URL    = "${ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com"
        REPO_NAME  = "blogpost_backend"
        S3_TFSTATE_BACKEND = "170770106047-terraform-tfstate"

        // docker
        NETWORK_NAME       =  "blogpost_web"
        TESTING_IMAGE_NAME = "sele_test"
    }

    stages {
        stage('Build') {
            steps {
                dir("webapp"){
                    
                    echo 'getting env dev file'
                    withCredentials([file(credentialsId: 'env_dev', variable: 'env_dev')]) 
                        {
                            sh 'cat $env_dev > .env.dev'
                        }
                    // create main network
                    sh 'docker network create -d bridge ${NETWORK_NAME} || echo Network Exist'
                    // build server image
                    sh 'docker-compose build'
                }
                // build testing image
                sh 'docker build -t ${TESTING_IMAGE_NAME} -f testing/Dockerfile testing'
            }
        }
        stage('Run server') {
            steps {
                dir("webapp"){

                    // run server container
                    sh 'docker-compose up -d; sleep 2'
                }
            }
        }
        stage('Browser_Test') {
            steps {
                // build nd run chrome container
                sh 'docker-compose -f testing/docker-compose.yml up -d; sleep 2'
                // run browser tests
                sh 'docker run --rm --name=testing --network=${NETWORK_NAME} ${TESTING_IMAGE_NAME} python main.py'
            }
        }

        stage('Stop Test') {
            steps {
                // remove webserver
                sh 'docker-compose -f webapp/docker-compose.yml kill'
                // remove browser
                sh 'docker-compose -f testing/docker-compose.yml kill'
            }
        }
        
        stage('Push to AWS ECR') {
            steps {
                withCredentials([file(credentialsId: 'aws_credentials', variable: 'aws_credentials')]) 
                    {
                        sh 'mkdir $HOME/.aws || echo Folder Exists'
                        sh 'cat $aws_credentials > $HOME/.aws/credentials'
                    }
                // check login
                sh 'aws ecr get-login-password | docker login --username AWS --password-stdin ${ECR_URL}'
                
                // create repo
                sh 'aws ecr create-repository --repository-name="${REPO_NAME}" || echo Repo ${REPO_NAME} Exist '

                // tag image
                sh 'docker tag ${REPO_NAME}:latest ${ECR_URL}/${REPO_NAME}:${GIT_COMMIT}'
                
                // push image
                sh 'docker push ${ECR_URL}/${REPO_NAME}:${GIT_COMMIT}'
            }
        }

        stage('Deploy to AWS') {
            steps  {
                dir("deploy/.before_tf"){
                    sh 'python3 main.py'
                }
                dir("deploy/terraform"){
                    withCredentials([file(credentialsId: 'tfvars', variable: 'tfvars')]) 
                    {
                        sh 'cat $tfvars > terraform.tfvars'
                    }
                    
                    sh 'terraform init && terraform validate'
                    sh 'terraform plan -var="REPO_NAME=${REPO_NAME}" -var="GIT_COMMIT=${GIT_COMMIT}"'
                    sh 'terraform apply -var="REPO_NAME=${REPO_NAME}" -var="GIT_COMMIT=${GIT_COMMIT}" -auto-approve'
                }
            }
        }

        stage('Cleanup'){
            steps {
                // remove webserver
                sh 'docker-compose -f webapp/docker-compose.yml down -v'
                // remove browser
                sh 'docker-compose -f testing/docker-compose.yml down -v'
                // Removing aws credentials
                sh 'rm -rf $HOME/.aws'
                // Removing dangling-container-images
                sh 'docker rmi $(docker images --filter dangling=true -q) || echo No dangling images'
                // remove tfvars
               dir("deploy/terraform"){
                   sh 'rm terraform.tfvars'
               }
            }
        }
    }
}