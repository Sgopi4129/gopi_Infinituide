# Output the public IP of the EC2 instance
output "instance_public_ip" {
  description = "The public IP address of the web server instance"
  value       = aws_instance.web_server.public_ip
}

# Output the API Gateway URL
output "api_gateway_url" {
  description = "The base URL of the API Gateway"
  value       = aws_api_gateway_deployment.deployment.invoke_url
}
