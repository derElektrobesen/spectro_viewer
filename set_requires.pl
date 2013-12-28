#!/usr/bin/perl

use strict;
use warnings;
use File::Copy;

my $help = <<HELP;
    Usage: $0 [options] [requires]
    Options:
        -i  --  Set input file name [required]
        -b  --  Do file backuping [default 0]
        -h  --  Show this help
HELP

my @requires;
my $do_backup = 0;
my $input_fname = '';

while ($_ = shift @ARGV) {
    if (/-i\b/) {
        $input_fname = shift;
    } elsif (/-b/) {
        $do_backup = 1;
    } elsif (/(-h|--help)\b/) {
        print $help;
        exit 0;
    } else {
        unshift @requires, $_;
    }
}

die "No requires given\n" unless @requires;
die "No input file given\n" unless $input_fname;

copy($input_fname, "$input_fname.bac") or die "Copy failed";
open my $if, "<", "$input_fname.bac" or die "Open failure";
open my $of, ">", "$input_fname" or die "Open failure";

my $flag = 0;

while (<$if>) {
    if (!$flag && /\=end/) {
        $flag = 1;
    } elsif ($flag == 1) {
        my $str = $_;
        print $of "\nrequire '$_'" for @requires;
        $_ = $str;
        $flag = 2;
    }
    print $of $_;
}

unlink "$input_fname.bac" unless $do_backup;
