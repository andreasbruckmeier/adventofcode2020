{ split($1,p,"-"); gsub(":", "", $2); gsub("[^" $2 "]", "", $3); if (length($3) >= p[1] && length($3) <= p[2]) c++ } END {print c}
