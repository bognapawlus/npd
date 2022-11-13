#!/bin/bash

#b)
printf "sequences in NC_002306.faa: "
grep -o '>' NC_002306.faa | wc -l
printf "sequences in NC_010437.faa: "
grep -o '>' NC_010437.faa | wc -l


#c)
num=0

cat NC_002306.faa | while read fil
do
	if [[ $fil =~ 'spike' ]]
	then
		num=1
	elif [[ $fil =~ '>' ]]
	then
		num=0
	elif [[ $num == 1 ]]
	then
		echo $fil >> out1.txt
	fi
done 

cat NC_010437.faa | while read fil
do
	if [[ $fil =~ 'spike' ]]
	then
		num=1
	elif [[ $fil =~ '>' ]]
	then
		num=0
	elif [[ $num == 1 ]]
	then
		echo $fil >> out2.txt
	fi
done 

#d)
diff out1.txt out2.txt



