pipeline {
    
    environment {
        //AWS_ACCOUNT_ID="458277318855"
       // AWS_DEFAULT_REGION="us-east-2" 
        IMAGE_REPO_NAME="dvwa"
        IMAGE_TAG="latest"
        target_url="http://3.138.69.19:80"
        Nmap="3.138.69.19"
        //REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
        //def BUILD_NUMBER = "$currentBuild.number"
    }
      
    agent none
   
    stages {
        stage('Checkout using SOURCE_BRANCH') {
            agent { label 'jenkinsbuild' }
            
            
            steps { 
             
             git branch: 'master', url: 'https://Mukeshit91@bitbucket.org/Mukeshit91/docker-vulnerable-dvwa.git'
   }
        }
        
          stage ('Check-Git-Secrets') {
              agent { label 'jenkinsbuild' }
        
        steps {
             //sh '/bin/spdx-sbom-generator -h'
             
           
            sh 'rm gitsecret_report.json || true'
            //sh "chmod +x -R ${env.WORKSPACE}"
            sh 'ls -la'
            //sh 'sudo chown -R jenkins:jenkins /var/lib/jenkins/workspace/Devsecops'
            
            //sh 'chmod +x /home/ubuntu/detect-secrets/.secrets.baseline'
        
            sh '/usr/local/bin/detect-secrets  scan > gitsecret_report.json'

            sh 'cat gitsecret_report.json'
            
            sh '''
             time=$(date +'%Y-%m-%d')        
		sudo curl --location --request POST 'http://18.220.19.210:8080/api/v2/import-scan/' \
--header 'Authorization: Token a1c2e4b944e0ba004336bccc9ec5dd2fcfdba1b2' \
--form 'engagement="1"' \
--form 'verified="true"' \
--form 'active="true"' \
--form 'lead="1"' \
--form tags=$BUILD_NUMBER \
--form scan_date=$date \
--form 'scan_type="Detect-secrets Scan"' \
--form 'minimum_severity="Info"' \
--form 'skip_duplicates="true"' \
--form 'close_old_findings="false"' \
--form 'file=@"gitsecret_report.json"'

'''
            
        }
        }
        
        stage ('Source-Composition-Analysis') {
            agent { label 'jenkinsbuild' }
         
        steps {
            sh 'sudo rm var/lib/jenkins/workspace/Devsecops/odc-reports/dependency-check-report.xml|| true'
            //sh 'rm owasp-* || true'
            sh 'ls -lrth'
            sh 'sudo chown -R jenkins:jenkins ${WORKSPACE}/odc-reports || true'
           //sh 'sudo chown -R jenkins:jenkins /var/lib/jenkins/workspace/Devsecops'
           
            sh 'chmod +x owasp-dependency-check.sh'
            sh './owasp-dependency-check.sh'
            sh 'cat /var/lib/jenkins/workspace/Devsecops/odc-reports/dependency-check-report.xml'
            sh '''
             time=$(date +'%Y-%m-%d')        
		sudo curl --location --request POST 'http://18.220.19.210:8080/api/v2/import-scan/' \
--header 'Authorization: Token a1c2e4b944e0ba004336bccc9ec5dd2fcfdba1b2' \
--form 'engagement="1"' \
--form 'verified="true"' \
--form 'active="true"' \
--form 'lead="1"' \
--form tags=$BUILD_NUMBER \
--form scan_date=$date \
--form 'scan_type="Dependency Check Scan"' \
--form 'minimum_severity="Info"' \
--form 'skip_duplicates="true"' \
--form 'close_old_findings="false"' \
--form 'file=@"/var/lib/jenkins/workspace/Devsecops/odc-reports/dependency-check-report.xml"'

'''
    }
}

 

stage('SonarQube Analysis')
{
     agent { label 'build' }
 
steps{
    git branch: 'master', url: 'https://Mukeshit91@bitbucket.org/Mukeshit91/docker-vulnerable-dvwa.git'
    withSonarQubeEnv('SonarQube') {
    sh '''
  
  
   /opt/sonar-scanner/bin/sonar-scanner \
  -Dsonar.projectKey=Sonar-report \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://18.118.146.40:9000 \
  -Dsonar.login=862c13eba4d28b45a6170b0a3d286330df0957a2
 
    
    '''
    }
  
 

}
}  

stage('scaning Dockerfile') {
    agent { label 'jenkinsbuild'}
          
      steps{
          sh '/usr/local/bin/trivy conf -f json -o trivy1.json ${WORKSPACE}/Dockerfile'
          sh 'cat trivy1.json'
          
            sh '''
             time=$(date +'%Y-%m-%d')        
		sudo curl --location --request POST 'http://18.220.19.210:8080/api/v2/import-scan/' \
--header 'Authorization: Token a1c2e4b944e0ba004336bccc9ec5dd2fcfdba1b2' \
--form 'engagement="1"' \
--form 'verified="true"' \
--form 'active="true"' \
--form 'lead="1"' \
--form tags=$BUILD_NUMBER \
--form scan_date=$date \
--form 'scan_type="Trivy Scan"' \
--form 'minimum_severity="Info"' \
--form 'skip_duplicates="true"' \
--form 'close_old_findings="false"' \
--form 'file=@"trivy1.json"'

'''
      }
 }
 

stage('Building image') {
    agent { label 'jenkinsbuild' }
      steps{
          
        // dir("/var/lib/jenkins/workspace/Devsecops") {
        script {
            //sh 'chmod -R 777 ./'
            sh 'sudo chown -R jenkins:jenkins /var/lib/jenkins/workspace/Devsecops'
            
          dockerImage = docker.build "${IMAGE_REPO_NAME}:${IMAGE_TAG}"
          //sh 'docker ps'
       //}
      }
    }
    }
    
    /* stage('Image scanning') {
      agent { label 'jenkinsbuild' }
   
      steps{
          
          
        
        sh 'rm dockle_report.json || true'
       sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock goodwithtech/dockle:v0.4.5 -f json ${IMAGE_REPO_NAME}:${IMAGE_TAG}| tee dockle_report1.json'
       sh "sed '1d' dockle_report1.json >dockle_report.json"
       sh 'cat dockle_report.json'
       sh '''
             time=$(date +'%Y-%m-%d')        
		sudo curl --location --request POST 'http://18.220.19.210:8080/api/v2/import-scan/' \
--header 'Authorization: Token a1c2e4b944e0ba004336bccc9ec5dd2fcfdba1b2' \
--form 'engagement="1"' \
--form 'verified="true"' \
--form 'active="true"' \
--form 'lead="1"' \
--form tags=$BUILD_NUMBER \
--form scan_date=$date \
--form 'scan_type="Dockle Scan"' \
--form 'minimum_severity="Info"' \
--form 'skip_duplicates="true"' \
--form 'close_old_findings="false"' \
--form 'file=@"dockle_report.json"'

'''
        }
}
*/

stage('trivy image scan') {
    agent { label 'jenkinsbuild'}
          
      steps{
  // sh 'SECURE_API_TOKEN=81056cbb-eb24-43ce-b592-2c1e6247010e ./sysdig-cli-scanner --apiurl https://us2.app.sysdig.com dvwa:latest'
    //sh '/usr/local/bin/trivy conf -f json -o trivy.json ${WORKSPACE}'
    sh '/usr/local/bin/trivy image -f json -o trivy.json dvwa:latest'
    sh 'cat trivy.json'
    
     sh '''
             time=$(date +'%Y-%m-%d')        
		sudo curl --location --request POST 'http://18.220.19.210:8080/api/v2/import-scan/' \
--header 'Authorization: Token a1c2e4b944e0ba004336bccc9ec5dd2fcfdba1b2' \
--form 'engagement="1"' \
--form 'verified="true"' \
--form 'active="true"' \
--form 'lead="1"' \
--form tags=$BUILD_NUMBER \
--form scan_date=$date \
--form 'scan_type="Trivy Scan"' \
--form 'minimum_severity="Info"' \
--form 'skip_duplicates="true"' \
--form 'close_old_findings="false"' \
--form 'file=@"trivy.json"'

'''
      }
 } 
 stage('Deployed on docker') {
     agent { label 'jenkinsbuild' }
      steps{
          
        script {
        sh 'docker ps'
       //sh 'docker run -d --name dvwa -p 80:80 dvwa:latest /bin/bash' 
       
        }
      }
 }
 
 stage ('DAST') {
		  agent { label 'jenkinsbuild' }
		    	steps {
			     script {
                     
               sh 'rm zap_report.xml || true'      
               sh 'chmod -R 777 ./'
               sh 'ls -lrth'
                     //sh 'docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable zap-baseline.py -t http://18.222.18.171:32607/ -g gen.conf -r zap_report.html || true'
           // sh 'docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable zap-full-scan.py -t http://18.191.140.189:80 -g gen.conf -x zap_report.xml || true'
            sh 'docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable zap-baseline.py -t $target_url -g gen.conf -x zap_report.xml || true'
            sh 'cat zap_report.xml'
            
            sh '''
             time=$(date +'%Y-%m-%d')        
		sudo curl --location --request POST 'http://18.220.19.210:8080/api/v2/import-scan/' \
--header 'Authorization: Token a1c2e4b944e0ba004336bccc9ec5dd2fcfdba1b2' \
--form 'engagement="1"' \
--form 'verified="true"' \
--form 'active="true"' \
--form 'lead="1"' \
--form tags=$BUILD_NUMBER \
--form scan_date=$date \
--form 'scan_type="ZAP Scan"' \
--form 'minimum_severity="Info"' \
--form 'skip_duplicates="true"' \
--form 'close_old_findings="false"' \
--form 'file=@"zap_report.xml"'

'''
            
			     }
		    	}
 }
 
 stage ('Nikto Scan') 
        {
           agent { label 'jenkinsbuild' }
		    steps {
			sh 'rm nikto-output.xml || true'
			sh 'docker pull secfigo/nikto:latest'
			sh 'sudo docker run --user $(id -u):$(id -g) --rm -v $(pwd):/report -i secfigo/nikto:latest -h $target_url -output /report/nikto-output.xml'
			sh 'cat nikto-output.xml || true'
			sh '''
             time=$(date +'%Y-%m-%d')        
		sudo curl --location --request POST 'http://18.220.19.210:8080/api/v2/import-scan/' \
--header 'Authorization: Token a1c2e4b944e0ba004336bccc9ec5dd2fcfdba1b2' \
--form 'engagement="1"' \
--form 'verified="true"' \
--form 'active="true"' \
--form 'lead="1"' \
--form tags=$BUILD_NUMBER \
--form scan_date=$date \
--form 'scan_type="Nikto Scan"' \
--form 'minimum_severity="Info"' \
--form 'skip_duplicates="true"' \
--form 'close_old_findings="false"' \
--form 'file=@"nikto-output.xml"'

'''
			
			
			
		    }
        }
        
        stage ('Port Scan') {
        	          agent { label 'jenkinsbuild' }      

		    steps {
			sh 'rm nmap* || true'
			sh 'docker run --rm -v "$(pwd)":/data uzyexe/nmap -sS -sV -oX nmap $Nmap'
			sh 'cat nmap'
			
			sh '''
             time=$(date +'%Y-%m-%d')        
		sudo curl --location --request POST 'http://18.220.19.210:8080/api/v2/import-scan/' \
--header 'Authorization: Token a1c2e4b944e0ba004336bccc9ec5dd2fcfdba1b2' \
--form 'engagement="1"' \
--form 'verified="true"' \
--form 'active="true"' \
--form 'lead="1"' \
--form tags=$BUILD_NUMBER \
--form scan_date=$date \
--form 'scan_type="Nmap Scan"' \
--form 'minimum_severity="Info"' \
--form 'skip_duplicates="true"' \
--form 'close_old_findings="false"' \
--form 'file=@"nmap"'

'''
			
		    }
        }
    
}
}
