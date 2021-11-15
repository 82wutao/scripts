#!/usr/bin/bash


function make_market_api_sql()
{
  ex=$1
  plt=$3

  IFS=',' #将空格设置为分隔符。
  read -ra accArr <<<"$2" #将字符串读取到数组中，并由 IFS 分配分隔符。>>>


  echo -e "  OUT:"
  for acc in ${accArr[@]} 
  do
      key=`uuidgen`
      sect=`uuidgen`
      echo -e "" 
      echo -e "\tinsert into t_account_api (id , exchange_id , account_id , name , key , secret , bind_ip , permission , period , status , created_at , updated_at , remark )"
      echo -e "\tvalues (default,$ex,$acc,'${plt}_market_master','$key','$sect','',2,3,1,now(),now(),'');"

  done

}

case $1 in
make_market|mm)
    echo -e "  HINTS: make_market_api_sql($2,$3)"
    make_market_api_sql $2 $3 $4
    ;;
*)
    echo -e '  ./this_script.sh mm $exchange_id $account_id spot|contract  // show sql of insert market master api '
    ;;
esac
