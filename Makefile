PKG_NAME := jdk-zkclient
URL := https://repo1.maven.org/maven2/com/101tec/zkclient/0.8/zkclient-0.8.jar
ARCHIVES := https://repo1.maven.org/maven2/com/101tec/zkclient/0.8/zkclient-0.8.pom %{buildroot}

include ../common/Makefile.common
