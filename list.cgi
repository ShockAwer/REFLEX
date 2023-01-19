#! /usr/bin/perl
#
#ゆいぽすと1.1(list.cgi)
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
$youbi = ('日','月','火','水','木','金','土') [$wday];
$date = "$month月$mday日（$youbi）$hour時$min分$sec秒";
$today = "$month/$mday";
$chat_file = './den/log.000.dat';
$roommax = 300;#設置できる最大の私書箱数
$cgidir = 'http://www.plumfield.ne.jp/~neu/reflex/yuipost/';#postというディレクトリ内にCGIを置く場合
if ($ENV{'REQUEST_METHOD'} eq "POST") { read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'}); }
else { $buffer = $ENV{'QUERY_STRING'}; }
}#init END
##################################################
sub html {
print "Content-type: text/html\n\n";
print <<"_HTML_";
<HTML><HEAD><TITLE>あやしいわーるどREFLEX 新規掲示板作成</TITLE></HEAD>
<BODY bgcolor="#004040" text="#ffffff" link="#eeffee" vlink="#dddddd" alink="#ff0000">

_HTML_



print <<"_HTML_";
</ul>
<FONT size=+1><B><A NAME="make">あやしいわーるどREFLEX 新規掲示板作成</A></B></FONT>　<font size=-1><b><a href=\"bbs.cgi\">リスト一覧</a></font></b>　<font size=-1><b><a href=\"bbs.cgi\?area\=read\">最新投稿一覧</a></b></font><BR><p>
<FORM method="GET" ACTION="./list.cgi"><INPUT TYPE=hidden NAME="make" value="on">
タイトル　 <INPUT TYPE=text NAME="title" SIZE="30"><BR>
ID　　　　 <INPUT TYPE=text NAME="id" SIZE="7">(半角英数字を必ず記入)<BR>
パスワード <INPUT TYPE=text NAME="pass" SIZE="7">(半角英数字を必ず記入)<p>
背景色　　 　<INPUT TYPE=text NAME="bgcolor" SIZE="7" VALUE="004040"><BR>
文字色 　　　<INPUT TYPE=text NAME="mgcolor" SIZE="7" VALUE="ffffff"><BR>
リンク色 　　<INPUT TYPE=text NAME="lkcolor" SIZE="7" VALUE="eeffee">
<br>
既読リンク色 <input type=text name="vlinkcolor" size=7 value="dddddd"><br>
題名色 　　　<input type=text name="sbcolor" size=7 value="ffffee"><br>
背景画像 　　<input type=text name="backimage" size=30 value="http://">
<p>
<INPUT type=submit value="新規作成／設定変更"></FORM><hr><font size=-1>
設定を変更するときには、IDとパスワードは前と同じものを使用してください。<br>
</font><hr>

<H5 align=right><A HREF="http://www.cup.com/yui/index.html">ゆいぽすと(Free)</A></H5></BODY></HTML>
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
sub make {#新規話題ルームを設置
#タイトルチェック。
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


chmod 0600, "./pref/$id.dat";#0666でないとダメかも。
chmod 0666, "./data/$id.dat";#0666でないとダメかも。

$buffer=~s/&title=/&name2=/;
&locate;
}#make END
#################################################
sub locate{	#移動します。

print "Content-type: text/html\n\n";
print <<"_HTML_";
<HTML><HEAD><TITLE>$title</TITLE>
</HEAD><BODY bgcolor="#004040" text="#ffffff" link="#eeffee" vlink="#dddddd" alink="#ff0000">
<H1>
作成完了。</H1>
<HR><BR>
<a href="bbs.cgi?area=$id">
こちらに移動します。</a><BR>何か投稿をするとリストに追加されます。<BR>
<BR><BR><BR><BR><BR>
<H5 ALIGN=right><A HREF="http://www.cup.com/yui/index.html">ゆいぽすと(Free)</A></H5></BODY></HTML>
_HTML_
exit;
}#make END

#################################################


sub getcookie{	#くっきーを頂きます。
	$cooks = $ENV{'HTTP_COOKIE'};
	$cooks = '' unless($cooks =~s/.*yuipost=(.*)yuipostend.*/$1/) ;
	($hotlist,$rev,$lmax) = split(/\t/, $cooks);
}#getcookie END

sub setcookie{	#くっきーをブラウザにプレゼントします。
	$data = "$hotlist\t$rev\t$lmax\tyuipostend";
	print "Set-Cookie: yuipost=$data; expires=Wednesday, 09-Nov-1999 00:00:00 GMT\n" unless ($ENV{'HTTP_COOKIE'}=~/$data/);
}#このクッキーは1999/11/9まで有効です。それを過ぎたら、日付をもっと先にして。
sub err{
$error = $_[0];
print "Content-type: text/html\n\n";
print <<"_HTML_";
<HTML><HEAD><TITLE>$title</TITLE>
</HEAD><BODY BGCOLOR="#A1FE9F" TEXT="#000000" LINK="#ff0000" VLINK="#ff0000" ALINK="#FF0000">
<H1>
タイプ $error のエラーが発生しました。</H1>
<HR><BR>
エラータイプの説明<BR><BR>
タイプ0：ログファイルが開けません。<BR>
タイプ1：私書箱設定の修正時に必要となるパスワードが間違っています。<BR>
タイプ3：私書箱のタイトルが短いです。<BR>
タイプ4：予期せぬエラーです。<BR>
タイプ5：設置数が最大設定値$roommaxを越えるため、新規に設置ができません。<BR>
<BR><BR><BR><BR><BR>
<H5 ALIGN=right><A HREF="http://www.cup.com/yui/index.html">ゆいぽすと(Free)</A></H5></BODY></HTML>
_HTML_
exit;
}
__END__
