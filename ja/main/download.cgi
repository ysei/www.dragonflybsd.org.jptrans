#!/usr/local/www/cgi-bin/tablecg
#
# $DragonFly: site/data/main/download.cgi,v 1.53 2004/07/24 15:09:54 justin Exp $
# $Id: download.cgi,v 1.3 2004/08/23 14:56:19 wids Exp $

$TITLE(DragonFly - Download)
<h1>DragonFly の取得</h1>

<h2>CD イメージ</h2>

<p>
DragonFly の CD は 'live' です。
これらの CD でシステムをブートし、(パスワード無しで) root としてログインし、IDE のディスクを使用しているシステムへインストールできます。 
CD はコンソール、あるいは(実験的に)ウェブブラウザ経由で動作するインストーラを含んでいます。
より多くの情報は 
<a href="/cgi-bin/cvsweb.cgi/~checkout~/src/nrelease/root/README">README</a> 
ファイルを読んで確認してください。
ダウンロードできる場所のリストは下記のダウンロードサイト一覧を見てください。
</p>

<p>
<b>The DragonFly 1.0-RELEASE が公開されました! ダウンロードは下記のサイト一覧からどうぞ! 
リリースファイルの md5 は以下のようになっています:
<br />MD5 (dfly-1.0REL.iso.gz) = c95a378c13257f39420f5f9e4104bd7b
<br />MD5 (dfly-1.0_REL-1.0A_REL.xdelta) = 6001980541a4a2b77505c1845f925d57
<br />MD5 (dfly-1.0A_REL.iso) = ddf5686f828b2ece0b4029ae3ed78c2a
<br />MD5 (dfly-1.0A_REL.iso.gz) = b1c8ded31133960fa58a7b10c300aabd

</b><br /> </p>
<p><b>
注意! リリース版は、インストーラの fdisk とスライスの問題を修正した 1.0A  に更新されました。
オリジナルの 1.0REL ISO-image をダウンロードした人達のために xdelta (/usr/ports/misc/xdelta) パッチを用意しています。
また、新しい ISO-image はミラーサイトへ配布済みです。
パッチを適用するには、1.0REL の ISO-image を unzip し、パッチを適用し、それから md5 を走らせた結果、それが unzip された 1.0A_REL の ISO-image と一致するかどうかを確かめてください。
</b></p>

<h2>CVS 経由のソース取得</h2>

<p>
cvsup を経由してのソース取得を好んでいる場合は、1日1回のみになりますが、 /home/dcvs へソースを取得するために
<a href="dragonfly-cvs-supfile">この cvsup の設定ファイル</a>
が使用できます。
sys 階層のみの cvsup 設定ファイルも用意されています。
適切な cvsup サーバの場所については下記を見てください。
</p>


<h2>その他のサイト</h2>

BSD 中心のコミュニティによるウェブサイトである 
<a href="http://gobsd.com">GoBSD.com</a> 
は 数千の 
<a href="http://gobsd.com/packages">build  済み DragonFly ソフトウェアパッケージ</a>
を提供しています。
これらは <code>pkg_add -r <i>packagename</i></code> という方法でインストールすることが可能です。

<p>
日毎の DragonFly の出来事とニュースは 
<a href="http://www.shiningsilence.com/dbsdlog/">DragonFly BSD Log</a> 
で報告されます。
</p>

<h2>1.0 Release Errata</h2>
<p>
<A HREF="http://www.bsdinstaller.org/errata.html">インストーラの Errata</A>
<br /><A HREF="errata.cgi">一般的な Errata</A>
</p>
<p><b>
重要な追加 Errata: 複数のスライスを持つディスク上でインストーラを使用すると、それが最後のスライスでない時には目的のスライスが不適切にリサイズされ、最後のスライスと同じサイズになり、結果的にディスクが壊れてしまいます。
この問題を修正した 1.0A が現在取得可能になっていますし、 xdelta パッチも取得可能です: 
<A HREF="ftp://ftp.dragonflybsd.org/iso-images/dfly-1.0_REL-1.0A_REL.xdelta">dfly-1.0_REL-1.0A_REL.xdelta (マスターサイト上)</A>. 
1.0A の ISO-image はミラーサイトに配布済みです。
オリジナルリリースの ISO-image を持っているのなら、xdelta プログラムと前記の 1.0A にするために gunzip された ISO-image へ xdelta パッチを使用し、適用後は MD5 の結果を確かめてください。
</b></p>

