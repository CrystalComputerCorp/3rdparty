
OS_VER := $(shell cat /etc/redhat-release | sed 's/.*release \([56789]\).*/\1/')

RPM_OUTPUT_DIR ?= $(shell pwd)
RPM_BUILDOPTS := --define '_rpmdir $(RPM_OUTPUT_DIR)' \
                 --define '_build_name_fmt %{NAME}-%{VERSION}-%{RELEASE}.%{ARCH}.rpm' \
                 --define 'dist $(shell rpmbuild --eval %dist | sed -e s/.centos//)' \
                 --define '_sourcedir $(shell pwd)' \
                 --define '_srcrpmdir $(shell pwd)'

ifeq ($(OS_VER),7)

all:
	setarch i386 rpmbuild $(RPM_BUILDOPTS) -bb v8-trivial.spec
else
	@echo "Nothing to do for this OS version"
endif
clean:
	@rm -f *.rpm *.log