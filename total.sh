count=1
while [ $count -ne 2 ]
do
	 echo "debut total" >> test.txt
    # commandes à exécuter
    curl https://www.boursorama.com/cours/1rPTTE/ > /home/ubuntu/total.txt
    cat total.txt | grep -oP '(?<=c-instrument c-instrument--last" data-ist-last>).*?(?=</span>)' | tail -n -1 >> /home/ubuntu/total_prix.txt
    date +"%d/%m/%Y %H:%M:%S" >> /home/ubuntu/total_date.txt
    count=$((count+1))
    # attendre 1 minute avant de continuer
    echo "fin total" >> test.txt
done
