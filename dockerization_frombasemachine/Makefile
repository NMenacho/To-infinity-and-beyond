IMAGE_NAME=to-inifinity-and-beyond-image-01

# docker_build_api_machine_amd64_dev:
# 	docker build \
# 	--platform linux/amd64 \
# 	--tag=${IMAGE_NAME}:dev \
# 	.

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
