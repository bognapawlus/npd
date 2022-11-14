#!/bin/bash

#b)
printf "sequences in NC_002306.faa: "
grep -o '>' NC_002306.faa | wc -l
printf "sequences in NC_010437.faa: "
grep -o '>' NC_010437.faa | wc -l


#c)
num=0


#num==0 -> szukamy 'spike'
#num==1 -> wypisujemy
#num==2 -> koniec
cat NC_002306.faa | while read fil
do
	if [[ $fil =~ 'spike' ]]
	then
		num=1
	elif [[ $fil =~ '>' ]]
	then
		num=2
	elif [[ $num == 1 ]]
	then
		echo $fil >> out1.txt
	fi
done 

num=0
cat NC_010437.faa | while read fil
do
	if [[ $fil =~ 'spike' ]]
	then
		num=1
	elif [[ $fil =~ '>' ]]
	then
		num=2
	elif [[ $num == 1 ]]
	then
		echo $fil >> out2.txt
	fi
done 

#d)
diff out1.txt out2.txt



