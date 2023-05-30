#!/bin/bash 

for p in $(cat pokemon_list.txt); do
  echo "Getting data for $p"
  curl -s "https://pokeapi.co/api/v2/pokemon-species/$p" > "$p.json" 
  sleep 2
done
