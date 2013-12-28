#!/usr/bin/perl

use strict;
use warnings;

my @requires = @ARGV;
@ARGV = ();
my $flag = 0;

while (<>) {
    if (!$flag && /\=end/) {
        $flag = 1;
    } elsif ($flag == 1) {
        my $str = $_;
        print "\nrequire '$_'" for @requires;
        $_ = $str;
        $flag = 2;
    }
    print;
}
