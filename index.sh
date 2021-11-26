#!/usr/bin/bash


function help()
{
    echo -e '  ./index.sh ca "name_hant,name_en,name_id" "content_hant,content_en,content_id" "reward_hant,reward_en,reward_id" reward_num nav  
            start_date end_date[ picture_url complete_condition rewardlife]'
    echo -e '                                                        // show sql of create a activity sql '
    echo -e '\n'
    echo -e '  ./index.sh mm $exchange_id $account_id spot|contract  // show sql of insert market master api '
    echo -e '  ./index.sh ma $activityID                             // show sql of insert into account_activity select account '
    echo -e '  ./index.sh trans $trans_matrix.txt $src_matrix.txt [out.txt]  // trans_matrix dot src_matrix => out.txt|stdout'
}


case $1 in
market_master|mm)
    bash ./market_master.sh $@
    ;;
mount_activity|ma)
    bash ./market_master.sh $@
    ;;
create_activity|ca)
    bash ./market_master.sh $@
    ;;
matrix_trans|mt)
    python3 ./matrix_trans.py $@
    ;;
*)
    help
    ;;
esac
