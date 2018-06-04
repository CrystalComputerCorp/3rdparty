
OS_VER := $(shell cat /etc/redhat-release | sed 's/.*release \([56789]\).*/\1/')

RPM_OUTPUT_DIR ?= $(shell pwd)
RPM_BUILDOPTS := --define '_rpmdir $(RPM_OUTPUT_DIR)' \
                 --define '_build_name_fmt %{NAME}-%{VERSION}-%{RELEASE}.%{ARCH}.rpm' \
                 --define '_sourcedir $(shell pwd)' \
                 --define '_srcrpmdir $(shell pwd)'

ZMQ_VER := 4.1.6
ZMQ_URL := https://github.com/zeromq/zeromq4-1/releases/download/v4.1.6/zeromq-4.1.6.tar.gz
ZMQ_TARBALL := zeromq-$(ZMQ_VER).tar.gz

ifeq ($(OS_VER),7)
all: x86_64 i686
x86_64: $(ZMQ_TARBALL)
	rpmbuild $(RPM_BUILDOPTS) \
	    --define 'dist $(shell rpmbuild --eval %dist | sed -e s/.centos//)' \
	    -ba zeromq.spec
i686:
	setarch i386 \
	    /usr/bin/mock -r centos-7-i386 \
	    --define 'dist $(shell rpmbuild --eval %dist | sed -e s/.centos//)' \
	    --resultdir $(shell pwd) \
	    rebuild *.src.rpm \
	&& rm -f *.log
else
all: x86_64 i686
	@echo "Nothing to do for this OS version"
endif

$(ZMQ_TARBALL):
	wget https://github.com/zeromq/zeromq4-1/releases/download/v4.1.6/zeromq-4.1.6.tar.gz

clean:
	@rm -f *.rpm *.log