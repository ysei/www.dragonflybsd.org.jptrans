#!/usr/local/www/cgi-bin/tablecg
#
# $DragonFly: site/data/main/download.cgi,v 1.53 2004/07/24 15:09:54 justin Exp $
# $Id: download.cgi,v 1.3 2004/08/23 14:56:19 wids Exp $

$TITLE(DragonFly - Download)
<h1>DragonFly �μ���</h1>

<h2>CD ���᡼��</h2>

<p>
DragonFly �� CD �� 'live' �Ǥ���
������ CD �ǥ����ƥ��֡��Ȥ���(�ѥ����̵����) root �Ȥ��ƥ����󤷡�IDE �Υǥ���������Ѥ��Ƥ��륷���ƥ�إ��󥹥ȡ���Ǥ��ޤ��� 
CD �ϥ��󥽡��롢���뤤��(�¸�Ū��)�����֥֥饦����ͳ��ư��륤�󥹥ȡ����ޤ�Ǥ��ޤ���
���¿���ξ���� 
<a href="/cgi-bin/cvsweb.cgi/~checkout~/src/nrelease/root/README">README</a> 
�ե�������ɤ�ǳ�ǧ���Ƥ���������
��������ɤǤ�����Υꥹ�Ȥϲ����Υ�������ɥ����Ȱ����򸫤Ƥ���������
</p>

<p>
<b>The DragonFly 1.0-RELEASE ����������ޤ���! ��������ɤϲ����Υ����Ȱ�������ɤ���! 
��꡼���ե������ md5 �ϰʲ��Τ褦�ˤʤäƤ��ޤ�:
<br />MD5 (dfly-1.0REL.iso.gz) = c95a378c13257f39420f5f9e4104bd7b
<br />MD5 (dfly-1.0_REL-1.0A_REL.xdelta) = 6001980541a4a2b77505c1845f925d57
<br />MD5 (dfly-1.0A_REL.iso) = ddf5686f828b2ece0b4029ae3ed78c2a
<br />MD5 (dfly-1.0A_REL.iso.gz) = b1c8ded31133960fa58a7b10c300aabd

</b><br /> </p>
<p><b>
���! ��꡼���Ǥϡ����󥹥ȡ���� fdisk �ȥ��饤��������������� 1.0A  �˹�������ޤ�����
���ꥸ�ʥ�� 1.0REL ISO-image ���������ɤ�����ã�Τ���� xdelta (/usr/ports/misc/xdelta) �ѥå����Ѱդ��Ƥ��ޤ���
�ޤ��������� ISO-image �ϥߥ顼�����Ȥ����ۺѤߤǤ���
�ѥå���Ŭ�Ѥ���ˤϡ�1.0REL �� ISO-image �� unzip �����ѥå���Ŭ�Ѥ������줫�� md5 �����餻����̡����줬 unzip ���줿 1.0A_REL �� ISO-image �Ȱ��פ��뤫�ɤ�����Τ���Ƥ���������
</b></p>

<h2>CVS ��ͳ�Υ���������</h2>

<p>
cvsup ���ͳ���ƤΥ����������򹥤�Ǥ�����ϡ�1��1��Τߤˤʤ�ޤ����� /home/dcvs �إ�������������뤿���
<a href="dragonfly-cvs-supfile">���� cvsup ������ե�����</a>
�����ѤǤ��ޤ���
sys ���ؤΤߤ� cvsup ����ե�������Ѱդ���Ƥ��ޤ���
Ŭ�ڤ� cvsup �����Фξ��ˤĤ��Ƥϲ����򸫤Ƥ���������
</p>


<h2>����¾�Υ�����</h2>

BSD �濴�Υ��ߥ�˥ƥ��ˤ�륦���֥����ȤǤ��� 
<a href="http://gobsd.com">GoBSD.com</a> 
�� ����� 
<a href="http://gobsd.com/packages">build  �Ѥ� DragonFly ���եȥ������ѥå�����</a>
���󶡤��Ƥ��ޤ���
������ <code>pkg_add -r <i>packagename</i></code> �Ȥ�����ˡ�ǥ��󥹥ȡ��뤹�뤳�Ȥ���ǽ�Ǥ���

