Name:		ardentryst
Summary:	Action/RPG sidescoller
Version:        1.71
Release:        2
License:        GPLv3
Source:         %{name}%{version}.tar.gz
Group:		Games/Adventure
Url:            https://jordan.trudgett.com/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:	noarch
BuildRequires:	python
Requires:	pygame

%description
Ardentryst is an action/RPG sidescoller, focused not just on fighting, 
but on story, and character development. Strategy as well as reflexes 
will be needed to overcome the game. The game is set in another world. 

It is somewhat a cross between Donkey Kong Country, Mario, Castlevania 
and Kingdom Hearts. Ardentryst is focused on a fantasy world. 

The player is guided through a storyline which he or her must act in and 
play a major role in keeping peace and order in Ardentryst. It features 
two playable characters and a variety of weapons, items, armour, monsters, 
and beautiful level scenery and graphics.

Authors:
--------
Jordan Trudgett <jordan_trudgett@hotmail.com>

%prep
%setup -q -n %{name}%{version}

%build

%install
%__rm -rf %{buildroot}

install -m 755 -d -D %{buildroot}%{_bindir}
install -m 755 -D %{name} %{buildroot}%{_bindir}/%{name}
install -m 755 -d -D %{buildroot}%{_datadir}/games/%{name}/
install -m 644 -D *.py OPR.txt %{buildroot}%{_datadir}/games/%{name}/
install -m 755 -d -D %{buildroot}%{_datadir}/pixmaps/
install -m 644 -D icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -m 755 -d -D %{buildroot}%{_datadir}/applications/
install -m 644 -D Ardentryst.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

#Install data
cp -R Base %{buildroot}%{_datadir}/games/%{name}/
cp -R Data %{buildroot}%{_datadir}/games/%{name}/
cp -R Demos %{buildroot}%{_datadir}/games/%{name}/
cp -R Fonts %{buildroot}%{_datadir}/games/%{name}/
cp -R Levels %{buildroot}%{_datadir}/games/%{name}/
cp -R Music %{buildroot}%{_datadir}/games/%{name}/
cp -R Saves %{buildroot}%{_datadir}/games/%{name}/
cp -R Screenshots %{buildroot}%{_datadir}/games/%{name}/
cp -R Sounds %{buildroot}%{_datadir}/games/%{name}/
cp dig.dig %{buildroot}%{_datadir}/games/%{name}/
cp mapconfig.xml %{buildroot}%{_datadir}/games/%{name}/

#Small fixes
sed -i s\|RolePlaying\|AdventureGame\;\|g %{buildroot}%{_datadir}/applications/%{name}.desktop
chmod 755 %{buildroot}%{_datadir}/games/%{name}/%{name}.py

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc help.txt README.txt COPYING
%{_bindir}/%{name}
%dir %{_datadir}/games/%{name}/
%{_datadir}/games/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png



%changelog
* Thu Sep 01 2011 Andrey Bondrov <abondrov@mandriva.org> 1.71-1
+ Revision: 697695
- imported package ardentryst


* Thu Sep 01 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 1.71-1mdv2010.2
- Packaged Ardentryst
