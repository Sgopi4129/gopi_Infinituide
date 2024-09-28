pipeline {
    agent any

    environment {
        // Environment variables for AWS credentials
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')  // Jenkins credentials ID for AWS access key
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key') // Jenkins credentials ID for AWS secret key
    }

    stages {
        stage('Checkout Source Code') {
            steps {
                // Checkout the source code from GitHub
                git url: 'https://github.com/yourusername/yourname_infintudeIT.git', branch: 'main'
            }
        }

        stage('Static Code Analysis') {
            steps {
                // Run static code analysis (e.g., using pylint)
                script {
                    def analysisResult = sh(script: 'pylint *.py', returnStatus: true)
                    if (analysisResult != 0) {
                        error 'Static code analysis failed, aborting the build.'
                    }
                }
            }
        }

        stage('Terraform Init and Apply') {
            steps {
                // Initialize and apply Terraform script
                dir('path/to/terraform') {  // Change to the directory where your Terraform script is located
                    sh 'terraform init'
                    sh 'terraform apply -auto-approve'  // Auto-approve to skip confirmation
                }
            }
        }

        stage('Deploy FASTAPI Application') {
            steps {
                // SSH into the EC2 instance and run the FastAPI application
                script {
                    // Replace with your actual EC2 instance public IP
                    def ec2InstanceIp = 'your.ec2.public.ip'
                    sh """
                    ssh -o StrictHostKeyChecking=no -i path/to/your/key.pem ec2-user@${ec2InstanceIp} << 'ENDSSH'
                        # Navigate to your application directory
                        cd /path/to/your/app

                        # Install dependencies and run the application
                        pip install -r requirements.txt
                        nohup uvicorn main:app --host 0.0.0.0 --port 80 &
                    ENDSSH
                    """
                }
            }
        }

        stage('Configure Elastic Load Balancer') {
            steps {
                // Configure Elastic Load Balancer (example using AWS CLI)
                script {
                    sh """
                    # Create an Elastic Load Balancer (Change the parameters as per your needs)
                    aws elbv2 create-load-balancer \
                        --name my-load-balancer \
                        --subnets subnet-xxxxxx subnet-yyyyyy \
                        --security-groups sg-xxxxxx

                    # Create a target group
                    aws elbv2 create-target-group \
                        --name my-targets \
                        --protocol HTTP \
                        --port 80 \
                        --vpc-id vpc-xxxxxx

                    # Register the EC2 instance with the target group
                    aws elbv2 register-targets \
                        --target-group-arn arn:aws:elasticloadbalancing:region:account-id:targetgroup/my-targets/xxxxxxxx \
                        --targets Id=i-xxxxxxxxx

                    # Create a listener for the load balancer
                    aws elbv2 create-listener \
                        --load-balancer-arn arn:aws:elasticloadbalancing:region:account-id:loadbalancer/app/my-load-balancer/xxxxxxxx \
                        --protocol HTTP \
                        --port 80 \
                        --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:region:account-id:targetgroup/my-targets/xxxxxxxx
                    """
                }
            }
        }
    }

    post {
        always {
            // Clean up resources or notify on completion
            echo 'Pipeline completed.'
        }
    }
}
