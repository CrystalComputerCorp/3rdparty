#########################################################################
# elasticsearch-plugin-head
#########################################################################

%define _builddir ./
%define _sourcedir ./
%define _rpmdir ./rpm/
%define prefix /usr/share/elasticsearch/plugins/head/_site/

#########################################################################
Summary: ElasticSearch Head Plugin
Name: elasticsearch-plugin-head
Version: %{version}
Release: %{release}
License: Apache-2.0
Group: ElasticSearch/Plugins
BuildArch: noarch
URL: https://github.com/mobz/elasticsearch-head

Requires: elasticsearch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This package installs the elasticsearch head plugin

%prep

%build

%install

mkdir -p %{_rpmdir} %{buildroot}%{prefix}
cp -a elasticsearch-head/* %{buildroot}%{prefix}

%pre

%post

%postun

%clean

rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{prefix}/Gruntfile.js
%{prefix}/LICENCE
%{prefix}/README.textile
%{prefix}/dist/app.css
%{prefix}/dist/app.js
%{prefix}/dist/base/favicon.png
%{prefix}/dist/base/loading.gif
%{prefix}/dist/base/reset.css
%{prefix}/dist/fonts/FontAwesome.otf
%{prefix}/dist/fonts/fontawesome-webfont.eot
%{prefix}/dist/fonts/fontawesome-webfont.svg
%{prefix}/dist/fonts/fontawesome-webfont.ttf
%{prefix}/dist/fonts/fontawesome-webfont.woff
%{prefix}/dist/i18n.js
%{prefix}/dist/lang/en_strings.js
%{prefix}/dist/lang/fr_strings.js
%{prefix}/dist/lang/pt_strings.js
%{prefix}/dist/vendor.css
%{prefix}/dist/vendor.js
%{prefix}/elasticsearch-head.sublime-project
%{prefix}/grunt_fileSets.js
%{prefix}/index.html
%{prefix}/package.json
%{prefix}/src/app/app.css
%{prefix}/src/app/app.js
%{prefix}/src/app/base/boot.js
%{prefix}/src/app/base/favicon.png
%{prefix}/src/app/base/loading.gif
%{prefix}/src/app/base/reset.css
%{prefix}/src/app/data/boolQuery.js
%{prefix}/src/app/data/dataSourceInterface.js
%{prefix}/src/app/data/metaData.js
%{prefix}/src/app/data/metaDataFactory.js
%{prefix}/src/app/data/model/model.js
%{prefix}/src/app/data/model/modelSpec.js
%{prefix}/src/app/data/query.js
%{prefix}/src/app/data/queryDataSourceInterface.js
%{prefix}/src/app/data/resultDataSourceInterface.js
%{prefix}/src/app/lang/en_strings.js
%{prefix}/src/app/lang/fr_strings.js
%{prefix}/src/app/lang/pt_strings.js
%{prefix}/src/app/services/cluster/cluster.js
%{prefix}/src/app/services/cluster/clusterSpec.js
%{prefix}/src/app/services/clusterState/clusterState.js
%{prefix}/src/app/services/clusterState/clusterStateSpec.js
%{prefix}/src/app/services/storage.js
%{prefix}/src/app/ui/abstractField/abstractField.css
%{prefix}/src/app/ui/abstractField/abstractField.js
%{prefix}/src/app/ui/abstractPanel/abstractPanel.css
%{prefix}/src/app/ui/abstractPanel/abstractPanel.js
%{prefix}/src/app/ui/abstractWidget/abstractWidget.js
%{prefix}/src/app/ui/anyRequest/anyRequest.css
%{prefix}/src/app/ui/anyRequest/anyRequest.js
%{prefix}/src/app/ui/browser/browser.css
%{prefix}/src/app/ui/browser/browser.js
%{prefix}/src/app/ui/button/button.css
%{prefix}/src/app/ui/button/button.js
%{prefix}/src/app/ui/button/buttonDemo.js
%{prefix}/src/app/ui/checkField/checkField.js
%{prefix}/src/app/ui/checkField/checkFieldDemo.js
%{prefix}/src/app/ui/checkField/checkFieldSpec.js
%{prefix}/src/app/ui/clusterConnect/clusterConnect.css
%{prefix}/src/app/ui/clusterConnect/clusterConnect.js
%{prefix}/src/app/ui/clusterOverview/clusterOverview.css
%{prefix}/src/app/ui/clusterOverview/clusterOverview.js
%{prefix}/src/app/ui/csvTable/csvTable.js
%{prefix}/src/app/ui/dateHistogram/dateHistogram.js
%{prefix}/src/app/ui/dialogPanel/dialogPanel.js
%{prefix}/src/app/ui/draggablePanel/draggablePanel.js
%{prefix}/src/app/ui/filterBrowser/filterBrowser.css
%{prefix}/src/app/ui/filterBrowser/filterBrowser.js
%{prefix}/src/app/ui/header/header.css
%{prefix}/src/app/ui/header/header.js
%{prefix}/src/app/ui/helpPanel/helpPanel.js
%{prefix}/src/app/ui/indexOverview/indexOverview.js
%{prefix}/src/app/ui/indexSelector/indexSelector.js
%{prefix}/src/app/ui/infoPanel/infoPanel.css
%{prefix}/src/app/ui/infoPanel/infoPanel.js
%{prefix}/src/app/ui/jsonPanel/jsonPanel.css
%{prefix}/src/app/ui/jsonPanel/jsonPanel.js
%{prefix}/src/app/ui/jsonPretty/jsonPretty.css
%{prefix}/src/app/ui/jsonPretty/jsonPretty.js
%{prefix}/src/app/ui/menuButton/menuButton.css
%{prefix}/src/app/ui/menuButton/menuButton.js
%{prefix}/src/app/ui/menuPanel/menuPanel.css
%{prefix}/src/app/ui/menuPanel/menuPanel.js
%{prefix}/src/app/ui/nodesView/nodesView.css
%{prefix}/src/app/ui/nodesView/nodesView.js
%{prefix}/src/app/ui/nodesView/nodesViewDemo.js
%{prefix}/src/app/ui/page/page.js
%{prefix}/src/app/ui/panelForm/panelForm.css
%{prefix}/src/app/ui/panelForm/panelForm.js
%{prefix}/src/app/ui/queryFilter/queryFilter.css
%{prefix}/src/app/ui/queryFilter/queryFilter.js
%{prefix}/src/app/ui/refreshButton/refreshButton.js
%{prefix}/src/app/ui/refreshButton/refreshButtonDemo.js
%{prefix}/src/app/ui/refreshButton/refreshButtonSpec.js
%{prefix}/src/app/ui/resultTable/resultTable.js
%{prefix}/src/app/ui/selectMenuPanel/selectMenuPanel.css
%{prefix}/src/app/ui/selectMenuPanel/selectMenuPanel.js
%{prefix}/src/app/ui/sidebarSection/sidebarSection.css
%{prefix}/src/app/ui/sidebarSection/sidebarSection.js
%{prefix}/src/app/ui/splitButton/splitButton.css
%{prefix}/src/app/ui/splitButton/splitButton.js
%{prefix}/src/app/ui/splitButton/splitButtonDemo.js
%{prefix}/src/app/ui/structuredQuery/structuredQuery.css
%{prefix}/src/app/ui/structuredQuery/structuredQuery.js
%{prefix}/src/app/ui/table/table.css
%{prefix}/src/app/ui/table/table.js
%{prefix}/src/app/ui/textField/textField.js
%{prefix}/src/app/ui/textField/textFieldDemo.js
%{prefix}/src/app/ui/toolbar/toolbar.css
%{prefix}/src/app/ui/toolbar/toolbar.js
%{prefix}/src/app/ux/class.js
%{prefix}/src/app/ux/dragdrop.js
%{prefix}/src/app/ux/fieldCollection.js
%{prefix}/src/app/ux/observable.js
%{prefix}/src/app/ux/table.css
%{prefix}/src/app/ux/templates/templateSpec.js
%{prefix}/src/app/ux/templates/templates.js
%{prefix}/src/vendor/dateRangeParser/date-range-parser.js
%{prefix}/src/vendor/font-awesome/css/font-awesome.css
%{prefix}/src/vendor/font-awesome/css/font-awesome.min.css
%{prefix}/src/vendor/font-awesome/fonts/FontAwesome.otf
%{prefix}/src/vendor/font-awesome/fonts/fontawesome-webfont.eot
%{prefix}/src/vendor/font-awesome/fonts/fontawesome-webfont.svg
%{prefix}/src/vendor/font-awesome/fonts/fontawesome-webfont.ttf
%{prefix}/src/vendor/font-awesome/fonts/fontawesome-webfont.woff
%{prefix}/src/vendor/graphael/g.raphael.standalone.js
%{prefix}/src/vendor/i18n/i18n.js
%{prefix}/src/vendor/joey/joey.js
%{prefix}/src/vendor/jquery/jquery.js
%{prefix}/src/vendor/nohtml/jquery-nohtml.js
%{prefix}/test/demo.html
%{prefix}/test/generators/conflictingField.sh
%{prefix}/test/generators/delete_all_indices.sh
%{prefix}/test/generators/multi_type.sh
%{prefix}/test/generators/twitter_feed.sh
%{prefix}/test/generators/twitter_river.sh
%{prefix}/test/perf.html
%{prefix}/test/spec/specHelper.js