<p>
����� DragonFly �ν�����ȥ˥塼���� 
<a href="http://www.shiningsilence.com/dbsdlog/">DragonFly BSD Log</a> 
����𤵤�ޤ���
</p>

<h2>1.0 Release Errata</h2>
<p>
<A HREF="http://www.bsdinstaller.org/errata.html">���󥹥ȡ���� Errata</A>
<br /><A HREF="errata.cgi">����Ū�� Errata</A>
</p>
<p><b>
���פ��ɲ� Errata: ʣ���Υ��饤������ĥǥ�������ǥ��󥹥ȡ������Ѥ���ȡ����줬�Ǹ�Υ��饤���Ǥʤ����ˤ���Ū�Υ��饤������Ŭ�ڤ˥ꥵ�������졢�Ǹ�Υ��饤����Ʊ���������ˤʤꡢ���Ū�˥ǥ�����������Ƥ��ޤ��ޤ���
��������������� 1.0A �����߼�����ǽ�ˤʤäƤ��ޤ����� xdelta �ѥå��������ǽ�Ǥ�: 
<A HREF="ftp://ftp.dragonflybsd.org/iso-images/dfly-1.0_REL-1.0A_REL.xdelta">dfly-1.0_REL-1.0A_REL.xdelta (�ޥ����������Ⱦ�)</A>. 
1.0A �� ISO-image �ϥߥ顼�����Ȥ����ۺѤߤǤ���
���ꥸ�ʥ��꡼���� ISO-image ����äƤ���Τʤ顢xdelta �ץ����������� 1.0A �ˤ��뤿��� gunzip ���줿 ISO-image �� xdelta �ѥå�����Ѥ���Ŭ�Ѹ�� MD5 �η�̤�Τ���Ƥ���������
</b></p>

<h2>��������ɥ�����</h2>

<TABLE BORDER="0">
<TR>
<TH>�ȿ�̾</TH>
<TH>�ߥ顼����Ƥ�������</TH>
<TH>����������ˡ</TH>
</TR>


<!-- REL links are all grouped together here. -->
<!-- for REL*/1.x releases, please list them here separately, -->
<!-- even if the site's a regular mirror too. -->

<TR><TD CLASS="mirrorsection" COLSPAN="3">�Ǥ�Ƕ�Υ�꡼��</TD></TR>

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

<TR><TD>Fortunaty.net (�衼��å�)</TD>
<TD>1.0A_REL image</TD>
<TD><A HREF="http://ftp.fortunaty.net/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">HTTP</A></TD></TR>

<TR><TD>univie.ac.at</TD>
<TD>1.0A_REL image</TD>
<TD><A HREF="http://ftp.univie.ac.at/systems/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">HTTP</A></TD></TR>

<TR><TD>hp48.org</TD>
<TD>1.0A_REL image</TD>
<TD><A HREF="http://nibble.hp48.org/dragonfly/iso-images/dfly-1.0A_REL.iso.gz">HTTP</A></TD></TR>

<TR><TD>Starkast.net (���������ǥ�)</TD>
<TD>1.0A_REL image</TD>
<TD>
<A HREF="ftp://ftp.starkast.net/pub/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">FTP</A>
<A HREF="http://ftp.starkast.net/pub/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">HTTP</A></TD></TR>

<TR><TD>chlamydia.fs.ei.tum.de (�ɥ���)</TD>
<TD>1.0A_REL image</TD>
<TD><A HREF="http://chlamydia.fs.ei.tum.de/pub/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">HTTP</A>, <A HREF="ftp://chlamydia.fs.ei.tum.de/pub/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">FTP</A></TD></TR>

<TR><TD>BSDTech.com (�Υ륦����)</TD>
<TD>1.0A_REL image</TD>
<TD>
<A HREF="http://dragon.bsdtech.com/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">HTTP</A>, 
<A HREF="ftp://dragon.bsdtech.com/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">FTP</A></TD></TR>

<TR><TD>AllBSD.org (����)</TD>
<TD>1.0A_REL image</TD>
<TD><A HREF="http://pub.allbsd.org/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">HTTP</A>, 
<A HREF="ftp://ftp.allbsd.org/pub/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">FTP</A>, 
<A HREF="rsync://rsync.allbsd.org/dragonfly-iso-images/dfly-1.0A_REL.iso.gz">rysnc</A></TD></TR>

