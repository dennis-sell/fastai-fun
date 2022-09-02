
.PHONY: cp_to_staging
cp_to_staging:
	# Uploads to hugging face luxury bag space. Note that hugging face uses
	# a separate git repo, which is already set up the repo locally.
	# Just go to this repo and git push when ready to deploy
	cp bag_classifier/* ../hugging_space/bag_classifier/

launch:
	cd bag_classifier/ && python3 app.py
