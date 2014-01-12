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

my @diagrams;

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
            visit_id=> $6,
            dev     => $3 eq '1' ? "blue" : "red",
            point   => $4,
            type    => $4 eq '1' ? "intact" : "other",
        };
        $diagrams[$2] = $rec;
        unless ($visits[$6]) {
            $visits[$6] = {
                name_id => $1,
                date    => $5,
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
    } elsif (/insert.*D(\d+).*\(([^,]+),([^)]+)\)/i) {
        push @{$diagrams[$1]->{points}}, [$2, $3];
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

$i = 0;
for (@diagrams) {
    next unless $_;
    next unless $_->{visit_id};
    my $str =  "insert into `Diagrams`(`visit_id`, `device`, `point_name`, `point_type`) values ($_->{visit_id}, " .
        "'$_->{dev}', '$_->{point}', '$_->{type}');\n";
    print $f $str;
    $i++;
    for (@{$_->{points}}) {
        print $f "insert into `Data`(`diagram_id`, `point`) values ($i, point($_->[0], $_->[1]));\n";
    }
}

print $f "\n\ncommit;";
