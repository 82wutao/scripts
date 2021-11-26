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
function mount_activity_to_accounts_sql()
{
  activityID=$1

  echo -e "  OUT:"
  echo -e "" 
  echo -e "\tinsert into t_account_activity (exchange_id,account_id,state,created_at,updated_at,remark)"
  echo -e "\tselect exchange_id,account_id,$activityID,1,now(),now(),'' from t_account;"
}
function create_activity_sql()
{
#[]name,[]content,picture,start,end,nav,complet,[]reward,rewardnum,rewardlife,

#    insert into t_activity(title_zh,title_en,title_idn,content_zh,content_en,content_idn,picture,start_date,end_date,navigation,complete_condition, reward_zh,reward_en,reward_idn,reward_num,
#    reward_life,state,created_at,updated_at,remark) 
#    values('充值抵现_hant','充值抵现_en','充值抵现 _id','Cont_hant','Cont_en','Cont_id',null,now(),now(),'deposits','充币','抵扣券 _hant','抵扣券_en','抵扣券_id',10.0,0,1,now(),now(),null),
echo $@

}

case $1 in
make_market|mm)
    echo -e "  HINTS: make_market_api_sql($2,$3,$4)"
    make_market_api_sql $2 $3 $4
    ;;
mount_activity|ma)
    echo -e "  HINTS: mount_activity_to_accounts_sql($2)"
    mount_activity_to_accounts_sql $2 
    ;;
create_activity|ca)
    echo -e "  HINTS: create_activity_to_accounts_sql($2)"
    create_activity_sql $@ 
    ;;
*)
    echo -e '  ./this_script.sh mm $exchange_id $account_id spot|contract  // show sql of insert market master api '
    echo -e '  ./this_script.sh ma $activityID                             // show sql of insert into account_activity select account '
    echo -e '  ./this_script.sh ca "name_hant,name_en,name_id" "content_hant,content_en,content_id" "reward_hant,reward_en,reward_id" reward_num nav \ 
            start_date end_date[ picture_url complete_condition rewardlife]'
    ;;
esac
