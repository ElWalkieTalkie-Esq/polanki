create_env:
	conda create --name pylanki python=3.9 -y

install:
	pip install -r requirements.txt
	pip install -e .

	

