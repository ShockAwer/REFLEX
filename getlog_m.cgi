#! /usr/local/bin/perl


#はじあや＠ふぁみーるのパソヲタさん、本当にありがとう


#--------------------

$body = '<body bgcolor="#004040" text="#ffffff" link="#eeffee" vlink="#dddddd" alink="#ff0000">';
$bbstitle ="あやしいわーるどREFLEX";


$logdir = './log/';

$cgiurl = 'getlog_m.cgi';
$action ='getlog';

$bbsurl = './bbs.cgi';

# 日本語コード変換ライブラリjocde.plのパス
require './jcode.pl';

# キーワードの最大文字数（半角）
$keylength = 64;

# 時差 サーバの時計がずれてる時や日本時間以外にしたい時に使う
$tim = 0;

$\ = "\n";
#--------------------
#if ($ENV{'REQUEST_METHOD'} eq "POST") { read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'}); }
#else { $buffer = $ENV{'QUERY_STRING'}; }


$buffer = $ENV{'QUERY_STRING'};


@argv = split(/&/,$buffer);
foreach (@argv) {
	($name, $value) = split(/=/);
	$value =~ tr/+/ /;

	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	&jcode'convert(*value,'sjis');

	$COMMAND{$name} = $value;
}


&error(2) if (length($COMMAND{'keyword'}) > $keylength);
&viewlog if ($COMMAND{'action'} eq "$action");


&list;
	
