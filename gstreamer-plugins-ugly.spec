#
# Conditional build:
%bcond_without	cdio		# don't build cdio plugin
%bcond_without	sid		# don't build sid plugin
%bcond_with	amr		# AMR-NB plugin
#
%define		gstname		gst-plugins-ugly
%define		gst_major_ver	0.10
%define		gst_req_ver	0.10.25
%define		gstpb_req_ver	0.10.25
#
%include	/usr/lib/rpm/macros.gstreamer
#
Summary:	Ugly GStreamer Streaming-media framework plugins
Summary(pl.UTF-8):	Brzydkie wtyczki do środowiska obróbki strumieni GStreamer
Name:		gstreamer-plugins-ugly
Version:	0.10.15
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-ugly/%{gstname}-%{version}.tar.bz2
# Source0-md5:	21c034a762a5da252f91640e53bfe457
Patch0:		%{name}-bashish.patch
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.5
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.1
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gstpb_req_ver}
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	liboil-devel >= 0.3.9
BuildRequires:	libtool >= 1.4
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	python >= 2.1
BuildRequires:	python-PyXML
##
## plugins
##
BuildRequires:	a52dec-libs-devel
%{?with_amr:BuildRequires:	amrnb-devel}
BuildRequires:	lame-libs-devel
%{?with_cdio:BuildRequires:	libcdio-devel >= 0.76}
# not yet
#BuildRequires:	libdvdnav-devel >= 0.1.7
BuildRequires:	libdvdread-devel
BuildRequires:	libid3tag-devel >= 0.15
BuildRequires:	libmad-devel >= 0.15
BuildRequires:	libmpeg2-devel >= 0.5.1
%{?with_sid:BuildRequires:	libsidplay-devel >= 1.36.57}
BuildRequires:	libx264-devel >= 0.1.3
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	twolame-devel >= 0.3.0
Requires:	gstreamer >= %{gst_req_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Obsoletes:	gstreamer-asf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstlibdir 	%{_libdir}/gstreamer-%{gst_major_ver}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plugins.

%description -l pl.UTF-8
GStreamer to środowisko obróbki danych strumieniowych, bazujące na
grafie filtrów operujących na danych medialnych. Aplikacje używające
tej biblioteki mogą robić wszystko od przetwarzania dźwięku w czasie
rzeczywistym, do odtwarzania filmów i czegokolwiek innego związego z
mediami. Architektura bazująca na wtyczkach pozwala na łatwe dodawanie
nowych typów danych lub możliwości obróbki.

##
## Plugins
##

%package -n gstreamer-a52dec
Summary:	GStreamer VOB decoder plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera dekodująca VOB
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}

%description -n gstreamer-a52dec
Plugin for decoding of VOB files.

%description -n gstreamer-a52dec -l pl.UTF-8
Wtyczka dekodująca pliki VOB.

%package -n gstreamer-amrnb
Summary:	GStreamer AMR-NB decoder plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera dekodująca pliki AMR-NB
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-amrnb
Plugin for decoding of AMR-NB files.

%description -n gstreamer-amrnb -l pl.UTF-8
Wtyczka dekodująca pliki AMR-NB.

%package -n gstreamer-cdio
Summary:	GStreamer plugin for CD audio input using libcdio
Summary(pl.UTF-8):	Wtyczka do GStreamera odtwarzająca płyty CD-Audio przy użyciu libcdio
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Requires:	libcdio >= 0.76

%description -n gstreamer-cdio
Plugin for playing audio tracks using libcdio under GStreamer.

%description -n gstreamer-cdio -l pl.UTF-8
Wtyczka do odtwarzania ścieżek dźwiękowych pod GStreamerem za pomocą
libcdio.

%package -n gstreamer-dvdread
Summary:	GStreamer plugin for DVD playback
Summary(pl.UTF-8):	Wtyczka do GStreamera odtwarzająca DVD
Group:		Libraries
# for NLS
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer >= %{gst_req_ver}
Obsoletes:	gstreamer-libdvdread

%description -n gstreamer-dvdread
GStreamer plugin for DVD playback.

