#!/usr/local/www/cgi-bin/tablecg
#
# $DragonFly: site/data/main/team.cgi,v 1.20 2004/09/24 17:40:55 dillon Exp $
# $Id: team.cgi,v 1.4 2004/10/05 13:14:29 wids Exp $

$TITLE(The DragonFly Team)

<p>
多くのオープンソースプロジェクトと同様に、 DragonFly は地理的に離れた人々のチームによるプロジェクトです。
標準に準拠するということを除けば、貢献者や貢献方法に関する制限は一切ありません。
ここに挙げたのはこのプロジェクトを実現させた幾人かの人々です。
</p>

<p>
<strong>プロジェクトリーダー</strong>:<br />
<a href="mailto:dillon 'at' apollo 'dot' backplane 'dot' com">Matthew Dillon</a> 
は Amiga の DICE C コンパイラを作ったことや、その後サンフランシスコで Best Internet(Best Internet Communications, www.best.com) を共同設立したことで有名です。 
また Matt は VM や NFS 等のコードを FreeBSD プロジェクトや Linux に寄贈していたこともあります。
</p>

<p>
Matt は DragonFly BSD プロジェクトの設立者です。 
Matt は DradonFly への主要なコード寄贈者でもあり、このプロジェクトのウェブサイトや他のオンラインリソースも管理しています。
彼は valiant symlinks 、 MPIPE 、 slab allocator 、 namecache 、 LWKT 、 dfports 、「live CD」、 AMD64 対応、他の貢献者が提案したことの調整、またそれ以外の様々な DragonFly に関するプロジェクトに取り組み、達成してきました。
</p>

<p>
<strong>貢献者</strong>:<br />
多くの個人が様々なアイデアや文書、コードの断片やフィードバックを DragonFly プロジェクトへ寄贈してくれています。
ここにあるのは部分的なリストです。
</p>

<table width="100%" cellpadding="3" cellspacing="0" border="1"
style="border-style: flat; border-collapse: collapse; border-color: #BEBEBE;">
<tr bgcolor="#ffcc00">
<th>名前</th><th>作業対象</th>
</tr>

<tr><td valign="top"><a href="mailto:joe 'at' angerson 'dot' com">Joe Angerson</a></td>
<td valign="top">The DragonFly Mascot Artwork</td>
</tr>

<tr><td valign="top"><a href="mailto:jcoombs 'at' gwi 'dot' net">Joshua Coombs</a></td>
<td valign="top">Sun Grid Engine</td>
</tr>

<tr><td valign="top"><a href="mailto:craig 'at' xlnx-x 'dot' net">Craig Dooley</a></td>
<td valign="top">K&amp;R to ANSI function cleanup, __P() removal, gcc3 building</td>
</tr>

<tr><td valign="top"><a href="mailto:liamfoy 'at' kerneled 'dot' org">Liam Foy</a></td>
<td valign="top">Code cleanness and userland utilities</td>
</tr>

<tr><td valign="top"><a href="mailto:rgarrett24 'at' cox  'dot' net">Robert Garrett</a> </td>
<td valign="top">RCNG, system installation tool
(commit access)</td>
</tr>

<tr><td valign="top">Jeffrey Hsu </td>
<td valign="top">Multithreading the network stack, RFC compliance
(commit access)</td>
</tr>

<tr><td valign="top"><a href="mailto:virtus 'at' wanadoo 'dot' nl">Douwe Kiela</a></td>
<td valign="top">Code cleanness and standards conformation
</td>
</tr>


<tr><td valign="top"><a href="mailto:coolvibe 'at' hackerheaven 'dot' org">Emiel Kollof</a></td>
<td valign="top">NVIDIA binary driver port override, misc kernel stuff, software porting.
</td>
</tr>

<tr><td valign="top"><a href="mailto:max 'at' love2party 'dot' net">Max Laier</a></td>
<td valign="top">Network interface aliasing, PFIL_HOOKS
</td>
</tr>

<tr><td valign="top"><a href="mailto:kmacy 'at' fsmware 'dot' com">Kip Macy</a></td>
<td valign="top">Checkpointing
</td>
</tr>

<tr><td valign="top"><a href="mailto:andre 'at' digirati 'dot' com 'dot' br">Andre Nathan</a> </td>
<td valign="top">Code cleanup, 'route show'
</td>
</tr>

<tr><td valign="top"><a href="mailto:eirikn 'at' kerneled 'dot' com">Eirik Nygaard</a> </td>
<td valign="top">Code cleanness and userland utilities
(commit access)</td>
</tr>

<tr><td valign="top"><a href="mailto:hmp 'at' backplane 'dot' com">Hiten Pandya</a> </td>
<td valign="top">Anything and Everything
(commit access)</td></tr>

<tr><td valign="top"><a href="mailto:cpressey 'at' catseye 'dot' mine 'dot' nu">Chris Pressey</a> </td>
<td valign="top">Janitorial work, Installer
(commit access)</td></tr>

<!--
<tr><td valign="top"><a href="mailto:daver 'at' gomerbud 'dot' com">David Reese</a> </td>
<td valign="top">Syscall separation, stackgap allocation removal
(commit access)</td>
</tr>
-->

<tr><td valign="top"><a href="mailto:drhodus 'at' catpa 'dot' com">David Rhodus</a> </td>
<td valign="top">ACPI, ATAng, security upgrades, NFS, tinderbox builds
(commit access)</td>
</tr>

<tr><td valign="top"><a href="mailto:asmodai 'at' wxs 'dot' nl">Jeroen Ruigrok van der Werven</a> </td>
<td valign="top">Regression testing, algorithm testing, subsystems
(PCI, USB, AGP, UDF, ISO9660, etc), compiler and utilities.
(commit access)</td>
</tr>

<tr><td valign="top"><a href="mailto:galen_sampson 'at' yahoo 'dot' com">Galen Sampson</a></td>
<td valign="top">LWKT port to userland
</td>
</tr>

<tr><td valign="top">Hiroki Sato </td>
<td valign="top">Mirror in Japan (AllBSD)
</td>
</tr>

<tr><td valign="top"><a href="mailto:corecode 'at' fs 'dot' ei 'dot' tum 'dot' de">Simon 'corecode' Schubert</a></td>
<td valign="top">Mirror in Germany, daily snapshots
</td>

</tr>

<tr><td valign="top">
<a href="mailto: joerg 'at' bec 'dot' de">J&ouml;rg Sonnenberger</a></td>
<td valign="top">Anything and Everything except web site
(commit access)
</td>
</tr>

<tr><td valign="top">
<a href="mailto:justin 'at' shiningsilence 'dot' com">Justin Sherrill</a></td>
<td valign="top">Secretarial work, documentation, website cleanup
(commit access)</td>
</tr>

<tr><td valign="top"><a href="mailto:geekgod 'at' geekgod 'dot' com">Scott Ullrich</a></td>
<td valign="top">Installer
</td>
</tr>

</table>

