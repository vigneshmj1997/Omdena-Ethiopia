
#download oscar dataset from hugginface
key="" #Enter you hf key here

if [ -z "$key" ]
then
    echo "the key string should not be empty"
    exit
else
    python3 download_oscar.py --hftoken $key
fi


#Download data from cc-100 Common crawl
wget -P downloads/ http://data.statmt.org/cc-100/am.txt.xz
xz -d downloads/am.txt.xz

#Combining both the file and making a single file of them 
cat downloads/am.txt downloads/amharic.txt > downloads/complete.txt && rm downloads/am.txt downloads/amharic.txt

echo "Total number of lines are"
wc -l downloads/complete.txt | awk '{print $1}'

rm downloads/am.txt.xz*
