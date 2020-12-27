#!/usr/bin/awk -f
BEGIN{FS=""}v==1||NR%v==1{m=i%(NF)+1;if($m=="#")t++;i+=h}END{print t}
