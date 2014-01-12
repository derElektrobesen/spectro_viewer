#!/usr/bin/perl
# coding: utf-8

use strict;
use warnings;
use List::Compare;
use Data::Dumper;
use utf8;

open my $f, ">:encoding(UTF-8)", "results.sql";
open my $inf, "<:encoding(UTF-8)", "dump.sql";
my %names;

while (<$inf>) {
    if (/insert.*names.*\((\d+),'([^']+)','([^']+)','([^']+)','([^']+)'\)/i) {
        $names{$1} = {
            lastname    => $2,
            name        => $3,
            middlename  => $4,
            birth_date  => $5,
            %{$names{$1} || {}}
        };
    } elsif (/insert.*maininfo.*\((\d+),'([^']+)','([^']*)',(\d+),'([^']*)'\)/i) {
        $names{$1} = {
            card_no     => $2,
            diagnosis   => $3,
            eco_count   => $4,
            treat       => $5,
            %{$names{$1} || {}}
        };
    }
}

my %cards;
my $i = 0;

for my $key (keys %names) {
    my $cur = $names{$key};
    next unless $cur->{name} and $cur->{middlename} and $cur->{lastname};
    my $card = $cur->{card_no} && uc $cur->{card_no};
    if (defined $card && $card =~ /([А-Я])(?:-| )?(\d{4})/) {
        $card = "$1-$2";
        if ($cards{$card}) {
            push @{$cards{$card}}, $key;
        } else {
            $cards{$card} = [$key];
            my $str = "call `add_patient`('$cur->{lastname}', '$cur->{name}', '$cur->{middlename}'," .
                "'$card', '$cur->{birth_date}', $cur->{eco_count}, '$cur->{diagnosis}', '$cur->{treat}');\n";
            $cur->{key} = ++$i;
            print $f $str;
        }
    }
}

