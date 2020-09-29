
# add centos8 baseos repository
yum-config-manager --add-repo https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64

# install rpms for build
dnf install --nogpgcheck freetds-libs
...
...


# openldap-ltb
# https://github.com/ltb-project/openldap-rpm

vi /etc/yum.repos.d/ltb-project.repo
[ltb-project]
name=LTB project packages
baseurl=https://ltb-project.org/rpm/$releasever/$basearch
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-LTB-project

rpm --import https://ltb-project.org/lib/RPM-GPG-KEY-LTB-project
dnf install openldap-ltb