<h2>ダウンロードサイト</h2>

<TABLE BORDER="0">
<TR>
<TH>組織名</TH>
<TH>ミラーされている内容</TH>
<TH>アクセス方法</TH>
</TR>


<!-- REL links are all grouped together here. -->
<!-- for REL*/1.x releases, please list them here separately, -->
<!-- even if the site's a regular mirror too. -->

<TR><TD CLASS="mirrorsection" COLSPAN="3">最も最近のリリース</TD></TR>

<TR><TD>GoBSD.COM</TD>
<TD>1.0A_REL image</TD>
<TD><A HREF="http://gobsd.com/dfly-1.0A_REL.iso.gz">HTTP</A></TD></TR>

<!-- <TR><TD>The-BOFH.org (Holland)</TD>
<TD>1.0_REL image</TD>
<TD><A HREF="http://www.the-bofh.org/dfly-1.0REL.iso.gz">HTTP</A></TD></TR> 
-->

<!--
<TR><TD>Sitetronics.com</TD>
<TD>1.0_REL image</TD>
<TD><A HREF="http://freebsd0.sitetronics.com/~dodell/dfly-1.0REL.iso.gz">HTTP</A></TD></TR>
-->

<TR><TD>Fortunaty.net (ヨーロッパ)</TD>
<TD>1.0A_REL image</TD>
<TD><A HREF="http://ftp.fortunaty.net/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">HTTP</A></TD></TR>

<TR><TD>univie.ac.at</TD>
<TD>1.0A_REL image</TD>
<TD><A HREF="http://ftp.univie.ac.at/systems/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">HTTP</A></TD></TR>

<TR><TD>hp48.org</TD>
<TD>1.0A_REL image</TD>
<TD><A HREF="http://nibble.hp48.org/dragonfly/iso-images/dfly-1.0A_REL.iso.gz">HTTP</A></TD></TR>

<TR><TD>Starkast.net (スウェーデン)</TD>
<TD>1.0A_REL image</TD>
<TD>
<A HREF="ftp://ftp.starkast.net/pub/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">FTP</A>
<A HREF="http://ftp.starkast.net/pub/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">HTTP</A></TD></TR>

<TR><TD>chlamydia.fs.ei.tum.de (ドイツ)</TD>
<TD>1.0A_REL image</TD>
<TD><A HREF="http://chlamydia.fs.ei.tum.de/pub/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">HTTP</A>, <A HREF="ftp://chlamydia.fs.ei.tum.de/pub/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">FTP</A></TD></TR>

<TR><TD>BSDTech.com (ノルウェー)</TD>
<TD>1.0A_REL image</TD>
<TD>
<A HREF="http://dragon.bsdtech.com/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">HTTP</A>, 
<A HREF="ftp://dragon.bsdtech.com/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">FTP</A></TD></TR>

<TR><TD>AllBSD.org (日本)</TD>
<TD>1.0A_REL image</TD>
<TD><A HREF="http://pub.allbsd.org/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">HTTP</A>, 
<A HREF="ftp://ftp.allbsd.org/pub/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">FTP</A>, 
<A HREF="rsync://rsync.allbsd.org/dragonfly-iso-images/dfly-1.0A_REL.iso.gz">rysnc</A></TD></TR>

<TR><TD>Pieter from Holland (EU)</TD>
<TD>1.0A_REL image</TD>
<TD><A HREF="http://15pc221.sshunet.nl/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">HTTP</A></TD></TR>

<TR><TD>RPI.edu (アメリカ・ニューヨーク)</TD>
<TD>1.0A_REL image</TD>
<TD><A HREF="http://www.acm.cs.rpi.edu/~tbw/dfly-1.0A_REL.iso.gz">HTTP</A></TD></TR>

