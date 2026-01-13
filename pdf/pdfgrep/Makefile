
BUILD_DIR=test_output

all: mk_output_dir
	python pdfgrep.py 

mk_output_dir:
	mkdir -p $(BUILD_DIR)

clean:
	rm -rf $(BUILD_DIR)
	rm -rf __pycache__