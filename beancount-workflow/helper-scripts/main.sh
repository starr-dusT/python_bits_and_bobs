#! /bin/sh
#  _         _                     
# | |_  ___ | |_  __ _  _ __  _ __ 
# | __|/ __|| __|/ _` || '__|| '__|
# | |_ \__ \| |_| (_| || |   | |   
#  \__||___/ \__|\__,_||_|   |_|   
# 
# Description: script that imports banking data as csv
# Author: Tyler Starr
# Date Created: 15 May 2020

dir="/home/tstarr/devel/python/beancount-workflow"
cd $dir/helper-scripts/plaid

echo "Extracting for bean-count!"
cp $dir/ledger/ledger.beancount $dir/ledger/ledger.beancount.back

chk="$dir/data/$start_date--$end_date-Checking.csv"
sav="$dir/data/$start_date--$end_date-Savings.csv"

chkim="$dir/imports/checking_$end_date"
savim="$dir/imports/savings_$end_date"

bean-extract $dir/helper-scripts/bean/config.py $chk > $chkim
bean-extract $dir/helper-scripts/bean/config.py $sav > $savim
echo "Done!"
