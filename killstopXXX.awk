#!/usr/bin/awk -f

BEGIN {
    stop_regex = "\\<(is|the|in|but|can|a|of|to|that|it|for|on|with|as|this|was|at|by|an|be|from|or|are)\\>";
}

{
    # https://www.gnu.org/software/gawk/manual/html_node/String-Functions.html#index-gsub_0028_0029-function-1
    gsub(stop_regex, "", $0);
    print $0;
}
