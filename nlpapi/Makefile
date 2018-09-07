clean:
	@rm -Rf build dist *.egg-info

gen_thrift:
	@rm -Rf nlpapi/*
	@thrift --out nlpapi --gen py api.thrift

install_deps:
	@pip install -e .

build:
	@python setup.py bdist_wheel
