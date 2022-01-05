# # FROM should be alwasy the first line of the Dockerfile , and it should be the same as the image name , FROM IMAGE_NAME:TAG
# # e.g.  
FROM ubuntu:latest

# # ------------------------------------------------------------------------------------------------------------------------------#

# # RUN <command> (shell form, the command is run in a shell, which by default is /bin/sh -c on Linux or cmd /S /C on Windows)
# #  can ber used to install software, or to run a command in the container. use -y always to install without asking for confirmation
# RUN apt-get update
# RUN apt-get install nginx -y
RUN echo "rahul" > /tmp/rahul

VOLUME [ "/vol1" ]
# VOLUME [ "/vol1" ]


# # ------------------------------------------------------------------------------------------------------------------------------#


# #  MAINTAINER instruction is deprecated. Instead, one should use the LABEL instruction , it will lable the conainer with the maintainer name
# # LABEL <key>=<value> (label the container with a key-value pair)
# LABEL name="RahulUbuntu" 
# #  view an image’s labels, use the docker inspect command. They will be under the "Labels" JSON attribute

# # ------------------------------------------------------------------------------------------------------------------------------#

# #  Copies new files or directories from <src> and adds them to the filesystem of the image at the path <dest>
# # COPY <src> <dest>
# # <src> may contain wildcards and matching will be done using Go’s filepath.Match rules.
# # <src> must be relative to the source directory that is being built (the context of the build).
# # <dest> is an absolute path, or a path relative to WORKDIR.

# COPY /home/avenger/Desktop/Docker/filea /userfile
# COPY /d/study/tech/DevOps/Git.txt /userfile/Git.txt


# # ------------------------------------------------------------------------------------------------------------------------------#

# #  ADD <src> <dest> , similar to COPY , but it has feature to download files from the internet and also extract and then save to <src>

# ADD http://archive.ubuntu.com/ubuntu/pool/universe/t/tree/tree_1.8.0-1_amd64.deb /tree

# # ------------------------------------------------------------------------------------------------------------------------------#

# #  Informs Docker that the container listens on the specified network port(s) at runtime.
# # EXPOSE does not make the ports of the container accessible to the host

# EXPOSE 8080

# #  The above line will instruct Docker that the container’s service can be connected to via port 8080


# # ------------------------------------------------------------------------------------------------------------------------------#

# # The ENV instruction sets the environment variable <key> to the value <value>.

# ENV name="Rahul"
# ENV key="mykey"

# # ------------------------------------------------------------------------------------------------------------------------------#

# # Sets the working directory for any RUN, CMD, ENTRYPOINT, COPY, and ADD instructions that follow it.
# WORKDIR /userfile

# # ------------------------------------------------------------------------------------------------------------------------------#

# # Docker has a default entrypoint which is /bin/sh -c but does not have a default command
# # CMD and entrypoint  used only once in a Dockerfile

# # CMD defines default commands and/or parameters for a container. CMD is an instruction that is best to use if you need a default
# #  command which users can easily override. If a Dockerfile has multiple CMDs, it only applies the instructions from the last one.
# #  CMD Executes the commands during the Image build process.
# CMD [ "echo" , " * hello this is echo CMD*" ]

# # ------------------------------------------------------------------------------------------------------------------------------#

# # ENTRYPOINT is preferred when you want to define a container with a specific executable
# # similar to CMD but ENTRYPOINT has higher priority than CMD , first command will be executed by only ENTRYPOINT
# ENTRYPOINT [ "echo" , "* hello this is echo ENtry *" ]

# # ------------------------------------------------------------------------------------------------------------------------------#

# # USER instruction sets the user name or 
# #    UID to use when running the image and for any RUN, CMD and ENTRYPOINT instructions that follow it in the Dockerfile.

# USER root
# USER rahuluser
# # ------------------------------------------------------------------------------------------------------------------------------#

# # ARG : lets you define an argument which can be passed to Docker when you build the Docker image from the Dockerfile.