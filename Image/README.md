
## Load the file in the below order

Dockerfile

requirements.txt

.gitlab-ci.yml

-------------------------------------------------------------------------------------------------

File - Dockerfile.txt

Starts from a small Python base image.

Installs packages from requirements.txt (layer-cached for faster rebuilds).

(Optional) switches to a non-root user for better security.

Sets a default command.

Note - Save the file as a docker file 

-------------------------------------------------------------------------------------------------

File - requirements.txt

Lists Python dependencies to install during the image build.

You may directly add the dependencies in the Dockerfile.

However, keeping dependencies in a separate file improves caching and readability


----------------------------------------------------------------------------------------------------

File - gitlab.txt

It is a continuous integration file

It runs a pipeline to build the image in CI without privileged Docker-in-Docker.

Pushes two tags to the project registry: :<commit-short-sha> and :latest.

Runs automatically when you push to main (and on Merge Reque


Note- Save the file as .gitlab-ci.yml

-----------------------------------------------------------------------------------------------------

Custom Image path

•	gitlab-registry.nrp-nautilus.io/n4e-mizzou/ml_image:428120b1

•	gitlab-registry.nrp-nautilus.io/n4e-mizzou/ml_image:latest

Link: https://gitlab.nrp-nautilus.io/N4e-mizzou/ml_image 