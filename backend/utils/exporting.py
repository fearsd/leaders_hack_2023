import os
import json
# import pandas as pd
from openpyxl import load_workbook
from typing import List, Tuple, Set, Optional
from sqlalchemy.orm import Session
from db.models import District, Municipal, Address, Schedule, Route, Group, Attendance, UserAccount
from db.db import get_db


def save_attendance():
    routes = {}
    groups = {}
    users = {}
    for m in range(5902):
        print(m, end=' ')
        with open(f'attend/attend{m}.json', 'r', encoding='utf-8') as f:
            db: Session = next(get_db())
            d = json.load(f)
            for i in d:
                if i['route'] == 'Свободное посещение':
                    d.remove(i)
                    continue
                
                if i['route'] not in routes:
                    i['route_id'] = db.query(Route).filter_by(name=i['route']).first().id
                    routes[i['route']] = i['route_id']
                else:
                    i['route_id'] = routes[i['route']] 
                i.pop('route')
                
                if i['group_old_id'] not in groups:
                    i['group_id'] = db.query(Group).filter_by(old_id=i['group_old_id']).first().id
                    groups[i['group_old_id']] = i['group_id']
                else:
                    i['group_id'] = groups[i['group_old_id']]
                
                if i['user_old_id'] not in users:
                    i['useraccount_id'] = db.query(UserAccount).filter_by(old_id=i['user_old_id']).first().id
                    users[i['user_old_id']] = i['useraccount_id']
                else:
                    i['useraccount_id'] = users[i['user_old_id']]
                i.pop('group_old_id')
                i.pop('user_old_id')
            db.bulk_insert_mappings(Attendance, d)
            db.commit()
            
