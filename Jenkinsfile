pipeline {
      environment {
        
        target_url="http://192.168.228.132:81"
        Nmap="192.168.228.132"
        
    }
    
    agent any
   
    stages {
        stage('Checkout using SOURCE_BRANCH') {
             
            steps {
            
            git branch: 'master', url: 'https://Mukeshit91@bitbucket.org/Mukeshit91/docker-vulnerable-dvwa.git'
            sh '''
            rm -rf sql_query
            scan_repo= echo "$(tail -n 1 bitbucket_repo)"
            git clone "$(tail -n 1 bitbucket_repo)"
            ls
           '''
   }
        }
        stage ('Check-Git-Secrets') {
        
        steps {
            //sh 'pip3 install detect-secrets'
           sh 'sudo rm gitsecret_report.json || true'
           //sh 'sudo chmod 777 /var/lib/jenkins/workspace/Devsecops'
            //sh "sudo chmod 777 -R ${env.WORKSPACE}"
            sh 'ls -la'
            //sh 'sudo chown -R $(id -u ${USER}):$(id -g ${USER}) ${WORKSPACE}'
           //sh 'sudo /home/ubuntu/.local/bin/detect-secrets  scan > gitsecret_report.json'
            //sh 'sudo /home/ubuntu/.local/bin/detect-secrets scan'
           // sh '/usr/local/bin/detect-secrets  scan > gitsecret_report.json'
            //sh 'git config --global --add safe.directory /var/lib/jenkins/workspace/Devsecops'
        //sh "detect-secrets -C /var/lib/jenkins/workspace/Devsecops scan >/var/lib/jenkins/workspace/Devsecops/gitsecret_report.json"
            //sh '/home/ubuntu/.local/bin/trufflehog --regex --entropy false https://Mukeshit91@bitbucket.org/Mukeshit91/docker-vulnerable-dvwa.git --json trufflehog.json'
            //sh '/usr/local/bin/detect-secrets scan > gitsecret_report.json'
             sh 'detect-secrets -C . scan >gitsecret_report.json'
             
            //sh 'sudo detect-secrets scan'
            //sh 'sudo docker run --rm -t gesellix/trufflehog --json https://bitbucket.org/Mukeshit91/docker-vulnerable-dvwa.git > trufflehog.json'
            //sh 'sudo docker run -v $(pwd):/src --rm hysnsec/trufflehog --repo_path /src file:///src --json trufflehog.json'
            sh 'cat gitsecret_report.json || true'
           /* sh '''
             time=$(date +'%Y-%m-%d')        
		sudo curl --location --request POST 'http://192.168.228.132:8080/api/v2/import-scan/' \
--header 'Authorization: Token 2e0eb13f2aed51caf04f270f2c9b32359f321998' \
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
*/
            
        }
        }
        
         stage ('Source-Composition-Analysis') {
            
         
        steps {
            //sh 'sudo rm var/lib/jenkins/workspace/Devsecops/odc-reports/dependency-check-report.xml|| true'
            //sh 'rm owasp-* || true'
            sh 'ls -lrth'
           // sh 'sudo chown -R jenkins:jenkins /var/lib/jenkins/workspace/Devsecops'
          // sh 'sudo chown -R ubuntu:ubuntu /var/lib/jenkins/workspace/Devsecops'
          // sh 'sudo chown -R $(id -u ${USER}):$(id -g ${USER}) ${WORKSPACE}'
          sh 'sudo chown -R $(id -u ${USER}):$(id -g ${USER}) ${WORKSPACE}/odc-reports || true'
           //sh 'wget https://raw.githubusercontent.com/devopssecure/webapp/master/owasp-dependency-check.sh'
            sh 'sudo chmod +x owasp-dependency-check.sh'
            sh 'sudo ./owasp-dependency-check.sh'
            sh 'cat ${WORKSPACE}/odc-reports/dependency-check-report.xml'
            
            sh '''
             time=$(date +'%Y-%m-%d')        
		sudo curl --location --request POST 'http://192.168.228.132:8080/api/v2/import-scan/' \
--header 'Authorization: Token 2e0eb13f2aed51caf04f270f2c9b32359f321998' \
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
--form 'file=@"odc-reports/dependency-check-report.xml"'

'''
        
    }
} 


stage('SonarQube Analysis')
           {

            steps{
             
    sh '''
    docker run \
      --rm \
      -v "$(pwd):/usr/src" \
      sonarsource/sonar-scanner-cli \
      -Dsonar.projectKey=sonar-report \
      -Dsonar.sources=. \
      -Dsonar.host.url=http://192.168.228.132:9000 \
      -Dsonar.login=sqp_8f1677ae900f243086c621b7b5f6a1048c83d567
    '''
    
            }
           }
           
   
  
  }
}

