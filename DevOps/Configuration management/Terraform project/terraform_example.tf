#  Using Terraform deploy apache server on AWS amazon linux

# steps :

# 1. configure aws cli
# 2. create vpc
# 3. create subnet
# 4. create security group
# 5. create internet gateway
# 6. create route table
# 7. associate route table with subnet
# 8. create network interface for instance communication over internet
# 9. get elastic ip and attach it to network interface
# 10. launch instance with attaching network interface and user commands to install and run apache server





terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = "us-east-2" # ohio region
 
  access_key = "AKIASKCKEKHHC2JLHWO7"
  secret_key = "iRo/oHcOx5/DbSA/XsqunQ3Y0Jy0yjh3Bs6+WfBr"
}


# -----------------------   VPC -------------------------------------------------

#  e.g. creating a vpc
resource "aws_vpc" "customvpc" {
  cidr_block = "10.0.0.0/16"

  tags = {
    "Name" = "my-custom-vpc-name"
  }

}

# -----------------------   Subnet -------------------------------------------------

resource "aws_subnet" "my-custom-subnet" {
  vpc_id     = aws_vpc.customvpc.id # getting ref id of the vpc without even creating actually
  cidr_block = "10.0.1.0/24"

  availability_zone = "us-east-2a"

  tags = {
    "Name" = "my-custom-subnet-name"
  }

}


# -----------------------   internet gateway -----------------------------------------------

resource "aws_internet_gateway" "my-custom-ig" {
  vpc_id = aws_vpc.customvpc.id # getting ref id of the vpc without even creating actually
  tags = {
    "Name" = "my-custom-ig-name"
  }

}
# -----------------------   Route table -----------------------------------------------

resource "aws_route_table" "my-custom-rt" {
  vpc_id = aws_vpc.customvpc.id # getting ref id of the vpc without even creating actually

  route {
    cidr_block = "0.0.0.0/0" # for all vpc traffic to access the internet
    # cidr_block = "10.0.1.0/24"       # only specific subnet traffic to access the internet
    gateway_id = aws_internet_gateway.my-custom-ig.id
  }



  tags = {
    Name = "my-custom-rt-name"
  }
}

# -----------------------  Route table association -----------------------------------------------

resource "aws_route_table_association" "my-custom-rt-association" {
  subnet_id      = aws_subnet.my-custom-subnet.id
  route_table_id = aws_route_table.my-custom-rt.id


}

# -----------------------  security group -----------------------------------------------

resource "aws_security_group" "sg-custom" {
  name        = "allow_tls"
  description = "Allow TLS inbound traffic"
  vpc_id      = aws_vpc.customvpc.id

  ingress { # inbound traffic  , from internet to instance
    description = "TLS from VPC"
    from_port   = 0
    to_port     = 1024
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]

  }

  egress { # outbound traffic  , from instance to internet
    from_port        = 0
    to_port          = 0
    protocol         = "-1" # -1 means all protocols
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "allow_all_traffic"
  }
}

# -----------------------  network interface  -----------------------------------------------

resource "aws_network_interface" "nic-custom" {
  subnet_id       = aws_subnet.my-custom-subnet.id
  private_ips     = ["10.0.1.50"]
  security_groups = [aws_security_group.sg-custom.id]


}

# -----------------------  assign public ip -----------------------------------------------

resource "aws_eip" "one" {
  vpc                       = true
  network_interface         = aws_network_interface.nic-custom.id
  associate_with_private_ip = "10.0.1.50"
  depends_on = [
    aws_internet_gateway.my-custom-ig # depends on internet gateway as internet gateway is required to assign public ip
  ]

}
# -----------------------   EC2 instance -------------------------------------------------

#   laucnhing a new instance

resource "aws_instance" "web-app-example" { # RESOURCE_NAME can be anything , only use to refer within code / terraform file
  ami           = "ami-0231217be14a6f3ba"
  instance_type = "t2.micro"
  # subnet_id     = aws_subnet.my-custom-subnet.id

  #  availability_zone = "us-east-2a"

  key_name = "rahulkeyaws"

    #  associate_public_ip_address = true
   network_interface {
     device_index = 0
    #  delete_on_termination = true
     network_interface_id = aws_network_interface.nic-custom.id
   }

   user_data = <<-EOF
    #!/bin/bash
    yum update -y
    yum install httpd -y
    service httpd start
    EOF


  tags = {
    Name = "ExampleAppServerInstance" # name for the instance
  }

}



# variable "abs" {
#   default = "http://"
#   description = "value of http://"

#     type = "string"  
# }