.PHONY: all solution clean

PASSWORD="briare"

all:
	./generator.py
	tar -czvf challenge.tar.gz game_0128.bak
	zip -e -P $(PASSWORD) challenge.tar.gz{.zip,}
	@echo "Build successful"

solve:
	@md5sum solution*

clean:
	rm -f solution* *.zip *.gz *.bak