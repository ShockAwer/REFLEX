#! /usr/local/bin/perl
#
#�䂢�ۂ���1.1(list.cgi)
#

require './jcodeLE.pl';
 &init;&decode;
if ($make ne 'on'){ 
$page = 0  if ($page eq '');
$page2 = $page*$lmax;

&html; exit;
}else{
&make
; exit;
}
##################################################
sub init{
($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime(time);
$min = "0$min" if ($min < 10);	$month++;
$youbi = ('��','��','��','��','��','��','�y') [$wday];
$date = "$month��$mday���i$youbi�j$hour��$min��$sec�b";
$today = "$month/$mday";
$chat_file = './den/log.000.dat';
$roommax = 300;#�ݒu�ł���ő�̎�������
$cgidir = 'http://www.plumfield.ne.jp/~neu/reflex/yuipost/';#post�Ƃ����f�B���N�g������CGI��u���ꍇ
if ($ENV{'REQUEST_METHOD'} eq "POST") { read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'}); }
else { $buffer = $ENV{'QUERY_STRING'}; }
}#init END
##################################################
sub html {
print "Content-type: text/html\n\n";
print <<"_HTML_";
<HTML><HEAD><TITLE>���₵����[���REFLEX �V�K�f���쐬</TITLE></HEAD>
<BODY bgcolor="#004040" text="#ffffff" link="#eeffee" vlink="#dddddd" alink="#ff0000">

_HTML_



print <<"_HTML_";
</ul>
<FONT size=+1><B><A NAME="make">���₵����[���REFLEX �V�K�f���쐬</A></B></FONT>�@<font size=-1><b><a href=\"bbs.cgi\">���X�g�ꗗ</a></font></b>�@<font size=-1><b><a href=\"bbs.cgi\?area\=read\">�ŐV���e�ꗗ</a></b></font><BR><p>
<FORM method="GET" ACTION="./list.cgi"><INPUT TYPE=hidden NAME="make" value="on">
�^�C�g���@ <INPUT TYPE=text NAME="title" SIZE="30"><BR>
ID�@�@�@�@ <INPUT TYPE=text NAME="id" SIZE="7">(���p�p������K���L��)<BR>
�p�X���[�h <INPUT TYPE=text NAME="pass" SIZE="7">(���p�p������K���L��)<p>
�w�i�F�@�@ �@<INPUT TYPE=text NAME="bgcolor" SIZE="7" VALUE="004040"><BR>
�����F �@�@�@<INPUT TYPE=text NAME="mgcolor" SIZE="7" VALUE="ffffff"><BR>
�����N�F �@�@<INPUT TYPE=text NAME="lkcolor" SIZE="7" VALUE="eeffee">
<br>
���ǃ����N�F <input type=text name="vlinkcolor" size=7 value="dddddd"><br>
�薼�F �@�@�@<input type=text name="sbcolor" size=7 value="ffffee"><br>
�w�i�摜 �@�@<input type=text name="backimage" size=30 value="http://">
<p>
<INPUT type=submit value="�V�K�쐬�^�ݒ�ύX"></FORM><hr><font size=-1>
�ݒ��ύX����Ƃ��ɂ́AID�ƃp�X���[�h�͑O�Ɠ������̂��g�p���Ă��������B<br>
</font><hr>

<H5 align=right><A HREF="http://www.cup.com/yui/index.html">�䂢�ۂ���(Free)</A></H5></BODY></HTML>
_HTML_
}#html END
##################################################
sub listing{

}#listing END

##################################################
sub decode {
   @pairs = split(/&/,$buffer);
   foreach $pair (@pairs)
   {
       ($name, $value) = split(/=/, $pair);
       $value =~ tr/+/ /;
       $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
&jcode'convert(*value,'sjis');
       $value =~ s/\n//g;$value =~ s/\r//g;$value =~ s/:#//g;
       $value =~ s/<//g;$value =~ s/>//g;
       $value =~ s/&gt//g;$value =~ s/\x00-\x1f//g;
       $value =~ s/$//g;$value =~ s/%//g;$value =~ s/|//g;
       $FORM{$name} = $value;
   }

$id=$FORM{'id'};
$pass = $FORM{'pass'}; 
$title = $FORM{'title'}; 
$page = $FORM{'page'}; 
$make = $FORM{'make'}; 
$amode = $FORM{'amode'}; 
$bmode = $FORM{'bmode'}; 
$bgcolor = $FORM{'bgcolor'};
$mgcolor = $FORM{'mgcolor'}; 
$lkcolor = $FORM{'lkcolor'};  
$vlkcolor = $FORM{'lkcolor'};  
$subcolor = $FORM{'sbcolor'};  
$bimage = $FORM{'backimage'};



if($FORM{'chg'}){
   $hotlist = $FORM{'h'};      $rev = $FORM{'r'};   $lmax = $FORM{'lm'};
}else{ &getcookie;}
$option = $FORM{'op'};
$lmax = '2' if($lmax eq '');
$rev = 'on' if($rev eq '');$hotlist = '0' if($hotlist eq '');
&setcookie;
}#decode END
##################################################
sub make {#�V�K�b�胋�[����ݒu
#�^�C�g���`�F�b�N�B
#&err(3) if(length($title) < 3);
#&err(4) unless(($ENV{'HTTP_REFERER'} eq '') || ($ENV{'HTTP_REFERER'}=~/$cgidir\/list.cgi/) );

$chat_file="./pref/bbb.dat";
$chat_file =~ s/bbb/$id/g;

$data_file="./data/bbb.dat";
$data_file =~ s/bbb/$id/g;


	open(DB, $chat_file);
		@lines = <DB>;
	close(DB);
	$set=shift(@lines);
 	($idd,$passd,$dum) = split(/:#/,$set);
if(($idd eq $id)&&($passd ne $pass)){&err(1);}


$value = "$id:#$pass:#$title:#$amode:#$bmode:#$bgcolor:#$mgcolor:#$lkcolor:#$vlkcolor:#$subcolor:#$bimage:#\n";


open(DB,">$chat_file");
	print DB $value;   print DB @lines;
close(DB);



if (!open(DB,"$data_file"))

 { 
open(OUT,">$data_file");
	print OUT $none;
close(OUT);
}

close(DB);


chmod 0600, "./pref/$id.dat";#0666�łȂ��ƃ_�������B
chmod 0666, "./data/$id.dat";#0666�łȂ��ƃ_�������B

$buffer=~s/&title=/&name2=/;
&locate;
}#make END
#################################################
sub locate{	#�ړ����܂��B

print "Content-type: text/html\n\n";
print <<"_HTML_";
<HTML><HEAD><TITLE>$title</TITLE>
</HEAD><BODY bgcolor="#004040" text="#ffffff" link="#eeffee" vlink="#dddddd" alink="#ff0000">
<H1>
�쐬�����B</H1>
<HR><BR>
<a href="bbs.cgi?area=$id">
������Ɉړ����܂��B</a><BR>�������e������ƃ��X�g�ɒǉ�����܂��B<BR>
<BR><BR><BR><BR><BR>
<H5 ALIGN=right><A HREF="http://www.cup.com/yui/index.html">�䂢�ۂ���(Free)</A></H5></BODY></HTML>
_HTML_
exit;
}#make END

#################################################


sub getcookie{	#�������[�𒸂��܂��B
	$cooks = $ENV{'HTTP_COOKIE'};
	$cooks = '' unless($cooks =~s/.*yuipost=(.*)yuipostend.*/$1/) ;
	($hotlist,$rev,$lmax) = split(/\t/, $cooks);
}#getcookie END

sub setcookie{	#�������[���u���E�U�Ƀv���[���g���܂��B
	$data = "$hotlist\t$rev\t$lmax\tyuipostend";
	print "Set-Cookie: yuipost=$data; expires=Wednesday, 09-Nov-1999 00:00:00 GMT\n" unless ($ENV{'HTTP_COOKIE'}=~/$data/);
}#���̃N�b�L�[��1999/11/9�܂ŗL���ł��B������߂�����A���t�������Ɛ�ɂ��āB
sub err{
$error = $_[0];
print "Content-type: text/html\n\n";
print <<"_HTML_";
<HTML><HEAD><TITLE>$title</TITLE>
</HEAD><BODY BGCOLOR="#A1FE9F" TEXT="#000000" LINK="#ff0000" VLINK="#ff0000" ALINK="#FF0000">
<H1>
�^�C�v $error �̃G���[���������܂����B</H1>
<HR><BR>
�G���[�^�C�v�̐���<BR><BR>
�^�C�v0�F���O�t�@�C�����J���܂���B<BR>
�^�C�v1�F�������ݒ�̏C�����ɕK�v�ƂȂ�p�X���[�h���Ԉ���Ă��܂��B<BR>
�^�C�v3�F�������̃^�C�g�����Z���ł��B<BR>
�^�C�v4�F�\�����ʃG���[�ł��B<BR>
�^�C�v5�F�ݒu�����ő�ݒ�l$roommax���z���邽�߁A�V�K�ɐݒu���ł��܂���B<BR>
<BR><BR><BR><BR><BR>
<H5 ALIGN=right><A HREF="http://www.cup.com/yui/index.html">�䂢�ۂ���(Free)</A></H5></BODY></HTML>
_HTML_
exit;
}
__END__
