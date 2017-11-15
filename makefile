default: nim

nim: nim.pybf
	./bf_reader.py nim && ./pbfc nim.bf nim

clean:
	rm -f nim