%description -n gstreamer-dvdread -l pl.UTF-8
Wtyczka odtwarzająca DVD do GStreamera.

%package -n gstreamer-lame
Summary:	GStreamer plugin encoding MP3 songs
Summary(pl.UTF-8):	Wtyczka do GStreamera kodująca pliki MP3
Group:		Libraries
# for NLS
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-lame
Plugin for encoding MP3 with lame.

%description -n gstreamer-lame -l pl.UTF-8
Wtyczka do GStreamera kodująca pliki MP3 przy użyciu lame.

%package -n gstreamer-mad
Summary:	GStreamer plugin using MAD for MP3 decoding
Summary(pl.UTF-8):	Wtyczka do GStreamera używająca MAD do dekodowania MP3
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}

%description -n gstreamer-mad
Plugin for playback of MP3 songs using the very good MAD library.

%description -n gstreamer-mad -l pl.UTF-8
Wtyczka do odtwarzania plików MP3 przy użyciu bardzo dobrej biblioteki
MAD.

%package -n gstreamer-mpeg
Summary:	GStreamer plugins for MPEG video playback and encoding
Summary(pl.UTF-8):	Wtyczka do GStreamera odtwarzająca i kodująca obraz MPEG
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-mpeg
Plugins for playing and encoding MPEG video.

%description -n gstreamer-mpeg -l pl.UTF-8
Wtyczki do odtwarzania i kodowania obrazu MPEG.

%package -n gstreamer-sid
Summary:	GStreamer Sid C64 music plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera odtwarzająca muzykę Sid C64
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-sid
Plugin for playback of C64 SID format music files.

%description -n gstreamer-sid -l pl.UTF-8
Wtyczka do odtwarzania plików z muzyką w formacie C64 SID.

%package -n gstreamer-x264
Summary:	GStreamer x264 decoder plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera dekodująca przy użyciu biblioteki x264
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}

%description -n gstreamer-x264
GStreamer x264 decoder plugin.

%description -n gstreamer-x264 -l pl.UTF-8
Wtyczka do GStreamera dekodująca przy użyciu biblioteki x264.

%prep
%setup -q -n %{gstname}-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_amr:--disable-amrnb} \
	%{!?with_cdio:--disable-cdio} \
	%{!?with_sid:--disable-sidplay} \
	--disable-static \
	--enable-experimental \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need plugins' *.la files
rm -f $RPM_BUILD_ROOT%{gstlibdir}/*.la

%find_lang %{gstname}-%{gst_major_ver}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{gstname}-%{gst_major_ver}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%{_datadir}/gstreamer-%{gst_major_ver}/presets
%attr(755,root,root) %{gstlibdir}/libgstasf.so
%attr(755,root,root) %{gstlibdir}/libgstdvdlpcmdec.so
%attr(755,root,root) %{gstlibdir}/libgstdvdsub.so
%attr(755,root,root) %{gstlibdir}/libgstiec958.so
%attr(755,root,root) %{gstlibdir}/libgstrmdemux.so
%attr(755,root,root) %{gstlibdir}/libgstsynaesthesia.so
%{_gtkdocdir}/gst-plugins-ugly-plugins-*

##
## Plugins
##

%files -n gstreamer-a52dec
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsta52dec.so

%if %{with amr}
%files -n gstreamer-amrnb
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstamrnb.so
%endif

%if %{with cdio}
%files -n gstreamer-cdio
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcdio.so
%endif

%files -n gstreamer-dvdread
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdvdread.so

%files -n gstreamer-lame
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstlame.so
%attr(755,root,root) %{gstlibdir}/libgsttwolame.so

%files -n gstreamer-mad
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmad.so

%files -n gstreamer-mpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmpeg2dec.so
%attr(755,root,root) %{gstlibdir}/libgstmpegaudioparse.so
%attr(755,root,root) %{gstlibdir}/libgstmpegstream.so

%if %{with sid}
%files -n gstreamer-sid
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstsid.so
%endif

%files -n gstreamer-x264
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstx264.so
