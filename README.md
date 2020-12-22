# Personal-Scripts
scripts that make life easier
# Trmals Scripts steps
1. Install the reuired slenium libraries using pip , install python with versions greater than 3.5
2. Create an account in twillio with free trail access
3. Get the auth token details from twillio and paste in the code
4. Mobile number will be generated from twillio and paste the numbe in code
5. Free trail has limited access to daily messages and overall duration

# Build ec2 login through code build
"Steps for enabling passwor based and granting root access to user
1. login as root an dcreate user ""adduser vamsi""
2. passwd vamsi and then create password
3. cd etc/sudoers add new line 
  vamsi ALL=(ALL) NOPASSWD: ALL
4. this will create a user with with entire root level access no password required once logged in
5. To make password less login enable passwordless authentication to yes whcih is not secure so need to investigate further on this"
6. Once this is done in build spec yaml need to add the required commands for creating docker and running the container
7. SSM has been used for getting the parameters data to make the data secure using KMS

