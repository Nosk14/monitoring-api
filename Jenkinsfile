node() {
    def image = null
    stage('Checkout') {
        checkout scm
    }

    stage('Build') {
        image = docker.build("monitoring-api:${env.BUILD_ID}")
    }

    stage('Deploy'){
        try{
            sh 'docker stop monitoring-api && docker rm monitoring-api'
        }catch(Exception e){
            echo e.getMessage()
        }

        def runArgs = '\
-v monitoring-data:$MA_DATABASE_PATH \
-e "DATABASE_PATH=$MA_DATABASE_PATH" \
-p 80:5000 \
--name monitoring-api'

        def container = image.run(runArgs)
    }
}
