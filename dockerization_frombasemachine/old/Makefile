IMAGE_NAME=api-machine-amd64

# DOCKER #######################################################################

docker_build_api_machine_amd64_dev:
	docker build \
	--platform linux/amd64 \
	--tag=${IMAGE_NAME}:dev \
	.

docker_build_api_machine_amd64_prod:
	docker build \
	--platform linux/amd64 \
	--tag=${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT_ID}/${GCP_AR_REPO}/${IMAGE_NAME}:prod \
	.

docker_push_prod:
	docker push ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT_ID}/${GCP_AR_REPO}/${IMAGE_NAME}:prod

docker_run_prod:
	gcloud run deploy \
	--image ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT_ID}/${GCP_AR_REPO}/${IMAGE_NAME}:prod \
	--memory ${GAR_MEMORY} \
	--region ${GCP_REGION}

# docker_start_local:
# 	docker run -e PORT=8000 -p 8000:8000 ${IMAGE_NAME}:dev

# docker_start_local_it:
# 	docker run -it -e PORT=8000 -p 8000:8000 ${IMAGE_NAME}:dev bash

# GCP CONFIG ###################################################################

# gcp_auth_configure_docker:
# 	gcloud auth configure-docker ${GCP_REGION}-docker.pkg.dev

# gcp_ar_create_repo:
# 	gcloud artifacts repositories create ${GCP_AR_REPO} \
# 	--repository-format=docker \
# 	--location=${GCP_REGION} \
# 	--description="tiab repo"

# GCP BUILD, PUSH, DEPLOY ######################################################

# gcp_docker_build:
# 	docker build \
# 	--platform linux/amd64 \
# 	-t ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT_ID}/${GCP_AR_REPO}/${GCP_AR_IMAGE}:prod .

# gcp_docker_push:
# 	docker push ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT_ID}/${GCP_AR_REPO}/${GCP_AR_IMAGE}:prod

# gcp_cloud_run_deploy:
# 	gcloud run deploy \
# 	--image ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT_ID}/${GCP_AR_REPO}/${GCP_AR_IMAGE}:prod \
# 	--memory ${GAR_MEMORY} \
# 	--region ${GCP_REGION}
