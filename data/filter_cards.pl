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
my @visits;

print $f "use `spectro_viewer`;\nstart transaction;\n\n";

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
    } elsif (/insert.*diagrams.*\((\d+),(\d+),(\d+),'([^']+)','([^']+)',(\d+)\)/i) {
        my $rec = {
            dia_id  => $2,
            dev     => $3 eq '1' ? "blue" : "red",
            point   => $4,
            type    => $4 eq '1' ? "intact" : "other",
        };
        if ($visits[$6]) {
            push @{$visits[$6]->{diagrams}}, $rec;
        } else {
            $visits[$6] = {
                name_id => $1,
                date    => $5,
                diagrams=> [$rec],
            };
        }
    } elsif (/insert.*comingrecords.*\((\d+),\d+,(\d+),([^,]+),(\d+),(\d+),'([^']*)','([^']*)','([^']*)'\)/i) {
        $visits[$1] = {
            %{$visits[$1]},
            circle_day  => $2,
            endo_w      => $3,
            scar        => $4,
            fibro       => $5,
            onco        => $6,
            more        => $7,
            treat       => $8,
        };
    }
}

my %cards;
my $i = 0;

for my $key (keys %names) {
    my $cur = $names{$key};
    unless ($cur->{name} and $cur->{middlename} and $cur->{lastname}) {
        delete $names{$key};
        next;
    }
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
    } else {
        delete $names{$key};
    }
}

print Dumper \@visits;

for $i (1 .. @visits - 1) {
    my $cur = $visits[$i] || next;
    my $str = "$cur->{name_id}, str_to_date('$cur->{date}', '%d.%m.%Y')";
    print $f "insert into `Visits`(`name_id`, `date`) values ($str);\n";
    $str = "insert into `Treatment`(`visit_id`, `treatment`, `cycle_day`, " .
        "`endometrium`, `scar`, `fibrosis`, `oncology`, `other_info`) values (" .
        "$i, '$cur->{treat}', $cur->{circle_day}, '$cur->{endo_w}', " .
        "$cur->{scar}, $cur->{fibro}, '$cur->{onco}', '$cur->{more}');\n";
    print $f $str;
}

print $f "\n\ncommit;";
