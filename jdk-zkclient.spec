Name     : jdk-zkclient
Version  : 0.8
Release  : 4
URL      : https://repo1.maven.org/maven2/com/101tec/zkclient/0.8/zkclient-0.8.jar
Source0  : https://repo1.maven.org/maven2/com/101tec/zkclient/0.8/zkclient-0.8.jar
Source1  : https://repo1.maven.org/maven2/com/101tec/zkclient/0.8/zkclient-0.8.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-zkclient-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-zkclient package.
Group: Data

%description data
data components for the jdk-zkclient package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/zkclient.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/zkclient.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/zkclient.xml \
%{buildroot}/usr/share/maven-poms/zkclient.pom \
%{buildroot}/usr/share/java/zkclient.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/zkclient.jar
/usr/share/maven-metadata/zkclient.xml
/usr/share/maven-poms/zkclient.pom
