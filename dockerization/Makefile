# start_local:
# 	uvicorn api2.app:app --reload

docker_build_local_image:
 	docker build --tag=tiab:dev .

docker_start_local:
	docker run -e PORT=8000 -p 8000:8000 toto:dev

docker_start_local_it:
	docker run -it -e PORT=8000 -p 8000:8000 tiab:dev bash

docker_build_amd64_image:
	docker build --platform linux/amd64 -t $GCP_REGION-docker.pkg.dev/$GCP_PROJECT/taxifare/$GAR_IMAGE:prod .

docker_cp_file_to_container:
	CONTAINER_ID=724b1770694b4c6a0ee3a7f1d31b92d56dcb888c814867f1c168706c68d82e3f
	SOURCE_PATH=./APINEW/api2/app.py
	TARGET_PATH=/api2/app.py
	docker cp ${SOURCE_PATH} ${CONTAINER_ID}:${TARGET_PATH}

gcp_auth_configure_docker:
	gcloud auth configure-docker ${GCP_REGION}-docker.pkg.dev

gcp_ar_create_repo:
	gcloud artifacts repositories create ${GCP_AR_REPO} \
	--repository-format=docker \
	--location=${GCP_REGION} \
	--description="tiab repo"

gcp_docker_build:
	docker build \
	--platform linux/amd64 \
	-t ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT_ID}/${GCP_AR_REPO}/${GCP_AR_IMAGE}:prod .
#	-t ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/tiab/${GCP_AR_IMAGE}:prod .

gcp_docker_push:
	docker push ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT_ID}/${GCP_AR_REPO}/${GCP_AR_IMAGE}:prod
#docker push ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/tiab/${GCP_AR_IMAGE}:prod

gcp_cloud_run_deploy:
	gcloud run deploy \
	--image ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT_ID}/${GCP_AR_REPO}/${GCP_AR_IMAGE}:prod \
	--memory ${GAR_MEMORY} \
	--region ${GCP_REGION}
#	--env-vars-file .env.yaml
