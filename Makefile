# ----- ANY -----
build-docker:
	@echo "generating project requirements..."
	@poetry export --without-hashes --format=requirements.txt > app/requirements.txt
	@echo "building images with compose...";
	@docker compose build
# ---------------

# ----- PROD -----
push-prod:
	@echo "pushing images with compose...";
	@docker compose push
# ---------------

# ----- DEV -----
install:
	@sudo apt-get install pipx ffmpeg
	@pipx ensurepath
	@pipx install poetry==2.1.1
	@poetry install

update-deps:
	@poetry lock
	@poetry install

run:
	@cd app; ENV=development poetry run python main.py

run-docker:
	@docker compose --env-file app/.env up
# ---------------