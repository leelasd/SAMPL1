for i in `ls *.pdb|sed 's/\.pdb//g'`
do
rm $i.cmd
#echo $i
#sed  "s/prometryn/$i/g" test.cmd >$i.cmd
#/Applications/Chimera.app/Contents/MacOS/chimera $i.cmd
done
