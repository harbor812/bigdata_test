# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 15:48:00 2018

@author: Brianzhu
"""

import redis

pool = redis.ConnectionPool(host='113.107.166.5', port=16379, db=0)    
r=redis.Redis(connection_pool=pool)
    #r.hset("test1", "k1", "v1")
    #
    #
i=0    
while i < 10:
    
    r.lpush("ceshi","{\"file:/application/controllers/api/Host.php\":[\"del:$pArr = DBinfo::$rank_list_new;\",\"del:$pArr[0] = '';\",\"del:foreach ($pArr as $key=>$g){\",\"add:foreach (DBinfo::$rank_list_new as $key=>$g){\",\"del:$param = ['orderType'=>3,'msgCount'=>100,'startDate'=>$data['time'],'endDate'=>$data['time']];\",\"del:!empty($data['games']) && $param['typeMaster'] = $data['games'];\",\"add:$param = ['typeMaster'=>$data['games'],'orderType'=>3,'msgCount'=>3,'startDate'=>$data['time'],'endDate'=>$data['time']];\",\"del:$v['xiaohulu_index'] = $item['xiaohulu_index'];\",\"add:$v['online'] = $item['xiaohulu_index'];\",\"del:$hitme['avatar'] = $platRoomDataArr[$hitme['platform_id'].'_'.$hitme['room_id']]['avatar'];\",\"add:$hitme['head_image'] = $platRoomDataArr[$hitme['platform_id'].'_'.$hitme['room_id']]['avatar'];\",\"del:$finArr = ['name'=>$g,'id'=>$key,'rank_list'=>$hList];\",\"del://  $redisKey = 'zh'.$data['platform_id'].'_'.$data['game'].'_'.$data['type'].'_'.$data['time'];\",\"del:!empty($platRoomData) && $this->myredis->set('REC_HOST_RANK_LIST_NEW'.'_'.$key.'_1',serialize($finArr));\",\"add:$finArr[] = ['name'=>$g,'id'=>$key,'rank_list'=>$hList];\",\"add:$this->myredis->set('REC_HOST_RANK_LIST_NEW',serialize($finArr));\",\"del://       responseMsg($finArr);\",\"add://responseMsg($finArr);\",\"del:$rankInfoNew1 = [];\",\"del:foreach (DBinfo::$rank_list_new as $key=>$g){\",\"del:$rankInfoNew = $this->myredis->get('REC_HOST_RANK_LIST_NEW'.'_'.$key.'_1');\",\"del:$rankInfoNew = unserialize($rankInfoNew);\",\"del:if(empty($rankInfoNew['rank_list'])) continue;\",\"del:$rankInfoNew['rank_list'] = array_slice($rankInfoNew['rank_list'],0,3);\",\"del:foreach ($rankInfoNew['rank_list'] as &$rankNewItem){\",\"del:$rankNewItem['online'] =$rankNewItem['xiaohulu_index'];\",\"del:$rankNewItem['head_image'] =$rankNewItem['avatar'];\",\"del:}\",\"del:$rankInfoNew1[] = $rankInfoNew;\",\"del:}\",\"del:/*$rankInfoNew =  $this->myredis->get('REC_HOST_RANK_LIST_NEW');\",\"del:$rankInfoNew = empty($rankInfoNew) ? []:unserialize($rankInfoNew);*/\",\"add:$rankInfoNew =  $this->myredis->get('REC_HOST_RANK_LIST_NEW');\",\"add:$rankInfoNew = empty($rankInfoNew) ? []:unserialize($rankInfoNew);\",\"del:responseMsg(['recHostList'=>$recHostList1,'slide_show'=>$data['slideShowList'],'rank_list'=>$rankInfo,'rank_list_new'=>$rankInfoNew1,'game_list'=>$data['game_list'],'platform_list'=>$data['platform_list'],'host_list'=>$hostList,'topic_list'=>$recommendTopicList]);\",\"add:responseMsg(['recHostList'=>$recHostList1,'slide_show'=>$data['slideShowList'],'rank_list'=>$rankInfo,'rank_list_new'=>$rankInfoNew,'game_list'=>$data['game_list'],'platform_list'=>$data['platform_list'],'host_list'=>$hostList,'topic_list'=>$recommendTopicList]);\",\"del:if(empty($hostList) && $data['time'] == 1 && empty($data['platform_id']) && $data['type'] = 2){\",\"del:$hostList = $this->myredis->get('realtime_host_rank_all_'.$data['time'].'_'.$data['platform_id'].'_'.$data['type']);\",\"del:responseMsg(unserialize($hostList));\",\"del:}\",\"del:}elseif($data['time'] == 1 && empty($data['platform_id']) && $data['type'] = 2){\",\"del:!empty($hostList) &&  $this->myredis->set('realtime_host_rank_all_'.$data['time'].'_'.$data['platform_id'].'_'.$data['type'],serialize($hostList));\",\"add:// $data['game_id'] = $this->input->get_post('game_ids',true);\",\"add://echo $data['games'];exit;\",\"add://echo $hostList;exit;\",\"add://$hostList = json_decode($hostList,true);\",\"del:if(empty($hostList) && empty($data['platform_id'])){\",\"del:empty($data['game']) && $data['game'] = 0;\",\"del:$rankInfoNew = $this->myredis->get('REC_HOST_RANK_LIST_NEW'.'_'.$data['game'].'_1');\",\"del:$rankInfoNew =  unserialize($rankInfoNew);\",\"del:!empty($rankInfoNew) && responseMsg($rankInfoNew['rank_list']);\",\"del:}\",\"add://$hostList = json_decode($hostList,true);\",\"del:$this->myredis->set($redisKey,serialize($hList),86400);\",\"add:$this->myredis->set($redisKey,serialize($hList),7200);\"],\"commentID\":[\"ea40652cc66e53baf69efb282ddba7e89d1964c6\"],\"time\":[\"2018-02-11 14:15:00\"],\"objectID\":[\"1\"]}")
    i=i+1
    #r.lpush("test2","123","456","678","000")