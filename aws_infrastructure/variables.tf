# AWS region
variable "aws_region" {
  description = "The AWS region to create resources in."
  type        = string
  default     = "us-east-1"  # Change the default region as needed
}

# EC2 instance type
variable "instance_type" {
  description = "EC2 instance type."
  type        = string
  default     = "t2.micro"  # Change instance type as needed
}

# VPC CIDR block
variable "vpc_cidr" {
  description = "CIDR block for the VPC."
  type        = string
  default     = "10.0.0.0/16"
}

# Public subnet CIDR block
variable "public_subnet_cidr" {
  description = "CIDR block for the public subnet."
  type        = string
  default     = "10.0.1.0/24"
}

# API Gateway name
variable "api_gateway_name" {
  description = "Name of the API Gateway."
  type        = string
  default     = "MyApiGateway"
}
