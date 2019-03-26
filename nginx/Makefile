all:
	rpm -U nginx*.src.rpm
	tar xvzf dev.tar.gz -C ~/rpmbuild/BUILD

get:
	wget https://github.com/sergey-dryabzhinsky/nginx-rtmp-module/archive/dev.tar.gz
	yumdownloader --enablerepo epel --source nginx
	sudo yum-builddep --enablerepo epel -y nginx