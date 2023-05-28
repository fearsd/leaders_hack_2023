// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-nocheck
import {useMemo, useState} from "react";
import {API} from "../../api/API.ts";
import Search from "antd/es/input/Search";
import Card, {ICard} from "../../components/Card.tsx";
import styled from "styled-components";
import {Button, Select} from "antd";
import {Option} from "antd/es/mentions";

interface IFilterComponent {
    isFilterVisible: boolean;
    setIsFilterVisible: (value: boolean) => void;
    districts: string[];
    setDistrict: (value: string) => void;
    days: string[];
    setDays: (value: string[]) => void;
    isOnline: boolean;
    setIsOnline: (value: boolean) => void;
}

const FilterComponent = ({
                             setIsFilterVisible,
                             setDistrict,
                             days,
                             setDays,
                             isOnline,
                             setIsOnline
                         }: IFilterComponent) => {
    const districtsList = [
        //это округа
        {
            id: 1,
            name: 'ЦАО'
        },
        {
            id: 2,
            name: 'САО'
        },
        {
            id: 3,
            name: 'СВАО'
        },
        {
            id: 4,
            name: 'ВАО'
        },
        {
            id: 5,
            name: 'ЮВАО'
        },
        {
            id: 6,
            name: 'ЮАО'
        },
        {
            id: 7,
            name: 'ЮЗАО'
        },
        {
            id: 8,
            name: 'ЗАО'
        },
        {
            id: 9,
            name: 'СЗАО'
        }
    ]

    //фукнция для манипуляции с дянми
    const dayAddOrRemove = (day: string) => {
        if (days.includes(day)) {
            setDays(days.filter((d) => d !== day))
        } else {
            setDays([...days, day])
        }
    }

    const setOnlineOrOffline = (value: boolean) => {
        setIsOnline(value)
    }
    return (
        <FilterWrapper>
            <MainTitle>Фильтры</MainTitle>
            <div style={{marginTop: "32px"}}>
                <Title>Формат занятий</Title>
                <div style={{
                    display: "flex",
                    justifyContent: "start",
                    alignItems: "center",
                    gap: "8px",
                    flexWrap: "wrap",
                    marginTop: "16px"
                }}>
                    <Button onClick={() => setOnlineOrOffline(true)}
                            type={isOnline ? "primary" : "default"}>Онлайн</Button>
                    <Button onClick={() => setOnlineOrOffline(false)}
                            type={!isOnline ? "primary" : "default"}>Оффлайн</Button>
                </div>
            </div>
            <div style={{marginTop: "32px"}}>
                <Title>Дни недели</Title>
                <div style={{
                    display: "flex",
                    justifyContent: "start",
                    alignItems: "center",
                    gap: "8px",
                    flexWrap: "wrap",
                    marginTop: "16px"
                }}>
                    <Button onClick={() => dayAddOrRemove("Понедельник")}
                            type={days.includes("Понедельник") ? "primary" : "default"}>ПН</Button>
                    <Button onClick={() => dayAddOrRemove("Вторник")}
                            type={days.includes("Вторник") ? "primary" : "default"}>ВТ</Button>
                    <Button onClick={() => dayAddOrRemove("Среда")}
                            type={days.includes("Среда") ? "primary" : "default"}>СР</Button>
                    <Button onClick={() => dayAddOrRemove("Четверг")}
                            type={days.includes("Четверг") ? "primary" : "default"}>ЧТ</Button>
                    <Button onClick={() => dayAddOrRemove("Пятница")}
                            type={days.includes("Пятница") ? "primary" : "default"}>ПТ</Button>
                    <Button onClick={() => dayAddOrRemove("Суббота")}
                            type={days.includes("Суббота") ? "primary" : "default"}>СБ</Button>
                    <Button onClick={() => dayAddOrRemove("Воскресенье")}
                            type={days.includes("Воскресенье") ? "primary" : "default"}>ВС</Button>
                </div>
            </div>
            <div style={{marginTop: "32px"}}>
                <Title>Округ</Title>
                <Select onChange={(e) => setDistrict(e.target.value)} style={{width: "100%"}}>
                    <Option value={''}>Не выбрано</Option>
                    {districtsList.map((district) => (
                        <option value={district.id}>{district.name}</option>
                    ))}
                </Select>
            </div>
            <Button style={{position: "absolute", top: "16px", right: "16px"}}
                    onClick={() => setIsFilterVisible(false)}>
                <p>X</p>
            </Button>
        </FilterWrapper>
    )
}


const SearchPage = () => {
    const districts = useMemo(() => {
        return API.getDistricts();
    }, []);
    const [isFilterVisible, setIsFilterVisible] = useState<boolean>(false);
    //фильтры онлайн офлайн день недели и округ москвы
    //поиск по имени
    const [searchValue, setSearchValue] = useState<string>('');
    const [isOnline, setIsOnline] = useState<boolean>(false);
    //выбор дней недели... при
    const [days, setDays] = useState<string[]>([]);
    //выбор округа москвы
    const [district, setDistrict] = useState<string>('');
    const [cards, setCards] = useState<ICard[]>([]);
    return (
        <div style={{width: "100%", display: "flex", flexDirection: "column", gap: "16px", padding: "16px"}}>
            <Search enterButton={"Найти"} placeholder={"Введите имя"} onSearch={(value) => setSearchValue(value)}/>
            <button onClick={() => setIsFilterVisible(!isFilterVisible)}>Фильтры</button>
            {
                cards.map((card) => {
                    return <Card address={card.address} title={card.title} description={card.description} id={card.id}/>
                })
            }
            {
                isFilterVisible &&
                <FilterComponent isFilterVisible={isFilterVisible} setIsFilterVisible={setIsFilterVisible}
                                 districts={districts} setDistrict={setDistrict} days={days} setDays={setDays}
                                 isOnline={isOnline} setIsOnline={setIsOnline}/>
            }
        </div>
    )
}

export default SearchPage

const FilterWrapper = styled.div`
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding: 16px;
  background: rgb(255, 255, 255);
  /* Card_Shadow */
  box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.15);
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  z-index: 100;
`

const Title = styled.h3`
  text-align: start;
  font-style: normal;
  font-weight: 700;
  font-size: 24px;
  margin-bottom: 16px;
  line-height: 28px;
  /* leading-trim and text-edge are draft CSS properties.
  
  Read more: https://drafts.csswg.org/css-inline-3/#leading-trim
  */
  leading-trim: both;
  text-edge: cap;

  /* Primary/Black */
  color: #0E0E0D;
`
const MainTitle = styled.h1`
  font-style: normal;
  font-weight: 800;
  font-size: 24px;
  line-height: 33px;
  /* leading-trim and text-edge are draft CSS properties.
  
  Read more: https://drafts.csswg.org/css-inline-3/#leading-trim
  */
  leading-trim: both;
  text-edge: cap;

  /* Primary/Black */
  color: #0E0E0D;
`
