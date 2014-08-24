#!/usr/local/www/cgi-bin/tablecg
#
# $DragonFly: site/data/main/errata.cgi,v 1.2 2004/09/07 01:56:57 justin Exp $
# $Id: errata.cgi,v 1.3 2004/10/05 13:02:12 wids Exp $

$TITLE(DragonFly - Errata)
<h1>DragonFly ISO の Errata</h1>
<p>
<CENTER>DragonFly Errata</CENTER>
</p><p>
<table BORDER="1">
<tr>
<th>Id</th>
<th>バージョン</th>
<th>修正時期</th>
<th>解説</th>
</tr>

<tr>
<td>#1</td>
<td>REL1.0</td>
<td>REL1.0A</td>
<td>インストーラが /etc, /usr/local/bin, /usr/local/etc, そして /usr/local/share/pristine に ユーザ 1000 そして/または グループ 1000 に所有され、そのユーザあるいはグループによって書き込み可能なファイルやディレクトリを含む多くのファイルを作成する。</td>
</tr>

<tr>
<td>#2</td>
<td>&lt;=REL1.0A</td>
<td>[次リリース]</td>
<td>新規インストールされるシステムで crond と syslogd がデフォルト(/etc/rc.conf 中)で有効にならない。</td>
</tr>

<tr>
<td>#3</td>
<td>&lt;=REL1.0A</td>
<td>[2004 年 7 月 21 日の current]</td>
<td>ATA-RAID ('ar') は、RAID が破損の跡を残し、使用できずアレイを削除し再作成することを要求し、パーティーションテーブルが修正のために同じ設定を使ってリストア(scan_ffs port はこれをおおいに助けてくれる)される原因になる、古いコードを含んでいる。
1.0A ISO では ATA-RAID を使用しないように。</td>
</tr>

</table>
</p>
