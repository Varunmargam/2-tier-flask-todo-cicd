pipeline{
    agent any
    
    stages{
        stage("Clone"){
            steps{
               git url: 'https://github.com/Varunmargam/2-tier-flask-todo-cicd.git', branch: 'master' 
            }
        }
        stage("Build"){
            steps{
                sh "docker build . -t flask-todo-app-cicd"
            }
        }
        stage("Push to Repository"){
            steps{
                withCredentials([usernamePassword(credentialsId:"DockerHub",passwordVariable:"DockerHubPass",usernameVariable:"DockerHubUser")]){
                    sh "docker login -u ${env.DockerHubUser} -p ${env.DockerHubPass}"
                    sh "docker tag flask-todo-app-cicd ${env.DockerHubUser}/flask-todo-app-cicd:latest"
                    sh "docker push ${env.DockerHubUser}/flask-todo-app-cicd:latest"
                }
            }
        }
        stage("Deploy"){
            steps{
                sh "docker-compose down && docker-compose up -d"
            }
        }
        stage("Remove unused images"){
            steps{
                sh "docker image prune -af"
            }
        }
    }
}
