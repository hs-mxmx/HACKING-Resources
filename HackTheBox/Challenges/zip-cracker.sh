#!/bin/bash


#find . -name "*.zip" | while read filename; do unzip -o -d "`dirname "$filename"`" "$filename"; done;

declare -a cracked_zip
declare -a all_zips


extract(){
	zip=$1
	total=$(( $2 + 1 ))
	pattern=" |'"
	zip="$(echo $zip | tr -dc '0-9')"
	#echo $zip
	zipassword="$(zipinfo $zip | head -n 3 | cut -c53-)"
	#echo Password: $(echo $zipassword)
	zipassword="$(echo $zipassword | tr -dc '0-9')"
	echo -e "\t\n[+]Password:" $zipassword "\n"
	#echo [+]ZipFile: $zip
	echo $(unzip -P $zipassword $zip)
	echo -e "\t\n[!]Files Cracked: " $total
	extract $zipassword $total

}

zip=$1
total=0

extract $zip $total 





