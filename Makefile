update_env_vars:
	direnv reload

show_env_vars:
	@echo SERVICE_ACCOUNT=${SERVICE_ACCOUNT}
	@echo DISPLAY_NAME=${DISPLAY_NAME}
	@echo PROJECT=${PROJECT}
	@echo PROJECT=${PROJECT_ID}

set_gcloud_project:
	gcloud config set project ${GCP_PROJECT_ID}

create_and_download_keys:
	gcloud iam service-accounts keys create ~/code/GCP/${PROJECT}.json --iam-account ${SERVICE_ACCOUNT}@${GCP_PROJECT_ID}.iam.gserviceaccount.com

create_service_account:
	gcloud iam service-accounts create ${SERVICE_ACCOUNT} --display-name ${DISPLAY_NAME}

list_service_accounts:
	gcloud iam service-accounts list

list_projects:
	gcloud projects list

activate_virtual_env:
	pyenv local to-infinity-and-beyond

list_virtual_envs:
	pyenv virtualenvs

git_quick_add_commit_push:
	git add .
	git commit -m 'update'
	git push

git_merge_main_from_seb:
	git checkout seb-python-boilerplate
	git pull origin seb-python-boilerplate
	git merge main
	git push origin seb-python-boilerplate

git_merge_seb_from_main:
	git checkout main
	git pull origin main
	git merge seb-python-boilerplate
	git push origin main

git_switch_main_branch:
	git checkout main

git switch_seb_branch:
	git checkout seb-python-boilerplate