<TR><TD>Dragonflybsd.org (アメリカ・カリフォルニア)</TD>
<TD>1.0A_REL image</TD>
<TD><A HREF="ftp://ftp.dragonflybsd.org/iso-images/dfly-1.0A_REL.iso.gz">FTP</A>
(<I>最初に他のサイトを試して下さい)</I></TD></TR>

<!--
<TR><TD>EnergyHQ</TD>
<TD>1.0_REL image</TD>
<TD><A HREF="http://www.energyhq.es.eu.org/files/dfly-1.0REL.iso.gz.torrent">BitTorrent</A></TD></TR>
-->

<!-- end of REL links -->
<TR>
<TD COLSPAN="3">&nbsp;</TD>
</TR>

<TR><TD CLASS="mirrorsection" COLSPAN="3">SnapShot と ISO イメージ</TD></TR>

<TR>
<TD>DragonFlyBSD.org (カリフォルニア)</TD>
<TD>Code, ISO master site (<B>注意: ISO は他のサイトからダウンロードして下さい!</B>)</TD>
<TD><a href="ftp://ftp.dragonflybsd.org/">FTP</a>
</TD>
</TR>

<TR>
<TD>chlamydia.fs.ei.tum.de (ドイツ)</TD>
<TD>Snapshots master site, official ISOs</TD>
<TD>
<a href="http://chlamydia.fs.ei.tum.de/pub/DragonFly/snapshots">HTTP</a>
<a href="ftp://chlamydia.fs.ei.tum.de/pub/DragonFly/snapshots">FTP</a>
</TD>
</TR>

<TR>
<TD>AllBSD.org (日本)</TD>
<TD>Daily snapshots, official ISOs</TD>
<TD><a href="http://pub.allbsd.org/DragonFly/snapshots/">HTTP</a>,
<a href="ftp://ftp.allbsd.org/pub/DragonFly/snapshots/">FTP</a>, 
rsync
</TD>
</TR>

<TR>
<TD>dragon.BSDTech.com (ノルウェー)</TD>
<TD>Daily snapshots, official ISOs</TD>
<TD>
<a href="http://dragon.bsdtech.com/DragonFly/">HTTP</a>, 
<a href="ftp://dragon.bsdtech.com/DragonFly/">FTP</a>
</TD>
</TR>

<TR>
<TD>Esat.net (イギリス)</TD>
<TD>Daily snapshots, official ISOs</TD>
<TD>
<a href="http://ftp.esat.net/mirrors/chlamydia.fs.ei.tum.de/pub/DragonFly/">HTTP</a>, 
<a href="ftp://ftp.esat.net/mirrors/chlamydia.fs.ei.tum.de/pub/DragonFly/">FTP</a>, and 
<a href="rsync://ftp.esat.net/mirrors/chlamydia.fs.ei.tum.de/pub/DragonFly/">rysnc</a>. (IPv4 and IPv6)
</TD>
</TR>

<TR>
<TD>Fortunaty.net (ヨーロッパ)</TD>
<TD>Daily snapshots, official ISOs</TD>
<TD><a href="http://ftp.fortunaty.net/DragonFly/">HTTP</a>,
<a href="ftp://ftp.fortunaty.net/DragonFly/">FTP</a>
</TD>
</TR>

<TR>
<TD>The University of Vienna (オーストリア)</TD>
<TD>Daily snapshots, official ISOs</TD>
<TD>
<a href="http://ftp.univie.ac.at/systems/DragonFly/">HTTP</a>, 
<a href="ftp://ftp.univie.ac.at/systems/DragonFly/">FTP</a>, and
<a href="rsync://ftp.univie.ac.at/DragonFly/">rsync</a>
</TD>
</TR>

<TR>
<TD>University of Chicago (アメリカ・イリノイ)</TD>
<TD>Official ISOs</TD>
<TD><a href="ftp://cvsup.math.uic.edu/dragonflybsd/">FTP</a></TD>
</TR>

<TR>
<TD>dragonfly.the-bofh.org (オランダ)</TD>
<TD>Daily snapshots, official ISOs</TD>
<TD>
<a href="http://dragonfly.the-bofh.org/">HTTP</a>, 
<a href="ftp://dragonfly.the-bofh.org/">FTP</a>, 
</TD>
</TR>

