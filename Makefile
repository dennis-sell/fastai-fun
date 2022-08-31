
.PHONY: cp_to_staging
cp_to_staging:
	# Uploads to hugging face luxury bag space
	# Note that I already set up the repo locally
	cp bag_classifier/* ../hugging_space/bag_classifier/
	# Just go to this repo and git push when ready to deploy

launch:
	cd bag_classifier/
	python3 app.py
	cd ..
