#!/usr/bin/bash


function help()
{
    echo -e '  ./index.sh mm $exchange_id $account_id spot|contract  // show sql of insert market master api '
    echo -e '  ./index.sh trans $trans_matrix.txt $src_matrix.txt [out.txt]  // trans_matrix dot src_matrix => out.txt|stdout'
}


case $1 in
market_master|mm)
    bash ./market_master.sh $@
    ;;
matrix_trans|mt)
    python3 ./matrix_trans.py $@
    ;;
*)
    help
    ;;
esac