sub list {

	&error(0) if(!opendir(DIR, $logdir));

	@files=readdir(DIR);
	closedir(DIR);

               @files = sort by_number @files;
               $end = @files;
               $end--; 

	print "Content-type: text/html\n\n";
	print "<html><head><title>$bbstitle 過去ログ</title></head>\n";
	print "$body\n";
	print "<center>\n";
	print "<table border=0 cellpadding=1 cellspacing=1 width=100%><tr>";
	print "<td bgcolor=007f7f align=center><font color=ffffff><b>$bbstitle 過去ログ一覧</b></font></td></tr></table>";
	print "<form method=get action=\"$cgiurl\">";
	print "<input type=hidden name=\"action\" value=\"$action\">";
	print "<table>";
	print "<tr><td></td><td>ファイル名</td><td align=right>サイズ</td><td align=center>日付</td></tr>";
	foreach (0 .. $end) {
		if (!($files[$_] eq "." or $files[$_] eq "..")) {
			($dev,$ino,$mode,$nlink,$uid,$gid,$rdev,$size,$atime,$mtime,$ctime,$blksize,$blocks) = stat "$logdir$files[$_]";
			($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = gmtime($mtime + 32400 + $tim);
			$mon++;
			$mon = "0$mon" if ($mon < 10);
			if ($mday < 10)  { $mday  = "0$mday";  }
			if ($min < 10)  { $min =  "0$min";  }
			if ($hour < 10) { $hour = "0$hour"; }
			$checked = ' checked' if ($_ == $end);
			print "<tr><td><input type=\"radio\" name=\"logfile\" value=\"$files[$_]\"$checked></td>";
			print "<td><a href=\"$logdir$files[$_]\">$files[$_]</a></td>";
			print "<td align=right>$size</td><td align=center>$mon/$mday $hour:$min</td></tr>";
		}
	}

	print "<tr><td></td></tr><tr><td colspan=4>※ラジオボタンでファイル名を指定してください。</td></tr><tr><td></td></tr>\n";
	print "<tr><td colspan=4>日時指定：<select name=\"day1\">";
	print "<option value=\"01\">01";
	print "<option value=\"02\">02";
	print "<option value=\"03\">03";
	print "<option value=\"04\">04";
	print "<option value=\"05\">05";
	print "<option value=\"06\">06";
	print "<option value=\"07\">07";
	print "<option value=\"08\">08";
	print "<option value=\"09\">09";
	print "<option value=\"10\">10";
	print "<option value=\"11\">11";
	print "<option value=\"12\">12";
	print "<option value=\"13\">13";
	print "<option value=\"14\">14";
	print "<option value=\"15\">15";
	print "<option value=\"16\">16";
	print "<option value=\"17\">17";
	print "<option value=\"18\">18";
	print "<option value=\"19\">19";
	print "<option value=\"20\">20";
	print "<option value=\"21\">21";
	print "<option value=\"22\">22";
	print "<option value=\"23\">23";
	print "<option value=\"24\">24";
	print "<option value=\"25\">25";
	print "<option value=\"26\">26";
	print "<option value=\"27\">27";
	print "<option value=\"28\">28";
	print "<option value=\"29\">29";
	print "<option value=\"30\">30";
	print "<option value=\"31\">31";
	print "</select>日<select name=\"hour1\">";
	print "<option value=\"00\">00";
	print "<option value=\"01\">01";
	print "<option value=\"02\">02";
	print "<option value=\"03\">03";
	print "<option value=\"04\">04";
	print "<option value=\"05\">05";
	print "<option value=\"06\">06";
	print "<option value=\"07\">07";
	print "<option value=\"08\">08";
	print "<option value=\"09\">09";
	print "<option value=\"10\">10";
	print "<option value=\"11\">11";
	print "<option value=\"12\">12";
	print "<option value=\"13\">13";
	print "<option value=\"14\">14";
	print "<option value=\"15\">15";
	print "<option value=\"16\">16";
	print "<option value=\"17\">17";
	print "<option value=\"18\">18";
	print "<option value=\"19\">19";
	print "<option value=\"20\">20";
	print "<option value=\"21\">21";
	print "<option value=\"22\">22";
	print "<option value=\"23\">23";
	print "</select>時から";

	print "<select name=\"day2\">";
	print "<option value=\"01\">01";
	print "<option value=\"02\">02";
	print "<option value=\"03\">03";
	print "<option value=\"04\">04";
	print "<option value=\"05\">05";
	print "<option value=\"06\">06";
	print "<option value=\"07\">07";
	print "<option value=\"08\">08";
	print "<option value=\"09\">09";
	print "<option value=\"10\">10";
	print "<option value=\"11\">11";
	print "<option value=\"12\">12";
	print "<option value=\"13\">13";
	print "<option value=\"14\">14";
	print "<option value=\"15\">15";
	print "<option value=\"16\">16";
	print "<option value=\"17\">17";
	print "<option value=\"18\">18";
	print "<option value=\"19\">19";
	print "<option value=\"20\">20";
	print "<option value=\"21\">21";
	print "<option value=\"22\">22";
	print "<option value=\"23\">23";
	print "<option value=\"24\">24";
	print "<option value=\"25\">25";
	print "<option value=\"26\">26";
	print "<option value=\"27\">27";
	print "<option value=\"28\">28";
	print "<option value=\"29\">29";
	print "<option value=\"30\">30";
	print "<option value=\"31\" selected>31";
	print "</select>日<select name=\"hour2\">";
	print "<option value=\"24\">24";
	print "<option value=\"00\">00";
	print "<option value=\"01\">01";
	print "<option value=\"02\">02";
	print "<option value=\"03\">03";
	print "<option value=\"04\">04";
	print "<option value=\"05\">05";
	print "<option value=\"06\">06";
	print "<option value=\"07\">07";
	print "<option value=\"08\">08";
	print "<option value=\"09\">09";
	print "<option value=\"10\">10";
	print "<option value=\"11\">11";
	print "<option value=\"12\">12";
	print "<option value=\"13\">13";
	print "<option value=\"14\">14";
	print "<option value=\"15\">15";
	print "<option value=\"16\">16";
	print "<option value=\"17\">17";
	print "<option value=\"18\">18";
	print "<option value=\"19\">19";
	print "<option value=\"20\">20";
	print "<option value=\"21\">21";
	print "<option value=\"22\">22";
	print "<option value=\"23\">23";
	print "</select>時まで";

	print "</td></tr><br>";
	print " <tr><td colspan=4>　検索　：<select name=\"searchmode\">";
	print "<option value=\"keyword\">全文";
	print "<option value=\"bbs\">掲示板名";
	print "<option value=\"name\">投稿者名";
	print "<option value=\"subject\">題名\n</select>";
	print "<input type=text name=\"keyword\" size=\"24\" maxlength=$keylength></td></tr>";
	print "<tr><td colspan=4 align=center><input type=submit value=\"Get / Search\"></form></td></tr><br>";
	print "</table>";
	print "<hr>";
	print "<p align=center><a href=\"$bbsurl\">掲示板へ</a></p>";
	print "<h4 align=right>Getlog Ver0.3b4 月単位保存ログ対応版</h4>";
	print "</body></html>";
}



sub viewlog {

	if (!open(DB,"$logdir$COMMAND{'logfile'}")) { &error(1); }
	@lines = <DB>;
	close(DB);

	$COMMAND{'last'} = $COMMAND{'first'} + 1 if ($COMMAND{'first'} >= $COMMAND{'last'});
	$first = "$COMMAND{'day1'}日$COMMAND{'hour1'}時";
	$last = "$COMMAND{'day2'}日$COMMAND{'hour2'}時";
	
	if ($COMMAND{'searchmode'} eq 'name') { $keyword = "投稿者：.*>${COMMAND{'keyword'}}<"; }

	elsif ($COMMAND{'searchmode'} eq 'subject') { $keyword = "color=\"#ffffee\"><b>${COMMAND{'keyword'}}</b></font>"; }

	elsif ($COMMAND{'searchmode'} eq 'bbs') { $keyword = "秒　.*>${COMMAND{'keyword'}}<"; }

	else { $keyword = $COMMAND{'keyword'}; }
	if ($keyword ne '') {
		$keyword =~ s/\\/\\\\/;
		$keyword =~ s/\[/\\[/;
	}
	print "Content-type: text/html\n";
	print "<html><head><title>$bbstitle 過去ログ $COMMAND{'logfile'}</title></head>";
	print "$body";
	print "<h1>$COMMAND{'logfile'} $first～$last</h1>";
	$end = @lines;
	$end--;
	foreach (0 .. $end) {
#		MiniBBS7.5あやしいわーるど仕様
		if ($lines[$_] =~ /<font size=-1>　投稿日：/) {
			substr( $hour = substr( $lines[$_], 28, 12 ), 4, 4 ) = "" ;
			last if ($hour ge "$first");
		}
		$skip++;
	}
	$skip--;
#	print"<hr>";
	$\ = '';
	foreach ($skip .. $end) {
#		MiniBBS7.5あやしいわーるど仕様
		if ($lines[$_] =~ /<font size=-1>　投稿日：/) {
			substr( $hour = substr( $lines[$_], 28, 12 ), 4, 4 ) = "" ;

			last if ($hour ge "$last");
		}
		

		if ($keyword ne '') {
			if ($lines[$_] =~ /$keyword/) {
				$flag = 1;
				$hit++; 
			}
			push( @article, $lines[$_] );
			if ($lines[$_] =~ /<\/blockquote>/) {
				print @article if ($flag > 0);  
				splice( @article, 0 );
				$flag = 0;
			}
		}
		else { print $lines[$_]; }

	}
	$\ = "\n";
	if ($COMMAND{'keyword'} ne '') {
		print "<hr>";
		if ( $hit > 0 ) { print "<h3>「$COMMAND{'keyword'}」は $hit件見つかりました。</h3>"; }
		else { print "<h3>「$COMMAND{'keyword'}」は見つかりませんでした。</h3>"; }
	}
	print "</body></html>";

	exit;

}



sub error {

	$error = $_[0];
	if ($error == 0) { $errmsg = 'ディレクトリが開けませんでした。'; }
	if ($error == 1) { $errmsg = 'ファイルが開けませんでした。'; }
	if ($error == 2) { $errmsg = 'キーワードが長すぎます。'; }

	print "Content-type: text/html\n";
	print "<html><head><title>エラー</title></head>";
	print "$body";
	print "<h1>$errmsg</h1>";
	print "</body></html>";
	exit;
}




sub by_number {
	$a <=> $b;
}
