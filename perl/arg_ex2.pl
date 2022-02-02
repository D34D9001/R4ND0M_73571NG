#!/usr/bin/perl

use strict;
use warnings;

my ($name, $number) = @ARGV;

if (not defined $name) {
  die "Need name\n";
}

if (defined $number) {
  print "Save '$name' and '$number'\n";
  # save name/number in database
  exit;
}

print "Fetch '$name'\n";
# look up the name in the database and print it out
