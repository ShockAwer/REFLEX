#! /usr/local/bin/perl


#----------------#
#    �����ݒ�    #
#----------------#


# �f���̖��O --------------------------


$title = '���₵����[��ǁ�AMG'; 

# �����F��w�i�Ȃǂ̐ݒ�

# body��

$bgc    = '004040';

$textc  = 'ffffff';

$linkc  = 'eeffee';

$vlinkc = 'dddddd';

$alinkc = 'ff0000';

# �薼�̐F

$subjc  = 'ffffee';

# --- �\������ --------------------------------------------
# �P�y�[�W�ɕ\�����錏���̃f�t�H���g�l
$def =  30;
# �P�y�[�W�ɕ\�����錏���̍ŏ��l
$defmin =  0;
# ���̌����ȏ�Ń����[�h�^�������݂����Ƃ��ɂ͎��͂��̌����ɂ���B
$defmax =120;

# --- �t�q�k ----------------------------------------------
# ���̃X�N���v�g
$cgiurl = 'bbs.cgi';
$readfile= 'loveyou.dat';

# �A����
$mailadd = 'goodby@strangers.com';

# ���O�̂t�q�k
$loglog0 = 'log';
$loglog1 = 'http://';

# ---------------------------------------- �������݃`�F�b�N ----------------------------------------
# �Ǘ��l���O�`�F�b�N�E���[���A�h���X�E�p�X���[�h
$namez = '����';
$pass = 'chiba';
# �������ݍő��
$maxlength = 1024*16; 
#���e���e������
$max_v = 8000;      
#���e���e�s���i��̕������Ƃ̌��ˍ������l���āj
$max_line = 120;     

# ��d�������݃`�F�b�N����
$check = 10;
# ��d�������݃`�F�b�N�o�C�g��
$checklength = 10;
# �������݌����̍ő�o�^���̐ݒ�
$max = '120';
 
# ------------------------------------ �f�B���N�g���E�t�@�C���� ------------------------------------
# ���{��R�[�h�ϊ����C�u����jocde.pl�̃p�X
require './jcode.pl';
# ���e���������܂��L�^�t�@�C���̃p�X��ݒ�
$readfile = './loveyou.dat';
# �ʓr�Ƃ郍�O�̃t�@�C�����擪�����E�g���q�̎w��
$logfile = "./log/";
$logfiledat = ".html";

# -------------------------------------------- �J�E���^ --------------------------------------------
# �J�E���^�v���X�l
$countplus = "";
# �J�E���^�J�n��
$countdate = '99/7/26';
# �J�E���^�t�@�C���̐擪�����E�g���q�̎w��
$countfile = './count/count';
$countfiledat = '.txt';
# �J�E���^���x�i�O�̂Ƃ��͎g�p���Ȃ��j
$countlevel = 1;

# --------------------------------------------- ���̑� ---------------------------------------------
# ����
$tim =0*3600;
# ���͌`���̐ݒ�
$method = 'post';


# ��������
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time + $tim );
$month = ($mon + 1);

# �����̃[���T�v���X
if ($month < 10) { $month = "0$month"; }
if ($mday < 10)  { $mday  = "0$mday";  }
if ($sec < 10)   { $sec   = "0$sec";   }
if ($min < 10)   { $min   = "0$min";   }
if ($hour < 10)  { $hour  = "0$hour";  }

# �j���ϊ�����
$y0="��"; $y1="��"; $y2="��"; $y3="��"; $y4="��"; $y5="��"; $y6="�y";
$youbi = ($y0,$y1,$y2,$y3,$y4,$y5,$y6) [$wday];

# �����t�H�[�}�b�g
$date_now = "$month��$mday��($youbi)$hour��$min��$sec�b";


# ���O�t�@�C�����擾
$filedate = "$logfile$year$month$logfiledat";
# �悭�킩��Ȃ��ϐ�
$gesu = $ENV{'REMOTE_PORT'};
# ���e����action��
$action = "regist";

# �ǉ��΍� -------------------------------

# �O�����e�h�~�R�[�h
$protect_a = 9987;	# 4��
$protect_b = 55;		# 2��
$protect_c = 112;		# 3��

# �ߋ����O�̍ő�t�@�C���T�C�Y
$maxoldlogsize = 4 * 1024 * 1024;		# 3MB

###########################################################################################

