
elasticsearch-head:
	[ -d $@ ] || git clone https://github.com/mobz/elasticsearch-head.git
	rpmbuild -bb \
		--define "version `awk -F'[:,]+ *' '/"version"/{print $$2}' elasticsearch-head/package.json | xargs echo -n`" \
		--define "release `p4 counter change`" \
		elasticsearch-head.spec

clean:
	rm -rf elasticsearch-head rpms

.PHONY: elasticsearch-head clean
