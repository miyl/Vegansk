#!/usr/bin/perl
#100 - Curcumin (Turmeric, Gurkemejefarve)
#100 - Curcumin (Turmeric, Gurkemejefarve)
#101 - Riboflavin (Laktoflavin, Vitamin B2)
#943b - Isobutan
#950 - Acesulfamkalium (Sunett®)
#942 - Dinitrogenoxid (Kvælstofforilte, Lattergas, N2O)
#586 - 4-Hexylresorcinol
#635 - Dinatrium-5’-ribonucleotider

# vim presubstitution: %s/[0-9.]*\s*.\s//


while (<>) {
  if (m/^(.*?)\s+-\s+(.*?)(?:\s*\((.*)\))?$/) {
    $three = join('! ', split/,\s*/, $3);
    print "$1: $2? $three!\n";
  }
}
