terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

# Configure the GitHub Provider
provider "github" {
  token = var.github_token
}

/*Pass the token via CLI: 
terraform plan -var="github_token=$GITHUB_TOKEN"
terraform apply -var="github_token=$GITHUB_TOKEN"*/
variable "github_token" {
  type = string
  sensitive = true
}

resource "github_repository" "LeetCode-Solutions" {
  name        = "LeetCode-Solutions"
  description = "My Leetcode portfolio"

  visibility = "public"
}