# �t�H�[�����͂��ꂽ�f�[�^��$buffer�Ɋi�[����iget��post���ɂ���Ď擾���@���قȂ�j
#if ($ENV{'REQUEST_METHOD'} eq "POST" && $ENV{'CONTENT_LENGTH'} < $maxlength) { read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'}); }
#else { $buffer = $ENV{'QUERY_STRING'}; }
if ($ENV{'REQUEST_METHOD'} eq "POST") { read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'}); } else { $buffer = $ENV{'QUERY_STRING'}; }
if ($ENV{'CONTENT_LENGTH'} > $maxlength) {&error(5);}

# $buffer�Ɋi�[���ꂽFORM�`���̃f�[�^�����o��
@pairs = split(/&/,$buffer);
foreach $pair (@pairs) {
	
	($name, $value) = split(/=/, $pair);
	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	
	# �L�^����f�[�^��sjis
	&jcode'convert(*value,'sjis');
	

#���s�A�ł̂������������i�R�s�ȏ㉽���������ɉ��s�݂̂̕����͉��s�����j
#�X�y�[�X�{���s�̘A�ł�����i��L��������邽�߂ɃX�y�[�X������ĉ��s���鈫�Y�̏ꍇ�j
	if ($value =~ /\r\n/) { $value =~ s/\r\n/\r/g; }
	if ($value =~ /\n/) { $value =~ s/\n/\r/g; }

	if ($value =~ / \r \r/) { $value =~ s/ \r \r//g; }
	if ($value =~ /\�@\r\�@\r/) { $value =~ s/\�@\r\�@\r//g; }
	if ($value =~ / \r/) { $value =~ s/ \r/\r/g; }
	if ($value =~ /\�@\r/) { $value =~ s/\�@\r/\r/g; }
	if ($value =~ /\r\r\r\r/) { $value =~ s/\r\r\r\r//g; }


	# �����̓s����̏���
	$value =~ s/\n//g; # ���s�����͏���
	
	if ($name eq 'value') { $value =~ s/&/&amp\;/g; $value =~ s/\,/\0/g; }
	elsif ($name ne 'page' && $name ne 'image') { $value =~ s/\,//g; $value =~ s/\;//g; $value =~ s/\://g; $value =~ s/\=//g; }
	
	else { $value =~ s/\,//g; }
	
	$value =~ s/</&lt\;/g; $value =~ s/>/&gt\;/g;
	
	$FORM{$name} = $value;
}


# �\���y�[�W���̌��� ##################################################
if ($FORM{'def'} ne '') { $def = $FORM{'def'}; }
if ($def < $defmin) { $def = $defmin;}
$defnext = $def;
if ($defnext > $defmax) {$defnext = $defmax;}



# �\���F�̌��� ########################################################

if ($select ne "1")  { &select; }
$select=1;

# �|�b�v�A�b�v�E�C���h�E�̌��� ########################################################

#if ($FORM{'image'} eq '') { $checked1='checked'; }
#if ($FORM{'image'} eq '2') { $checked2='checked'; }

#if ($FORM{'himage'} eq '') { $himage=''; }
#if ($FORM{'himage'} eq '2'){ $link='$sec$min'; }


# �S�̗̂�������肷��iaction��pwd�̓t�H�[�����͂��ꂽ�f�[�^���i�[���閼�O�j
########################################################
#    action=regist  --> �L���L�^�������Ēʏ��ʂ�
#    ���̑�  --> �ʏ��ʂ�

if (($FORM{'def'} eq '0') && ($FORM{'value'} ne '')) { &regist; }
if ($FORM{'area'} eq 'read') { &read; }
if ($FORM{'area'} eq '') { &list; }
if ($FORM{'action'} eq "$action")  { &regist; }
if ($FORM{'action'} eq 'search1') { &search1; }
if ($FORM{'action'} eq 'search2') { &search2; }
if ($FORM{'action'} eq 'search3') { &search3; }
&html;


# ���C���\���T�u���[�`�� #######################################################
sub html {

if ($select ne "1")  { &select; }
$select=1;

	# �v���e�N�g�L�[����
	local ( $ptime ) = time + $tim * 60 * 60;
	local ( $pkey ) = ( $ptime + $protect_a ) * $protect_b + $protect_c;
	
	print "Content-type: text/html\n\n";
	print "<html><head><title>$title</title></head>\n";
	print "$body\n";

	
	# �o�i�[�͂���
	
print "<font size=+1 color=\"#$subjc\"><b>$title</b></font>�@<font size=-1><b><a href=\"$cgiurl\">���X�g�ꗗ</a></font></b>�@<font size=-1><b><a href=\"$cgiurl\?area\=read\">�ŐV���e�ꗗ</a></font></b>�@<font size=-1><b><a href=\"list.cgi\">�V�K�f���쐬</a></b></font><p>
\n";

print "<form method=$method action=\"$cgiurl\?area\=$FORM{area}\">\n";
	
	print "<input type=hidden name=\"action\" value=\"$action\">\n";
	print "���e�� <input type=text name=\"name\" size=20 maxlength=40 value=\"$FORM{'name'}\"><br>";
	print "���[�� <input type=text name=\"email\" size=30><br>\n";
	print "�薼�@ <input type=text name=\"subject\" size=30 maxlength=60>  \n";
	print "<input type=submit value=\"���e�^�����[�h\"><input type=reset value=\"����\"><p>���e<i>�i�^�O�͎g���܂���B���e���������ɓ��e�{�^���������ƃ����[�h���܂��B�j</i><br><textarea name=\"value\" rows=5 cols=70></textarea><input type=hidden name=\"page\" size=70 value=\"http://\"><p>\n";
	print "�\\������\n";
	print "<input type=text name=\"def\" size=8 value=\"$defnext\">\n";
	print "�o�b�N�O���E���h�J���[<input type=text name=\"bgcolor\" size=6 value=\"$bgc\"><input type=hidden name=\"link\" value=\"$FORM{'link'}\">\n";
	print "URL���������N<input type=checkbox name=\"image\" value=\"1\" checked></font> \n";

	print "<input type=hidden name=\"code\" value=\"$gesu$pkey\">\n";

	print "<input type=hidden name=\"area\" value=\"$FORM{area}\">\n";
	print "<input type=hidden name=\"areaname\" value=\"$title\">\n";

	print "<input type=hidden name=\"win_count\" value=\"$maxcount\">\n";

	print "<input type=hidden name=\"win_time\" value=\"$month$mday$hour$min$sec\">\n";



	# �v���e�N�g�R�[�h�o��
	print "<input type=hidden name=\"protect\" value=\"$pkey\">\n";
	
	
#	print "<br><i>�V�����L������\\�����܂��B�ō�$max���̋L�����L�^����A����𒴂���ƌÂ��L������폜����܂��B<br>\n";
#	print "�P��̕\\����$def�����z����ꍇ�́A���̃{�^�����������ƂŎ��̉�ʂ̋L����\\�����܂��B</i>\n";


		print "<p><font size=\-1\"><a href=\"http://AG.ST2.ARENA.NE.JP/cgi-bin/strangeworld/bbs.cgi\">��������</a>�b<a href=\"http://ch.st6.arena.ne.jp/cgi-bin/strangeworld/bbs/bbs.cgi\">�킩��</a>�b<a href=\"http://extra.tomato.nu/strangeworld/\">�G�N�X�g��</a>
�b<a href=\"http://www.njs.ne.jp/~rebirth/remix/bbs.cgi\">REMIX</a>�b<A href=\"http://members.tripod.com/~swattylink/\">SwattyLink</A> /
<A href=\"http://swatty.virtualave.net/cgi-bin/upload.cgi\">File</a>|<a href=\"http://edoya.neko.to/2/upload.cgi\">���E��Y</a>�b<a href=\"http://strange-empire.virtualave.net/cgi-bin/upload.cgi\">�p�j����[</a>�b<a href=\"http://wave.ruru.ne.jp/loplop/erunst/chat.cgi\">�`���b�g</a><p>
�����̉ߋ����O��<a href=\"getlog_m.cgi\?action\=\getlog\&logfile\=$year$month.html\&day1\=01\&hour1\=00&day2\=31\&hour2=24\&searchmode=bbs\&keyword\=$area\">����</a>�B�挎�̂�<a href=\"getlog_m.cgi\?action\=\getlog\&logfile\=$pastyear$p$pastmonth.html\&day1\=01\&hour1\=00&day2\=31\&hour2=24\&searchmode=bbs\&keyword\=$area\">����</a>�B\n";
#�J�E���^�[
	if ( $countlevel > 0 ){
		print "<font size=-1>$countdate���� ";
		&counter; print "$countplus�i�����ɂ������x��$countlevel�j</font>\n";	}


#	 �T�[�`�̒��ӏ���
	print "<br>���e�̓��e�⃊���[�g�z�X�g�ɂ��K����폜�����Ȃ����߁A�e�l���ӔC�𕉂��Ă��������B<br>�ő�\�\\�������F$max���@�@���F�ԐM�t�H�[���@���F�����T�[�`�@���F�X���b�h�ꗗ\n";


#	�����[�h
	print "<p></font></font><input type=submit value=\"���e�^�����[�h\">\n";
	print "</form>\n";
	
	#--- �L�^�L���̏o�� ----------------------------------#
	
	# �L�^�t�@�C����ǂݏo���I�[�v�����āA�z��<@lines>�Ɋi�[����
	if (!open(DB,"$file")) { &error(0); }
	@lines = <DB>;
	close(DB);
	
	if ($FORM{'page'} eq '') { $page = 0; } else { $page = $FORM{'page'}; }
	
	$accesses = @lines; $accesses--;
	$page_end = $page + $def - 1;
	if ($page_end > $accesses) { $page_end = $accesses; }

	foreach ($page .. $page_end) {
		($date,$name,$email,$value,$subject,$hpage,$himage,$code,$postid,$area) = split(/\,/,$lines[$_]);
		$value =~ s/\0/\,/g; # �k���R�[�h�ɕϊ��L�^�������p�J���}�𕜋A������
		chop($himage) if $himage =~ /\n/;
		chop($hpage) if $hpage =~ /\n/;
		chop($postid) if $postid =~ /\n/;
		&disp;
	}
	
	#--- ���y�[�W���� ------------------------------------#
	
	print "</form><hr><p>\n";
	$page_next = $page_end + 1;
	$i = $page + 1; $j = $page_end + 1;
	if ($page_end ne $accesses) {
		print "<font size=-1><i>�ȏ�́A���ݓo�^����Ă���V����$i�Ԗڂ���$j�Ԗڂ܂ł̋L���ł��B</i></font><p>\n";
		print "<form method=$method action=\"$cgiurl\?area\=$FORM{area}\">\n";
		print "<input type=hidden name=\"area\" value=\"$FORM{area}\">\n";
		print "<input type=hidden name=\"page\" value=\"$page_next\">\n";
		print "<input type=hidden name=\"def\" value=\"$def\">\n";
		print "<input type=hidden name=\"bgcolor\" value=\"$bgc\">\n";
		print "<input type=submit value=\"���̃y�[�W\"></form>\n";
	}
	else {
	
		print "<font size=-1><i>�ȏ�́A���ݓo�^����Ă���V����$i�Ԗڂ���$j�Ԗڂ܂ł̋L���ł��B";
		print "����ȉ��̋L���͂���܂���B</i></font>\n";
	}
	
	# ���̃X�N���v�g�̒��쌠�\���i���Ȃ炸�\�����Ă��������j

		print "<form method=$method action=\"$cgiurl\?area\=$FORM{area}\"><input type=hidden name=\"area\" value=\"$FORM{area}\"><input type=hidden name=\"def\" value=\"$def\"><input type=hidden name=\"bgcolor\" value=\"$bgc\"><input type=submit value=\"�@�����[�h�@\"></form>\n";
	print "<h4 align=right><hr size=5><a href=\"http://www.ask.or.jp/~rescue/\">MiniBBS v7.5</a> <a href=\"http://www.bea.hi-ho.ne.jp/strangeworld/recycle/\">REFLEX 991115</a> is Free.<br></h4>\n";
	print "</body></html>\n";
	exit;
}


# �������ݏ����T�u���[�`�� ############################################################
sub regist {
	
	# ���e���X�y�[�X�Ȃ烊���[�h
	if ($FORM{'value'} eq "") { &html; }

 # �ʂ̃y�[�W���炱�̂b�f�h�ւ̓��e��r�����鏈��
	$ref = $ENV{'HTTP_REFERER'};
	$ref_url = $cgiurl; $ref_url =~ s/\~/.*/g;
	if (!($ref =~ /$ref_url/i)) { &error(form); }
	
	# ���͂��ꂽ�f�[�^�̃`�F�b�N ##################################
	if ($FORM{'bgcolor'} eq "") { &error(1); }
	if ($FORM{'def'} eq "") { &error(1); }
	if ($FORM{'name'} eq "") { $FORM{'name'} = ''; }
	if ($FORM{'email'} =~ /,/) { &error(4); }
          $FORM{'email'}=~ s/\"//g;
	if ($FORM{'email'} ne "") { if (!($FORM{'email'} =~ /(.*)\@(.*)\.(.*)/)) { &error(3); }}
	if ($FORM{'subject'} eq "") { $FORM{'subject'} = '�@'; }
	
	if ($FORM{'page'} eq "" || $FORM{'page'} eq "http://") { $FORM{'page'} = ''; }
	else{
		$FORM{'page'} =~ s/\s//g;$FORM{'page'} =~ s/\"//g;$FORM{'page'} =~ s/\'//g;
		$FORM{'page'} =~ s/http\:\/\/http\:\/\//http\:\/\//g;
	}
	# �s������
if ($max_line) {
		$value_size = ($FORM{'value'} =~ tr/\r/\r/) + 1;     # \r �̐��𐔂���
		if ($value_size > $max_line) { &error(1); }
	}
	# ����������
	if ($max_v) {
		$value_size = length($FORM{'value'});
		if ($value_size > $max_v)  { &error(1); }
	}
	


# �v���e�N�g�R�[�h�`�F�b�N
	if ( $FORM{'protect'} ne '' ) {
		local ( $ptime ) = time + $tim * 60 * 60;
		local ( $pcheck ) = ( $FORM{'protect'} - $protect_c ) / $protect_b - $protect_a;
		
		( $csec, $cmin, $chour, $cmday, $cmon, $cyear, $cwday, $cyday, $cisdat )
			= localtime ( $pcheck );
		$cyear += 1900;
		$cmon++;
		local ( $cnowdate ) = sprintf ( "%d/%02d/%02d(%s)%02d��%02d��%02d�b", 
			$cyear, $cmon, $cmday, 
			( '��', '��', '��', '��', '��', '��', '�y' )[$cwday],
			$chour, $cmin, $csec );
		if ( 
		  ( $csec  < 0 ) || ( $csec  > 60 ) ||
		  ( $cmin  < 0 ) || ( $cmin  > 60 ) ||
		  ( $chour < 0 ) || ( $chour > 24 ) ||
		  ( ( $ptime - $pcheck ) > 1 * 60 * 60 ) ) {	# �P����
			&error ( 'xxx' );
		}
	} else {
		&error ( 'xxx' );
	}
	
	# �ߋ����O�̃t�@�C���T�C�Y�`�F�b�N
	if ( ( -s $filedate ) > $maxoldlogsize ) {
		&error (0);
	}
	
	# ���e�Җ��`�F�b�N
	$formname = $FORM{'name'};
#	if ($formname eq "$nameng"){ &error(xx); }
	if ($formname eq "$pass"){$formname = $namez; $FORM{'email'} = $mailadd;}
	else {
		$formname =~ s/$namez/<small>����<\/small>/g;
#		$formname =~ s/����/���́K/g;
	}
	
# �L�^�t�@�C����ǂݏo���I�[�v�����āA�z��<@lines>�Ɋi�[����
	open (DB,"+<$file") || &error (0);
	eval 'flock (DB, 2)';
	@lines = <DB>;
	
	# �ő�ێ��L�^���̏���
	$i = 0;
	foreach $line (@lines) {
		$i++;
		if ($i == $max) { last; }
		push(@new,$line);
	}

	# �A��������e�������݃`�F�b�N
	$i = 0; $j = 0;
	while ( ( $i < $check ) && ($j == 0) ) {
		($date0,$name0,$email0,$value0,$subject0,$hpage0,$himage0,$id0) = split(/\,/,$lines[$i]);
		if ( $FORM{'value'} eq $value0 ) { $j = 1; }
#	if ( $FORM{'image'} eq $himage0 ) { $j = 1; }
#		if (substr($FORM{'value'},0,$checklength) eq substr($value0,0,$checklength)){ $j = 1; }
#		if (substr($FORM{'value'},1-$checklength,$checklength) eq substr($value0,1-$checklength,$checklength)) { $j = 1; }
		$i++;
	}

	# ID����
	if ( $lines[0] =~ /^.*,.*,.*,.*,.*,.*,.*,.*,(.*),.*,.*\n/ ) {
		$postid = $1 + 1;
	} else {
		$postid = 1;
	}

$postid_now=$postid ;

		if ( $j == 1) { &error(0); }


	if ( $j == 0 ) {
		$value = "$date_now\,$formname\,$FORM{'email'}\,$FORM{'value'}\,$FORM{'subject'}\,$FORM{'page'}\,$FORM{'image'},$FORM{'code'},$postid,$FORM{'area'},$FORM{'areaname'}\n";

		unshift(@new,$value);
		
    seek (DB, 0, 0);
    truncate (DB, 0);
    print DB @new;
    eval 'flock (DB, 8)';
    close (DB);

	
# �ŐV���e�t�@�C���o��
########################
$emax=300;

# �L�^�t�@�C����ǂݏo���I�[�v�����āA�z��<@lines>�Ɋi�[����
	open (DB,"+<$readfile") || &error (0);
	eval 'flock (DB, 2)';
	@lines = <DB>;

	# �ő�ێ��L�^���̏���
	$i = 0;
	foreach $line (@lines) {

($date,$name,$email,$value,$subject,$hpage,$himage,$code,$postid,$area) = split(/\,/,$line);

		$i++;
		if ($i == $emax) { last; }
	    if ($FORM{'area'} eq $area ){ $del = 1; }
		if ($del == 0) { push(@neo,$line);}
		$del = 0; 
	}

		$val = "$date_now\,$formname\,$FORM{'email'}\,$FORM{'value'}\,$FORM{'subject'}\,$FORM{'page'}\,$FORM{'image'},$FORM{'code'},$postid_now,$FORM{'area'},$FORM{'areaname'}\n";

	unshift(@neo,$val);
		
    seek (DB, 0, 0);
    truncate (DB, 0);
    print DB @neo;
    eval 'flock (DB, 8)';
    close (DB);



# �ߋ����O�o��
########################
		$FORM{'value'} =~ s/\0/\,/g;
		open(LOG,">>$filedate") || &error(0);
		eval 'flock (LOG, 2)';


if (-z LOG) {
	# �t�@�C������̏ꍇ��HTML�w�b�_��t����
	print LOG "<html>\n<body bgcolor=\"#$bgc\" text=\"#$textc\" link=\"#$linkc\" vlink=\"#$vlinkc\" alink=\"#$alinkc\">\n<hr>";

# �ۑ���T�����߂����ߋ����O�t�@�C���͍폜
	( $oldsec, $oldmin, $oldhour, $oldmday, $oldmonth, $oldyear, $oldwday, $oldyday, $oldisdst )
  = localtime ( time + $tim - 10 * 60 * 60 * 24 );
$oldmonth += 1;
$oldlogfilename = sprintf ( "%s%d%02d%02d%s", $logfile, $oldyear, $oldmonth, $oldmday, $logfiledat );
	unlink $oldlogfilename;
}

		print LOG "<font size=+1 color=\"#$subjc\"><b>$FORM{'subject'}</b></font>";
		# ���[���A�h���X���L�^����Ă���f�[�^�ɂ̓����N��t����
		if ($FORM{'email'} ne '') { print LOG "�@���e�ҁF<b><a href=\"mailto:$FORM{'email'}\">$formname</a></b>\n"; }
		else { print LOG "�@���e�ҁF<font color=\"#$subjc\"><b>$formname</b></font>\n"; }

		print LOG "<font size=-1>�@���e���F$date_now";

	if ($FORM{'area'}  ne '') { print LOG "�@<a href=\"$cgiurl2\?area=$FORM{'area'}\" target=\"link\">$FORM{'area'}</a></font><p>\n"; }

if ($FORM{image} eq '1') {

    $FORM{'value'} =~ s!((https?|ftp|gopher|telnet|whois|news):(=\S+|[\x21-\x7f])+)!<a href="$1" target="$link">$1</a>!ig;
}


		print LOG "<blockquote><pre>$FORM{'value'}</pre><p>\n\n";
		
		# �t�q�k���L�^����Ă���f�[�^�ɂ̓����N��t����
		if ($FORM{'page'} ne '') {
			$page0 = $FORM{'page'};
			$page0 =~ s/$cgiurl\?action=search1\&search=(.*)\&id=\d*/�Q�l�F$1/;
			if ( $FORM{'page'} eq $page0 ) {
				print LOG "<a href=\"$FORM{'page'}\" target=\"jump\">$page0</a><p>\n";
			} else {
				print LOG "<font color=\"#$linkc\"><u>$page0</u></font><p>\n";
			}
		}
		print LOG "</blockquote>\n<hr>";
		
		eval 'flock (LOG, 8)';
		close(LOG);
		
#		if (!open(BD,">>./0000.txt")) {error(0); }
#		print BD "$date_now\,$FORM{'subject'}\,$host\n";
#		while ( ($a,$b) = each %ENV) {print BD "$a=$b\,";}
#		print BD "\n";
#		close(BD);
	
	} else {
		eval 'flock (LOG, 8)';
		close(LOG);
	}

	
	# �L�^������A�ēǂݍ��݂���
	if ( $FORM{'def'} eq "0" ) { &read; }
	elsif ( $FORM{'follow'} ne "on" ){ &html; }
	else {
		print "Content-type: text/html\n\n";
		print "<html><head><title>�������݊���</title></head>\n";
		print "$body\n";
		print "<h1>�������݊���</h1><font size=-1 color=$bgc> $FORM{'win_count'} - $FORM{'win_time'} �A$win_time0 - $win_count0</font>\n";
		exit;
	}
#	print "Location: $cgiurl" . '?' . "\n\n";
#	exit;
}

# �t�H���[���e�T�u���[�`���isearch1�j ############################################
sub search1 {

	#--- ���̓t�H�[����� --------------------------------#

	print "Content-type: text/html\n\n";
	print "<html><head><title>$FORM{search}�ɕԐM</title></head>\n";
	print "$body\n";

	# �o�i�[�͂���

	#--- �L�^�L���̏o�� ----------------------------------#

	# �L�^�t�@�C����ǂݏo���I�[�v�����āA�z��<@lines>�Ɋi�[����
	if (!open(DB,"$file")) { &error(0); }
	@lines = <DB>;
	close(DB);

	$accesses = @lines;
	$f = 0; $i = 0;
	while (($f == 0) && ($i < $accesses)){

		# �f�[�^���e�ϐ��ɑ������
		($date,$name,$email,$value,$subject,$hpage,$himage,$code,$postid) = split(/\,/,$lines[$i]);
		chop ($postid) if $postid =~ /\n/;
		if ($postid eq $FORM{id}) { $f = 1;}
		$i++;
	}
	
	if ($f == 1){
		$value =~ s/\0/\,/g; # �k���R�[�h�ɕϊ��L�^�������p�J���}�𕜋A������
		chop($himage) if $himage =~ /\n/;
		chop($hpage) if $hpage =~ /\n/;
		
		&disp;
		print "<hr>\n";
		
		$value =~ s/\r/\r&gt; /g;
$value =~ s/\r&gt;\s&gt;\s*\r/\r/g;
		$value ="&gt; $value";
		$value =~ s/&gt; &gt; &gt;.*?\r//g; 
		print "<p>\n";



		# �v���e�N�g�L�[����
		local ( $ptime ) = time + $tim * 60 * 60;
		local ( $pkey ) = ( $ptime + $protect_a ) * $protect_b + $protect_c;
		
		print "<form method=$method action=\"$cgiurl\">\n";
		print "<input type=hidden name=\"action\" value=\"$action\">\n";

if ($FORM{'link'} ne '') { $link = $FORM{'link'}; }

	if ($FORM{'link'} ne '_top') { print "<input type=hidden name=\"follow\" value=\"on\">\n"; }
		print "���e�� <input type=text name=\"name\" size=20 maxlength=20><br>";		
		print "���[�� <input type=text name=\"email\" size=30><br>\n";
		print "�薼�@ <input type=text name=\"subject\" size=30 value=\"��$name\">  \n";
		print "<input type=submit value=\"  ���e  \"><input type=reset value=\"����\"><p>\n";	


		print "<input type=hidden name=\"def\" value=\"$defnext\">\n";
#print "<input type=hidden name=\"image\" value=\"$acid\">\n";
		print "<input type=hidden name=\"link\" value=\"$FORM{link} \">\n";
		
		# �v���e�N�g�R�[�h�o��
		print "<input type=hidden name=\"protect\" value=\"$pkey\">\n";
		
		print "���e<i>�i�^�O�͎g���܂���B\n";
		print "���e���������ɓ��e�{�^���������ƃ����[�h���܂��B�j</i><br>\n";
		
		print "<textarea name=\"value\" rows=5 cols=70>$value\r";
		
		print "</textarea><p>\n";



		if ($himage ne '1') { 	print "URL���������N<input type=checkbox name=\"image\" value=\"1\"></font> \n";}
else{
	print "URL���������N<input type=checkbox name=\"image\" value=\"1\" checked></font> \n";}



	print "<input type=hidden name=\"area\" value=\"$FORM{area}\">\n";
	print "<input type=hidden name=\"areaname\" value=\"$title\">\n";


		print "<input type=hidden name=\"code\" value=\"$code\">\n";
		print "<input type=hidden name=\"page\" size=70 value=\"$cgiurl\?action\=search1\&search\=$date\&id=$postid\">\n";
		print "<input type=hidden name=\"bgcolor\" value=\"$bgc\"></form><p>\n";	}
	else { print "�݂���܂���<br>";}
	
	print "<hr></body></html>\n";
	exit;
}




# ���e�Җ��T�[�`�p�T�u���[�`���isearch2�j ############################################
sub search2 {

	print "Content-type: text/html\n\n";
	print "<html><head><title>$FORM{search}�̓��e�ꗗ</title></head>\n";
	print "$body\n";

	# �o�i�[�͂���

	#--- �L�^�L���̏o�� ----------------------------------#

	# �L�^�t�@�C����ǂݏo���I�[�v�����āA�z��<@lines>�Ɋi�[����
	if (!open(DB,"$file")) { &error(0); }
	@lines = <DB>;
	close(DB);

	$accesses = @lines;
	$f = 0;
	foreach ( @lines ){
		# �f�[�^���e�ϐ��ɑ������
		($date,$name,$email,$value,$subject,$hpage,$himage,$code,$postid) = split(/\,/,$_);
		if ( $name eq $FORM{search} ) {
			$f = 1;
			$value =~ s/\0/\,/g; # �k���R�[�h�ɕϊ��L�^�������p�J���}�𕜋A������
			chop($himage) if $himage =~ /\n/;
			chop($hpage) if $hpage =~ /\n/;
			&disp;
		}
	}

	if ($f == 0){ print "�݂���܂���<br>";}

	print "<hr></body></html>\n";
	exit;
}

# �g�s�b�N�T�[�`�p�T�u���[�`���isearch3�j ############################################
sub search3 {


	print "Content-type: text/html\n\n";
	print "<html><head><title>�X���b�h�ꗗ</title></head>\n";
	print "$body\n";

	#--- �L�^�L���̏o�� ----------------------------------#

	# �L�^�t�@�C����ǂݏo���I�[�v�����āA�z��<@lines>�Ɋi�[����
	if (!open(DB,"$file")) { &error(0); }
	@lines = <DB>;
	close(DB);

	$accesses = @lines;
	$f = 0;
	foreach ( @lines ){
		# �f�[�^���e�ϐ��ɑ������
		($date,$name,$email,$value,$subject,$hpage,$himage,$code,$postid) = split(/\,/,$_);

		if ( $code eq $FORM{search} ) {
			$f = 1;
			$value =~ s/\0/\,/g; # �k���R�[�h�ɕϊ��L�^�������p�J���}�𕜋A������
			chop($himage) if $himage =~ /\n/;
			chop($hpage) if $hpage =~ /\n/;
			&disp;
		}
	}

	if ($f == 0){ print "�݂���܂���<br>";}

	print "<hr></body></html>\n";
	exit;
}
# �g�b�v�y�[�W�\���p�T�u���[�`���ilist�j ############################################
sub list {

	print "Content-type: text/html\n\n";
	print "<html><head><title>$title</title></head>\n";
	print "$body\n";

		local ( $ptime ) = time + $tim * 60 * 60;
		local ( $pkey ) = ( $ptime + $protect_a ) * $protect_b + $protect_c;
		

#print "<b>�ŐV�A��(6/23)</b><p><font size=-1>���O�̑��ۑ�������1200���ɕύX�B<br>�Ȃ��A�������܌f������ύ��ݍ����Ă��邽�߁A�ǂ���<a href=\"http://kakumeigun.virtualave.net/cgi-bin/remix/bbs.cgi\" >REMIX���v���R</a>�̕����䗘�p�ɂȂ��Ă��������B</font><hr>\n";



print "<font color=ffffff size=+1><b>$title</b></font>�@<font size=-1><b><a href=\"$cgiurl\?bgcolor\=$bgc\&$\area\=read\">�ŐV���e�ꗗ</a></font></b>�@<font size=-1><b><a href=\"list.cgi\">�V�K�f���쐬</a></b></font><p>
\n";

	print "<form method=post action=\"$cgiurl\">\n";
	print "�\\������\n";
	print "<input type=text name=\"def\" size=8 value=\"$defnext\">\n";
	print "�o�b�N�O���E���h�J���[<input type=text name=\"bgcolor\" size=8 value=\"$bgc\"><input type=hidden name=\"link\" value=\"$FORM{'link'}\">�@<input type=submit value=\"�@�����[�h�@\">\n";

	print "<hr><font size=-1>�����̍D���ȃe�[�}�̌f�������܂��B�e�f���͍Ō�ɓ��e�̂��������t���̏���\�\\������܂��B�쐬���Ă����e���Ȃ���\�\\������܂���B�f���Ⓤ�e�̍폜�͈�؂ł��Ȃ��̂ŁA�S�Ă̍s���͎��ȐӔC�ōs���Ă��������B�ߋ����O��<a href=\"getlog_m.cgi\">����</a>�B\n";



	if ( $countlevel > 0 ){
		print "$countdate���� ";
		&counter; print "$countplus�i�����ɂ������x��$countlevel�j\n";
}

	print "<hr>\<a href=\"http://AG.ST2.ARENA.NE.JP/cgi-bin/strangeworld/bbs.cgi\">��������</a>�b<a href=\"http://ch.st6.arena.ne.jp/cgi-bin/strangeworld/bbs/bbs.cgi\">�킩��</a>�b<a href=\"http://extra.tomato.nu/strangeworld/\">�G�N�X�g��</a>
�b<a href=\"http://www.njs.ne.jp/~rebirth/remix/bbs.cgi\">REMIX</a>�b<A href=\"http://members.tripod.com/~swattylink/\">SwattyLink</A> /
<A href=\"http://swatty.virtualave.net/cgi-bin/upload.cgi\">File</a>|<a href=\"http://edoya.neko.to/2/upload.cgi\">���E��Y</a>�b<a href=\"http://strange-empire.virtualave.net/cgi-bin/upload.cgi\">�p�j����[</a>�b<a href=\"http://wave.ruru.ne.jp/loplop/erunst/chat.cgi\">�`���b�g</a><hr></form>\n";
print "<ul>\n";
	
	#--- �L�^�L���̏o�� ----------------------------------#
	
	# �L�^�t�@�C����ǂݏo���I�[�v�����āA�z��<@lines>�Ɋi�[����
	if (!open(DB,"$readfile")) { &error(0); }
	@lines = <DB>;
	close(DB);
	
	if ($FORM{'page'} eq '') { $page = 0; } else { $page = $FORM{'page'}; }
	
	$accesses = @lines; $accesses--;
	$page_end = $page + $def - 1;
	if ($page_end > $accesses) { $page_end = $accesses; }

	foreach ($page .. $page_end) {
		($date,$name,$email,$value,$subject,$hpage,$himage,$code,$postid,$area,$areaname) = split(/\,/,$lines[$_]);
		$value =~ s/\0/\,/g; # �k���R�[�h�ɕϊ��L�^�������p�J���}�𕜋A������
		chop($himage) if $himage =~ /\n/;
		chop($hpage) if $hpage =~ /\n/;
		chop($postid) if $postid =~ /\n/;
	if ($postid > 120) { $postid  = 120; }

	print "</font><font size=-1><li><a href=\"$cgiurl\?$\area\=$area\">$areaname</a></font><br><font size=-1 color=007f7f>$postid���̃��b�Z�[�W������܂��@�ŏI���e���F$date</li>\n";
	}
	
	#--- ���y�[�W���� ------------------------------------#
	
	print "</form></ul></font><hr><p>\n";
	$page_next = $page_end + 1;
	$i = $page + 1; $j = $page_end + 1;
	if ($page_end ne $accesses) {
		print "<font size=-1><i>�ȏ�́A���ݓo�^����Ă���V����$i�Ԗڂ���$j�Ԗڂ܂ł̋L���ł��B</i></font><p>\n";
		print "<form method=$method action=\"$cgiurl\">\n";
		print "<input type=hidden name=\"page\" value=\"$page_next\">\n";
		print "<input type=hidden name=\"def\" value=\"$def\">\n";
		print "<input type=hidden name=\"bgcolor\" value=\"$bgc\">\n";
		print "<input type=submit value=\"���̃y�[�W\"></form>\n";
	}
	else {
	
		print "<font size=-1><i>�ȏ�́A���ݓo�^����Ă���V����$i�Ԗڂ���$j�Ԗڂ܂ł̋L���ł��B";
		print "����ȉ��̋L���͂���܂���B</i></font>\n";
	}
	
	# ���̃X�N���v�g�̒��쌠�\���i���Ȃ炸�\�����Ă��������j

		print "<form method=$method action=\"$cgiurl\"><input type=hidden name=\"def\" value=\"$def\"><input type=hidden name=\"bgcolor\" value=\"$bgc\"><input type=submit value=\"�@�����[�h�@\"></form>\n";
	print "<h4 align=right><hr size=5><a href=\"http://www.ask.or.jp/~rescue/\">MiniBBS v7.5</a> <a href=\"http://www.bea.hi-ho.ne.jp/strangeworld/recycle/\">REQUIEM 990707��</a> is Free.<br></h4>\n";
	print "</body></html>\n";
	exit;
}


# ���O�ǂݗp�T�u���[�`��(logread)
###################################################

sub read{
if ($FORM{'area'} eq '') { $area = $title; }
if ($FORM{'bgcolor'} ne '') { $bgc = $FORM{'bgcolor'}; }
$body  = "<body bgcolor=\"#$bgc\" text=\"#$textc\" link=\"#$linkc\" vlink=\"#$vlinkc\" alink=\"#$alinkc\">";

if ($FORM{'area'} ne '') { $area = $FORM{'area'}; }
if ($FORM{'search'} ne '') { $area = $FORM{'search'}; }

#if ($FORM{'def'} ne '') { $def = $FORM{'def'}; }
#if ($def < $defmin) { $def = $defmin;}
#$defnext = $def;
#if ($defnext > $defmax) {$defnext = $defmax;}

	print "Content-type: text/html\n\n";
	print "<html><head><title>���₵����[���REFLEX�@�ŐV���e�ꗗ</title></head>\n";
	print "$body\n";

		local ( $ptime ) = time + $tim * 60 * 60;
		local ( $pkey ) = ( $ptime + $protect_a ) * $protect_b + $protect_c;
		


print "<font color=ffffff size=+1><b>���₵����[���REFLEX�@�ŐV���e�ꗗ</b></font>�@<font size=-1><b><a href=\"$cgiurl\?bgcolor\=$bgc\">���X�g�ꗗ</a></font></b>�@<font size=-1><b><a href=\"list.cgi\">�V�K�f���쐬</a></b></font>
\n";
	print "<form method=POST action=\"$cgiurl\">\n";
	print "�\\������\n";
	print "<input type=text name=\"def\" size=8 value=\"$defnext\">\n";
	print "�o�b�N�O���E���h�J���[<input type=text name=\"bgcolor\" size=8 value=\"$bgc\">�@<input type=submit value=\"�@�����[�h�@\"><input type=hidden name=\"link\" value=\"$FORM{'link'}\">\n";

	print "<input type=hidden name=\"link\" value=\"\" $checked1><input type=hidden name=\"link\" value=\"2\" $checked2><input type=hidden name=\"link\" value=\"3\" $checked3></font>\n"; 

	print "<input type=hidden name=\"area\" value=\"\"><br><font size=-1>\n";

#	 �J�E���^
	if ( $countlevel > 0 ){
		print "$countdate���� ";
		&counter; print "$countplus�i�����ɂ������x��$countlevel�j</font>�@\n";
	print "<form method=$method action=\"$cgiurl\">\n";
	print "<input type=hidden name=\"area\" value=\"$FORM{'area'}\">\n";
	print "<hr>
<font size=-1>�ߋ����O��<a href=\"./getlog_m.cgi\" target=\"_top\">����</a>�B\n";
	print "<input type=hidden name=\"image\" value=\"0\">\n";



	# �v���e�N�g�R�[�h�o��
	print "<input type=hidden name=\"protect\" value=\"$pkey\">\n";
	
	

	print "<font size=-1>\n";
#	print "<hr><i>�V�����L������\\�����܂��B�ō�$max���̋L�����L�^����A����𒴂���ƌÂ��L������폜����܂��B<br>\n";
#	print "�P��̕\\����$def�����z����ꍇ�́A���̃{�^�����������ƂŎ��̉�ʂ̋L����\\�����܂��B</i>\n";
	
#	 �T�[�`�̒��ӏ���
	print "�e�f���̍ŐV�̓��e���ǂ߂܂��B<br>���e�̍폜�͈�؂��Ȃ��̂ŁA�S�Ă̍s���͎��ȐӔC�ōs���Ă��������B<br>���F�ԐM�t�H�[���@���F�����T�[�`�@���F�X���b�h�ꗗ\n";

	print "<hr>\<a href=\"http://AG.ST2.ARENA.NE.JP/cgi-bin/strangeworld/bbs.cgi\">��������</a>�b<a href=\"http://ch.st6.arena.ne.jp/cgi-bin/strangeworld/bbs/bbs.cgi\">�킩��</a>�b<a href=\"http://extra.tomato.nu/strangeworld/\">�G�N�X�g��</a>
�b<a href=\"http://www.njs.ne.jp/~rebirth/remix/bbs.cgi\">REMIX</a>�b<A href=\"http://members.tripod.com/~swattylink/\">SwattyLink</A> /
<A href=\"http://swatty.virtualave.net/cgi-bin/upload.cgi\">File</a>|<a href=\"http://edoya.neko.to/2/upload.cgi\">���E��Y</a>�b<a href=\"http://strange-empire.virtualave.net/cgi-bin/upload.cgi\">�p�j����[</a>�b<a href=\"http://wave.ruru.ne.jp/loplop/erunst/chat.cgi\">�`���b�g</a><hr>\n";
	}

#	�����[�h
print "<p></font></font></font><input type=submit value=\"�@�����[�h�@\">\n";
	print "</form>\n";





	# �o�i�[�͂���

	
	#--- �L�^�L���̏o�� ----------------------------------#
	
	# �L�^�t�@�C����ǂݏo���I�[�v�����āA�z��<@lines>�Ɋi�[����
	if (!open(DB,"$readfile")) { &error(0); }
	@lines = <DB>;
	close(DB);
	
	if ($FORM{'page'} eq '') { $page = 0; } else { $page = $FORM{'page'}; }
	
	$accesses = @lines; $accesses--;
	$page_end = $page + $def - 1;
	if ($page_end > $accesses) { $page_end = $accesses; }

	foreach ($page .. $page_end) {
		($date,$name,$email,$value,$subject,$hpage,$himage,$code,$postid,$area,$areaname) = split(/\,/,$lines[$_]);
		$value =~ s/\0/\,/g; # �k���R�[�h�ɕϊ��L�^�������p�J���}�𕜋A������
		chop($himage) if $himage =~ /\n/;
		chop($hpage) if $hpage =~ /\n/;
		chop($postid) if $postid =~ /\n/;
		&disp;
	}
	
	#--- ���y�[�W���� ------------------------------------#
	
	print "</form><hr><p>\n";
	$page_next = $page_end + 1;
	$i = $page + 1; $j = $page_end + 1;
	if ($page_end ne $accesses) {
		print "<font size=-1><i>�ȏ�́A���ݓo�^����Ă���V����$i�Ԗڂ���$j�Ԗڂ܂ł̋L���ł��B</i></font><p>\n";
		print "<form method=$method action=\"$cgiurl\?area\=$FORM{area}\">\n";
		print "<input type=hidden name=\"page\" value=\"$page_next\">\n";
		print "<input type=hidden name=\"def\" value=\"$def\">\n";
		print "<input type=hidden name=\"bgcolor\" value=\"$bgc\">\n";
		print "<input type=hidden name=\"area\" value=\"read\">\n";
		print "<input type=submit value=\"���̃y�[�W\"></form>\n";
	}
	else {
	
		print "<font size=-1><i>�ȏ�́A���ݓo�^����Ă���V����$i�Ԗڂ���$j�Ԗڂ܂ł̋L���ł��B";
		print "����ȉ��̋L���͂���܂���B</i></font>\n";
	}
	
	# ���̃X�N���v�g�̒��쌠�\���i���Ȃ炸�\�����Ă��������j
	print "</font><h4 align=right><hr size=5><a href=\"http://www.ask.or.jp/~rescue/\" target=\"$link\">MiniBBS v7.5</a> <a href=\"http://www.bea.hi-ho.ne.jp/~strangeworld/remix/\" target=\"$link\">REMIX 991004</a> is Free.</h4>\n";
	print "</body></html>\n";
	exit;
}


# �e�ݒ�ǂݍ��ݗp�T�u���[�`�� #############################################################
sub select {

$ssij="./pref/bbb.dat";
$ssij =~ s/bbb/$FORM{'area'}/g;

	if (!open(DB,"$ssij")) { &error(0); }
	@lines = <DB>;
	close(DB);
	foreach ( @lines ){
		# �f�[�^���e�ϐ��ɑ������
($area,$passd,$title,$rmode,$wmode,$bgc,$textc,$linkc,$vlinkc,$subjc,$bimage) = split(/:#/,$_);
last; 
	}
$file="./data/bbb.dat";
$file =~ s/bbb/$FORM{'area'}/g;

# �J�E���^�t�@�C���̐擪�����E�g���q�̎w��

$countfile="./counters/eee";
$countfile=~ s/eee/$FORM{'area'}/g;

	if ($bimage eq "" || $bimage eq "http://") { $bimage = ''; }
	else{
		$bimage =~ s/\s//g;$bimage =~ s/\"//g;$bimage =~ s/\'//g;
		$bimage =~ s/http\:\/\/http\:\/\//http\:\/\//g;
	}

if ($FORM{'bgcolor'} ne '') { $bgc = $FORM{'bgcolor'}; }
$body  = "<body bgcolor=\"#$bgc\" text=\"#$textc\" link=\"#$linkc\" vlink=\"#$vlinkc\" alink=\"#$alinkc\" background=\"$bimage\">";

}


# �e���e�\���p�T�u���[�`�� #############################################################
sub disp {

	$hpage0 =$hpage;
	$hpage0 =~ s/$cgiurl\?action=search1\&search=(.*)\&id=\d*/�Q�l�F$1/;
	print "<hr>";
	print "<font size=+1 color=\"#$subjc\"><b>$subject</b></font>�@";
	

	if ($email ne '') { print "���e�ҁF<b><a href=\"mailto:$email\">$name</a></b>\n"; }
	else { print "���e�ҁF<b>$name</b></font>\n"; }

		print "<font size=-1>�@���e���F$date";

	print "�@<a href=\"$cgiurl\?bgcolor\=$bgc\&action\=search1\&search\=$date\&id=$postid&area=$area\" target=\"link\">��</a>";
	print "�@<a href=\"$cgiurl\?bgcolor\=$bgc\&action\=search2\&search\=$name&area=$area\" target=\"link\">��</a>";
	if ($hpage ne'' ) { print "�@<a href=\"$cgiurl\?bgcolor\=$bgc\&action\=search3\&search\=$code&area=$area\" target=\"link\">��</a>\n"; }

if ($FORM{'area'}  eq 'read') { print "�@<a href=\"$cgiurl\?area\=$area\" target=\"$link\">$areaname</a>\n"; }
	print "</font><p>\n";

if (($FORM{search}  eq '') && ($himage eq '1') ){
    $value =~ s!((https?|ftp|gopher|telnet|whois|news):(=\S+|[\x21-\x7f])+)!<a href="$1" target="link">$1</a>!ig;

}


	print "<blockquote><pre>$value</pre><p>\n\n";
	
	if ($hpage ne '') { print "<a href=\"$hpage\" target=\"link\">$hpage0</a><p>\n"; }
	
	print "</blockquote>\n";
}



# �G���[�����T�u���[�`�� ############################################################
sub error {
	
	#  &error(xx); �ŌĂяo���ꂽ���[�`���́A()���̐����� $error �ɑ�������B
	
	$error = $_[0];
	
	if    ($error eq "0") { $error_msg = '�L�^�t�@�C���̓��o�͂ɃG���[���������܂����B'; }
	elsif ($error eq "2") {	$error_msg = '���e��������Ă��܂���B�܂��͋L�^�֎~�̃^�O��������Ă��܂��B'; }
	elsif ($error eq "3") {	$error_msg = '���[���A�h���X�����������͂���Ă��܂���B'; }
	elsif ($error eq "4") {	$error_msg = '���[���A�h���X�͕����w��ł��܂���B'; }
	elsif ($error eq "5") {	$error_msg = '���e���e���傫�����܂��B'; }

	elsif ($error eq "6") {	$error_msg = '�A�N�Z�X�����ݍ����Ă邽�߁A�������݂ł��܂���ł����B������x�A���e�{�^���������Ă��������B'; }
	elsif ($error eq "form") { $error_msg = "���e��ʂ̂t�q�k��<br>$cgiurl<br>" . '�ȊO����̓��e�͂ł��܂���B'; }
	elsif ($error eq "x") {	$error_msg = "�ȉ��̏�񂪋L�^����܂����B����"; }
	elsif ($error eq "xx") { $error_msg = "���킢����"; }
	elsif ($error eq 'xxx') { $error_msg = ' '; }
	
	print "Content-type: text/html\n\n";
	print "<html><head><title>$title</title></head>\n";
	print "$body\n";
	print "<h3>$error_msg</h3>\n";


	print "</body></html>\n";
	exit;
}

# �J�E���^�[�����T�u���[�`�� #########################################################
sub counter {

	for( $i=0 ; $i < $countlevel ; $i++){
		open(IN,"$countfile$i$countfiledat");
		$count[$i] = <IN>;
		$filenumber[$count[$i]] = $i;
		close(IN);
	}
	@sortedcount = sort by_number @count;
	$maxcount = $sortedcount[$countlevel-1];
	$mincount = $sortedcount[0];

	$maxcount++;
	print $maxcount;

	open(OUT,">$countfile$filenumber[$mincount]$countfiledat");
	print OUT $maxcount;
	close(OUT);
}

sub by_number {
	$a <=> $b;
}

#end_of_script
