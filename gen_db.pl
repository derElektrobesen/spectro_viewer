#!/usr/bin/perl

use strict;
use warnings;

use DBI;

my %args = (
    add_name   => 1,
);

srand scalar time;

main();
exit 0;

sub add_name {
    my $dbh = shift;

    my @names = qw( Иван Петр Павел Кирилл Николай Александр );
    my @lastnames = qw( Иванович Петрович Павлович Кирилович Николаевич Александрович );
    my @surnames = qw( Иванов Петров Сидоров Николаев Антонов Павлов Александров );

    my $sth = $dbh->prepare("call add_patient(?, ?, ?, ?, '13.12.1992', 0, '', '')");

    my $name = $names[int(rand @names)];
    my $lastname = $lastnames[int(rand @lastnames)];
    my $surname = $surnames[int(rand @surnames)];
    my $card = sprintf "AA-%04d", int(rand 9999);

    $sth->execute($surname, $name, $lastname, $card);
}

sub add_visit {
    my ($dbh, $pat_id) = @_;
    my $sth = $dbh->prepare("select add_visit(?)");
    $sth->execute($pat_id);
    return $sth->fetchrow_arrayref()->[0];
}

sub add_diagram {
    my $dbh = shift;
    my $visit_id = shift;
    my $is_intact = shift;

    my $sth = $dbh->prepare("select add_graph(?, 'red', 'test', ?)");
    $sth->execute($visit_id, $is_intact ? 'intact' : 'other');
    return $sth->fetchrow_arrayref()->[0];
}

sub gen_diagram {
    my ($dbh, $d_id) = @_;

    my $sth = $dbh->prepare("insert into Data(diagram_id, point) values (?, POINT(?, ?))");
    
    my ($start, $end) = (6600, 8000);
    my $step = 0.2;
    my $cur = $start;
    my $divider = (4 * 3.1415926535897932) / ($end - $start);

    my $func = sub {
        my $x = shift;
        return (sin $x * $divider - 2 * 3.1415926535897932) * 1000 - rand(3000) + 1500;
    };

    while ($cur <= $end) {
        $sth->execute($d_id, $cur, $func->($cur));
        $cur += $step;
    }
}

sub main {
    my $dbh = DBI->connect("DBI:mysql:spectro_viewer:localhost:3306", "spv_user", "passw",
        { RaiseError => 0, PrintError => 1, });
    #add_name $dbh if $args{add_name};
    my $id = add_diagram($dbh, 1, 0);
    gen_diagram($dbh, $id);
}