<TR><TD>Pieter from Holland (EU)</TD>
<TD>1.0A_REL image</TD>
<TD><A HREF="http://15pc221.sshunet.nl/DragonFly/iso-images/dfly-1.0A_REL.iso.gz">HTTP</A></TD></TR>

<TR><TD>RPI.edu (����ꥫ���˥塼�衼��)</TD>
<TD>1.0A_REL image</TD>
<TD><A HREF="http://www.acm.cs.rpi.edu/~tbw/dfly-1.0A_REL.iso.gz">HTTP</A></TD></TR>

<TR><TD>Dragonflybsd.org (����ꥫ������ե���˥�)</TD>
<TD>1.0A_REL image</TD>
<TD><A HREF="ftp://ftp.dragonflybsd.org/iso-images/dfly-1.0A_REL.iso.gz">FTP</A>
(<I>�ǽ��¾�Υ����Ȥ��Ʋ�����)</I></TD></TR>

<!--
<TR><TD>EnergyHQ</TD>
<TD>1.0_REL image</TD>
<TD><A HREF="http://www.energyhq.es.eu.org/files/dfly-1.0REL.iso.gz.torrent">BitTorrent</A></TD></TR>
-->

<!-- end of REL links -->
<TR>
<TD COLSPAN="3">&nbsp;</TD>
</TR>

<TR><TD CLASS="mirrorsection" COLSPAN="3">SnapShot �� ISO ���᡼��</TD></TR>

<TR>
<TD>DragonFlyBSD.org (����ե���˥�)</TD>
<TD>Code, ISO master site (<B>���: ISO ��¾�Υ����Ȥ����������ɤ��Ʋ�����!</B>)</TD>
<TD><a href="ftp://ftp.dragonflybsd.org/">FTP</a>
</TD>
</TR>

<TR>
<TD>chlamydia.fs.ei.tum.de (�ɥ���)</TD>
<TD>Snapshots master site, official ISOs</TD>
<TD>
<a href="http://chlamydia.fs.ei.tum.de/pub/DragonFly/snapshots">HTTP</a>
<a href="ftp://chlamydia.fs.ei.tum.de/pub/DragonFly/snapshots">FTP</a>
</TD>
</TR>

<TR>
<TD>AllBSD.org (����)</TD>
<TD>Daily snapshots, official ISOs</TD>
<TD><a href="http://pub.allbsd.org/DragonFly/snapshots/">HTTP</a>,
<a href="ftp://ftp.allbsd.org/pub/DragonFly/snapshots/">FTP</a>, 
rsync
</TD>
</TR>

<TR>
<TD>dragon.BSDTech.com (�Υ륦����)</TD>
<TD>Daily snapshots, official ISOs</TD>
<TD>
<a href="http://dragon.bsdtech.com/DragonFly/">HTTP</a>, 
<a href="ftp://dragon.bsdtech.com/DragonFly/">FTP</a>
</TD>
</TR>

<TR>
<TD>Esat.net (�����ꥹ)</TD>
<TD>Daily snapshots, official ISOs</TD>
<TD>
<a href="http://ftp.esat.net/mirrors/chlamydia.fs.ei.tum.de/pub/DragonFly/">HTTP</a>, 
<a href="ftp://ftp.esat.net/mirrors/chlamydia.fs.ei.tum.de/pub/DragonFly/">FTP</a>, and 
<a href="rsync://ftp.esat.net/mirrors/chlamydia.fs.ei.tum.de/pub/DragonFly/">rysnc</a>. (IPv4 and IPv6)
</TD>
</TR>

<TR>
<TD>Fortunaty.net (�衼��å�)</TD>
<TD>Daily snapshots, official ISOs</TD>
<TD><a href="http://ftp.fortunaty.net/DragonFly/">HTTP</a>,
<a href="ftp://ftp.fortunaty.net/DragonFly/">FTP</a>
</TD>
</TR>

<TR>
<TD>The University of Vienna (�������ȥꥢ)</TD>
<TD>Daily snapshots, official ISOs</TD>
<TD>
<a href="http://ftp.univie.ac.at/systems/DragonFly/">HTTP</a>, 
<a href="ftp://ftp.univie.ac.at/systems/DragonFly/">FTP</a>, and
<a href="rsync://ftp.univie.ac.at/DragonFly/">rsync</a>
</TD>
</TR>

