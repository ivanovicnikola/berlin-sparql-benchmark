- Generate Turtle dataset for 1 product
./generate -fc -s ttl -fn dataset_1 -pc 1

- Run zsh ./Scripts/load_data.sh to load data
replace the path to your system path

- Run testdriver on http://localhost:8890/sparql with the following command:
./testdriver http://localhost:8890/sparql

- update: ./testdriver -ucf usecases/exploreAndUpdate/sparql.txt -u http://localhost:8890/sparql -udataset dataset_update.nt http://localhost:8890/sparql