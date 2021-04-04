#!/bin/bash
#This is a crapy script to generate single star files with coordinates for relion extraction. You will need a text file with all the unique images names (without extension, no .mrc) that
#can be easily generate from topaz particle txt file using the uniq cmd. This file should be called list_files.txt
#You need acces to relion_star_loopheader in your bash, then just run using as argument the topaz.txt file with the picked particles.
#Then copy the imagename_topaz.star files to the directory where the images are and you can extract normally using ./_topaz.star in relion extract job 
#
#
#
#
#
get_files () {
        files="`uniq list_files.txt`"
}
#
#extract_coordinates () {
#       local i
#       m=`grep -w $i $1 | gawk '{ pritf "%4s %4s %10s\n", $2, $3, $4 }'`
#}
#
get_files
for f in $files
do
        #
        touch ${f}_topaz.star
        #
        relion_star_loopheader rlnCoordinateX rlnCoordinateY rlnAutopickFigureOfMerit > ${f}_topaz.star
        #
        grep -w $f $1 | gawk '{ printf "%4s %4s %10f\n", $2, $3, $4 } ' >> ${f}_topaz.star
        #       

done
