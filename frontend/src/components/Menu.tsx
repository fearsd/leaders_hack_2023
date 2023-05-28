// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-nocheck

import styled from "styled-components";
import homeIcon from "../assets/Home.svg"
import searchIcon from "../assets/search.svg"
import profileIcon from "../assets/profile.svg"
import {useLocation, useNavigate} from "react-router-dom";

const Menu = () => {
    const location = useLocation();
    const navigate = useNavigate();
    return (
        <MenuWrapper>
            <MenuContainer>
                <MenuItem icon={homeIcon} title="Главная" isActive={location.pathname === "/home"} onClick={() => {
                    navigate("/home")
                }}/>
                <MenuItem icon={searchIcon} title="Поиск" isActive={location.pathname === "/search"} onClick={() => {
                    navigate("/search")
                }}/>
                <MenuItem icon={profileIcon} title="Профиль" isActive={location.pathname === "/profile"}
                          onClick={() => {
                              navigate("/profile")
                          }}/>
            </MenuContainer>
        </MenuWrapper>
    )
}


const MenuItem = ({icon, title, isActive, onClick}: {
    icon: string,
    title: string,
    isActive: boolean,
    onClick: () => void
}) => (
    <MenuItemWrapper isActive={isActive} onClick={onClick}>
        <img src={icon} alt={title}/>
        <span>{title}</span>
    </MenuItemWrapper>
)

const MenuItemWrapper = styled.div<{ isActive: boolean }>`
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  color: ${props => props.isActive ? "#1C8C93" : "#9FA3A7"};
  font-weight: 700;
  fill ${props => props.isActive ? "#1C8C93" : "#9FA3A7"};
  stroke ${props => props.isActive ? "#1C8C93" : "#9FA3A7"};
  font-size: 10px;
  line-height: 12px;
  text-align: center;
  text-transform: uppercase;
  cursor: pointer;
`


export default Menu


const MenuWrapper = styled.div`
  position: sticky;
  max-width: 428px;
  margin: 0 auto;
  bottom: 0;
  left: 0;
  right: 0;
  width: 100%;
  height: 56px;
  background: #ffffff;
  mix-blend-mode: normal;
  box-shadow: 0px -6px 20px rgba(0, 0, 0, 0.15);
  //border-radius: 15px 15px 0px 0px;
  padding: 16px 42px;

`

const MenuContainer = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 428px;
  margin: 0 auto;
  width: 100%;
`