<TR>
<TD>Starkast.net (スウェーデン)</TD>
<TD>Daily snapshots, official ISOs</TD>
<TD>
<a href="http://ftp.starkast.net/pub/DragonFly/">HTTP</a>, 
<a href="ftp://ftp.starkast.net/pub/DragonFly/">FTP</a>
</TD>
</TR>

<TR>
<TD>bgp4.net</TD>
<TD>Daily snapshots, official ISOs</TD>
<TD>
<a href="http://www.bgp4.net/pub/DragonFly/">HTTP</a>, 
<a href="ftp://ftp.bgp4.net/pub/DragonFly/">FTP</a>
</TD>
</TR>

<TR>
<TD>Chung Hua University (台湾)</TD>
<TD>code, official ISOs</TD>
<TD>
<a href="http://ftp.csie.chu.edu.tw">HTTP</a>, 
<a href="ftp://ftp.csie.chu.edu.tw">FTP</a>
</TD>
</TR>

<TR>
<TD>Providence University (台湾)</TD>
<TD>Daily snapshots, official ISOs</TD>
<TD>
<a href="http://dragonflybsd.cs.pu.edu.tw/">HTTP</a>,
<a href="ftp://dragonflybsd.cs.pu.edu.tw/DragonFLYBSD">FTP</a>
</TD>
</TR>

<!-- source only after this -->

<TR>
<TD COLSPAN="3">&nbsp;</TD>
</TR>

<TR><TD CLASS="mirrorsection" COLSPAN="3">ソースミラー</TD></TR>

<TR>
<TD>DragonFlyBSD.org (カリフォルニア)</TD>
<TD>Code master site (<B>注意: 他のサイトを使って下さい!</B>)</TD>
<TD> 
<a href="http://www.dragonflybsd.org/cgi-bin/cvsweb.cgi">cvsweb</a>
</TD>
</TR>

<TR>
<TD>AllBSD.org (日本)</TD>
<TD>Code</TD>
<TD>
rsync, cvsup, cvsync, cvsweb
</TD>
</TR>

<TR>
<TD>dragon.BSDTech.com (ノルウェー)</TD>
<TD>Code</TD>
<TD>
cvsup</TD>
</TR>

<TR>
<TD>grappa.unix-ag.uni-kl.de (ドイツ)</TD>
<TD>Code</TD>
<TD>
<a href="http://grappa.unix-ag.uni-kl.de/cgi-bin/cvsweb/?cvsroot=dragonfly">cvsweb</a>, 
cvsup, cvsync, rsync, anoncvs
</TD>
</TR>

<TR>
<TD>dragonfly.the-bofh.org (オランダ)</TD>
<TD>Code</TD>
<TD>
cvsup, <a href="http://dragonfly.the-bofh.org/cgi-bin/cvsweb.cgi/">cvsweb</a>
</TD>
</TR>

</TABLE>

<h2>商用サイト</h2>

<TABLE BORDER="0">
<TR>
<TH>組織名</TH>
<TH>アクセス方法</TH>
</TR>

<TR>
<TD COLSPAN="2">
DragonFly に関するものを売っているあらゆる商用サイトがここにリストされています。
</TR>

<TR>
<TD><B>Crescent Anchor</B><br>
Crescent Anchor はわずかな料金で DragonFly 1.0A の CD-ROM を提供する予定です。
あなたが Crescent Anchor から購入したものの一部は、近々設立される非営利法人を通じて、DragonFly の開発継続のための資金として提供されることになっています。
詳細や価格、他に提供しているものについては、Crescent Anchor を見てください。
</TD>
<TD><A HREF="http://www.crescentanchor.com/">http://www.crescentanchor.com/</A>
</TR>

<TR>
<TD><B>Linux Bazar</B><br>
Linux Bazar は低価格でソフトウェアの CD を販売している業者です。
出荷はインド国内のみ行っています。
</TD>
<TD><A HREF="http://www.LinuxBazar.com/">http://www.LinuxBazar.com/</A>
</TR>

</TABLE>