<TR>
<TD>University of Chicago (����ꥫ������Υ�)</TD>
<TD>Official ISOs</TD>
<TD><a href="ftp://cvsup.math.uic.edu/dragonflybsd/">FTP</a></TD>
</TR>

<TR>
<TD>dragonfly.the-bofh.org (������)</TD>
<TD>Daily snapshots, official ISOs</TD>
<TD>
<a href="http://dragonfly.the-bofh.org/">HTTP</a>, 
<a href="ftp://dragonfly.the-bofh.org/">FTP</a>, 
</TD>
</TR>

<TR>
<TD>Starkast.net (���������ǥ�)</TD>
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
<TD>Chung Hua University (����)</TD>
<TD>code, official ISOs</TD>
<TD>
<a href="http://ftp.csie.chu.edu.tw">HTTP</a>, 
<a href="ftp://ftp.csie.chu.edu.tw">FTP</a>
</TD>
</TR>

<TR>
<TD>Providence University (����)</TD>
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

<TR><TD CLASS="mirrorsection" COLSPAN="3">�������ߥ顼</TD></TR>

<TR>
<TD>DragonFlyBSD.org (����ե���˥�)</TD>
<TD>Code master site (<B>���: ¾�Υ����Ȥ�ȤäƲ�����!</B>)</TD>
<TD> 
<a href="http://www.dragonflybsd.org/cgi-bin/cvsweb.cgi">cvsweb</a>
</TD>
</TR>

<TR>
<TD>AllBSD.org (����)</TD>
<TD>Code</TD>
<TD>
rsync, cvsup, cvsync, cvsweb
</TD>
</TR>

<TR>
<TD>dragon.BSDTech.com (�Υ륦����)</TD>
<TD>Code</TD>
<TD>
cvsup</TD>
</TR>

<TR>
<TD>grappa.unix-ag.uni-kl.de (�ɥ���)</TD>
<TD>Code</TD>
<TD>
<a href="http://grappa.unix-ag.uni-kl.de/cgi-bin/cvsweb/?cvsroot=dragonfly">cvsweb</a>, 
cvsup, cvsync, rsync, anoncvs
</TD>
</TR>

<TR>
<TD>dragonfly.the-bofh.org (������)</TD>
<TD>Code</TD>
<TD>
cvsup, <a href="http://dragonfly.the-bofh.org/cgi-bin/cvsweb.cgi/">cvsweb</a>
</TD>
</TR>

</TABLE>

<h2>���ѥ�����</h2>

<TABLE BORDER="0">
<TR>
<TH>�ȿ�̾</TH>
<TH>����������ˡ</TH>
</TR>

<TR>
<TD COLSPAN="2">
DragonFly �˴ؤ����Τ���äƤ��뤢���뾦�ѥ����Ȥ������˥ꥹ�Ȥ���Ƥ��ޤ���
</TR>

<TR>
<TD><B>Crescent Anchor</B><br>
Crescent Anchor �Ϥ鷺��������� DragonFly 1.0A �� CD-ROM ���󶡤���ͽ��Ǥ���
���ʤ��� Crescent Anchor �������������Τΰ����ϡ��᡹��Ω����������ˡ�ͤ��̤��ơ�DragonFly �γ�ȯ��³�Τ���λ��Ȥ����󶡤���뤳�ȤˤʤäƤ��ޤ���
�ܺ٤���ʡ�¾���󶡤��Ƥ����ΤˤĤ��Ƥϡ�Crescent Anchor �򸫤Ƥ���������
</TD>
<TD><A HREF="http://www.crescentanchor.com/">http://www.crescentanchor.com/</A>
</TR>

<TR>
<TD><B>Linux Bazar</B><br>
Linux Bazar ������ʤǥ��եȥ������� CD �����䤷�Ƥ���ȼԤǤ���
�в٤ϥ���ɹ���Τ߹ԤäƤ��ޤ���
</TD>
<TD><A HREF="http://www.LinuxBazar.com/">http://www.LinuxBazar.com/</A>
</TR>

</TABLE>