def export_attendance():
    file = 'Датасеты/attend.csv'
    old_id_col = 'уникальный номер занятия'
    group_old_id_col = 'уникальный номер группы'
    user_old_id_col = 'уникальный номер участника'
    route_col = 'направление 3'
    is_online_col = 'онлайн/офлайн'
    date_col = 'дата занятия'
    time_start_col = 'время начала занятия'
    time_end_col = 'время окончания занятия'
    
    df = pd.read_csv(file)
    num = df.count()['уникальный номер занятия']
    df_dict = df.to_dict()
    attendances = []
    print(num)
    for i in range(num):
        old_id = df_dict[old_id_col][i]
        group_old_id = df_dict[group_old_id_col][i]
        user_old_id = df_dict[user_old_id_col][i]
        route = df_dict[route_col][i]
        is_online = True if df_dict[is_online_col][i] == 'Да' else False
        date = df_dict[date_col][i]
        time_start = df_dict[time_start_col][i]
        time_end = df_dict[time_end_col][i]
        attendances.append(
            {
                'old_id': old_id,
                'group_old_id': group_old_id,
                'user_old_id': user_old_id,
                'route': route,
                'is_online': is_online,
                'date': date,
                'time_start': time_start,
                'time_end': time_end,
            }
        )
    os.mkdir('backend/attend')
    for i in range(num//1000+1):
        print(i, end=' ')
        with open(f'backend/attend/attend{i}.json', 'w', encoding='utf-8') as f:
            json.dump(attendances[i*1000:(i+1)*1000], f, ensure_ascii=False, indent=4)
    
        

def export_groups():
    file = 'Датасеты/groups.csv'
    group_old_id_col = 'уникальный номер'
    route_col = 'направление 3'
    df = pd.read_csv(file)
    num = df.count()['уникальный номер']
    df_dict = df.to_dict()
    res = []
    for i in range(num):
        old_id = df_dict[group_old_id_col][i]
        route = df_dict[route_col][i]
        res.append({
            'old_id': old_id,
            'route': route,
        })
    with open('backend/groups1.json', 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=4)

def save_groups():
    with open('groups1.json', 'r', encoding='utf-8') as f:
        db: Session = next(get_db())
        d = json.load(f)
        for i in d:
            try:
                i['route_id'] = db.query(Route).filter_by(name=i['route']).first().id
            except:
                continue
        
            i.pop('route')
            i['schedules'] = [r.id for r in db.query(Schedule).filter_by(group_old_id=i['old_id'])]
            i['addresses'] = [r.id for r in db.query(Address).filter(Address.group_old_ids.any(i['old_id'])).all()]
        db.bulk_insert_mappings(Group, d)
        db.commit()

    
    
def build_schedules(schedules, group_old_id, is_active = False, is_planned=False):
    res = []
    for i in schedules:
        res.append({
            'group_old_id': group_old_id,
            'body': i,
            'is_active': is_active,
            'is_planned': is_planned,
        })
    return res

def export_schedules():
    file = 'Датасеты/groups.csv'
    
    active_col = 'расписание в активных периодах'
    closed_col = 'расписание в закрытых периодах'
    planned_col = 'расписание в плановом периоде'
    group_old_id_col = 'уникальный номер'
    df = pd.read_csv(file)
    num = df.count()['уникальный номер']
    df_dict = df.to_dict()
    schedules = []
    for i in range(num):
        active = df_dict[active_col][i].split('; ') if isinstance(df_dict[active_col][i], str) else [""]
        closed = df_dict[closed_col][i].split('; ') if isinstance(df_dict[closed_col][i], str) else [""]
        planned = df_dict[planned_col][i].split('; ') if isinstance(df_dict[planned_col][i], str) else [""]
        # print(active, closed, planned)
        group_old_id = df_dict[group_old_id_col][i]
        if active != ['']:
            schedules += build_schedules(active, group_old_id, is_active=True)
        if closed != ['']:
            schedules += build_schedules(closed, group_old_id)
        if planned != ['']:
            schedules += build_schedules(planned, group_old_id, is_planned=True)
    with open('backend/schedules.json', 'w', encoding='utf-8') as f:
        json.dump(schedules, f, ensure_ascii=False, indent=4)

def save_schedules():
    with open('schedules.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
        db: Session = next(get_db())
        db.bulk_insert_mappings(Schedule, d)
        db.commit()
        
    

def build_addresses(address: str, district: str, municipal: str, group_old_id = None) -> Set[Tuple]:
    _splitted_addr = address.split(', ')
    _splitted_district = district.split(', ')
    _splitted_municipal = municipal.split(', ')
    formatted_addresses = []
    address_parts = []
    for address_part in _splitted_addr:
        if "Москва" in address_part:
            formatted_address = ", ".join(address_parts)
            if formatted_address:
                formatted_addresses.append(formatted_address)
            address_parts = [address_part]
        else:
            address_parts.append(address_part)
    formatted_address = ", ".join(address_parts)
    if formatted_address:
        formatted_addresses.append(formatted_address)
    if group_old_id:
        mapped = set(zip(formatted_addresses, _splitted_district, _splitted_municipal, [group_old_id]*len(formatted_address)))
    else:
        mapped = set(zip(formatted_addresses, _splitted_district, _splitted_municipal))
    return mapped

    

def export_level1_to_json():
    # file = 'Датасеты/groups.csv'
    # with open(file, newline='') as csvfile:
    #     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #     for row in spamreader:
    #         print(', '.join(row))
    # district_col = 'округ площадки'
    # municipal_col = 'район площадки'
    # address_col = 'адрес площадки'
    # group_old_id_col = 'уникальный номер'
    # df = pd.read_csv(file)
    # num = df.count()['уникальный номер']
    # df_dict = df.to_dict()
    # addresses = set()
    # addresses2 = set()
    # # _address = build_addresses(df_dict[address_col][2], df_dict[district_col][2], df_dict[municipal_col][2], df_dict[group_old_id][2])
    # for i in range(num):
    #     _address: str = df_dict[address_col][i]
    #     _district: str = df_dict[district_col][i] if isinstance(df_dict[district_col][i], str) else ""
    #     _municipal: str = df_dict[municipal_col][i] if isinstance(df_dict[district_col][i], str) else ""
    #     group_old_id: int = df_dict[group_old_id_col][i]
    #     if 'Москва' not in _address:
    #         addresses.add((_address, _district, _municipal, group_old_id))
    #         addresses2.add((_address, _district, _municipal))
    # 
    #     else:
    #         addresses |= build_addresses(_address, _district, _municipal, group_old_id)
    #         addresses2 |= build_addresses(_address, _district, _municipal)
    # second_step = {}
    # group_old_ids = list(addresses)
    # for i in group_old_ids:
    #     if i[0] in second_step:
    #         second_step[i[0]].append(i[3])
    #     else:
    #         second_step[i[0]] = [i[3]]
    # third_step = []
    # for i in addresses2:
    #     third_step.append({
    #         'address': i[0],
    #         'district': i[1],
    #         'municipal': i[2],
    #         'group_old_ids': second_step[i[0]]
    #     })
    
    
        
    #         
    #     
    # districts = []
    # municipal = []
    # for i in _districts:
    #     districts.append({'name': i})
    # for i in _municipal:
    #     municipal.append({'name': i})
    
        # second_step.append({
            # 'old_id': df_dict[''][i],
    #         'datetime_created': df_dict['дата создание личного дела'][i],
    #         'address': df_dict['адрес проживания'][i],
    #         'birthday': df_dict['дата рождения'][i],
    #         'gender': df_dict['пол'][i]
    #     })
    # wb = load_workbook('Датасеты/dict.xlsx')
    # active_sheet = wb.active
    # first_step = set()
    # row0 = 2
    # category = 'A'
    # level1_old_id_column = 'B'
    # # level1_name_column = 'C'
    # level2_old_id_column = 'D'
    # # level2_name_column = 'E'
    # level3_old_id_column = 'F'
    # level3_name_column = 'G'
    # level3_description_column = 'H'
    # 
    # for i in range(row0, 901):
    #     d = (
    #         active_sheet[f'{level1_old_id_column}{i}'].value,
    #         active_sheet[f'{level2_old_id_column}{i}'].value,
    #         active_sheet[f'{level3_old_id_column}{i}'].value, active_sheet[f'{level3_name_column}{i}'].value,
    #         active_sheet[f'{level3_description_column}{i}'].value, active_sheet[f'{category}{i}'].value
    #     )
    #     first_step.add(d)
    # # print(first_step, len(first_step))
    # second_step = []
    # for i in first_step:
    #     second_step.append({
    #         'level1_old_id': i[0], 'level2_old_id': i[1],
    #         'old_id': i[2], 'name': i[3], 'description': i[4],
    #         'category': i[5]
    #     })
    # print(len(second_step))
    # with open('backend/districts.json', 'w', encoding='utf-8') as f:
    #     json.dump(districts, f, ensure_ascii=False, indent=4)
    # with open('backend/municipal.json', 'w', encoding='utf-8') as f:
    #     json.dump(municipal, f, ensure_ascii=False, indent=4)
    # with open('backend/addresses1.json', 'w', encoding='utf-8') as f:
    #     json.dump(third_step, f, ensure_ascii=False, indent=4)
    
    # with open('districts.json', 'r', encoding='utf-8') as f:
    #     d = json.load(f)
    #     db: Session = next(get_db())
    #     db.bulk_insert_mappings(District, d)
    #     db.commit()
    # with open('municipal.json', 'r', encoding='utf-8') as f:
    #     d = json.load(f)
    #     db: Session = next(get_db())
    #     db.bulk_insert_mappings(Municipal, d)
    #     db.commit()
    # with open('addresses1.json', 'r+', encoding='utf-8') as f:
    #     db: Session = next(get_db())
    #     d = json.load(f)
    #     for i in d:
    #         if i['district']:
    #             i['district_id'] = db.query(District).filter_by(name=i['district']).first().id
    #         i.pop('district', None)
    #         if i['municipal']:
    #             i['municipal_id'] = db.query(Municipal).filter_by(name=i['municipal']).first().id
    #         i.pop('municipal')
    #     db.bulk_insert_mappings(Address, d)
    #     db.commit()
        
    pass
    # with open('users.json', 'r', encoding='utf-8') as f:
    #     d = json.load(f)
    #     db: Session = next(get_db())
    #     db.bulk_insert_mappings(UserAccount, d)
    #     db.commit()
    
    # with open('level3.json', 'r', encoding='utf-8') as f:
    #     d = json.load(f)
    #     db: Session = next(get_db())
    #     _soul = db.query(Category).filter_by(name='Для души').first()
    #     _brain = db.query(Category).filter_by(name='Для ума').first()
    #     _body = db.query(Category).filter_by(name='Для тела').first()
    #     _cat = {
    #         'Для души': _soul,
    #         'Для ума': _brain,
    #         'Для тела': _body,
    #     }
    #     
    #     for index, i in enumerate(d):
    #         i['category_id'] = _cat[i['category']].id
    #         i['level1_id'] = db.query(Level1).filter_by(old_id=i['level1_old_id']).first().id
    #         i['level2_id'] = db.query(Level2).filter_by(old_id=i['level2_old_id']).first().id
    #         i['is_online'] = True if i['name'].startswith('ОНЛАЙН') else False
    #         i.pop('category', None)
    #         i.pop('level1_old_id', None)
    #         i.pop('level2_old_id', None)
    #         print(i)
    #         print(index+1)
    #     
    #     db.bulk_insert_mappings(Route, d)
    #     db.commit()
    
