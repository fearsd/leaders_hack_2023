// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-nocheck
import styled from "styled-components";
import LocationIcon from "../assets/LocationIcon.svg";

export interface ICard {
    id: number;
    address: string;
    title: string;
    description: string;
}

const Card = ({id, address, title, description}: ICard) => {
    return (
        <CardWrapper>
            <div style={{
                display: "flex",
                justifyContent: "start",
                alignItems: "center",
                gap: "8px",
            }}>
                <img src={LocationIcon} alt="Location Icon"/>
                <Format>{address}</Format>
            </div>
            <Title>{title}</Title>
            <Description>{description}</Description>
            <div style={{
                height: "96px",
                width: "100%",
                display: "flex",
                justifyContent: "end",
                alignItems: "end",
            }
            }>
                <Button>Узнать больше</Button>
            </div>
        </CardWrapper>
    )
}

export default Card


const CardWrapper = styled.div`
  background: rgba(28, 140, 147, 0.05);
  /* Card_Shadow */
  box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.15);
  border-radius: 15px;
  position: relative;
  padding: 16px;
  width: 100%;
  text-align: start;
`


const Format = styled.span`
  font-style: normal;
  font-weight: 700;
  font-size: 14px;
  line-height: 16px;
  /* leading-trim and text-edge are draft CSS properties.
  
  Read more: https://drafts.csswg.org/css-inline-3/#leading-trim
  */
  leading-trim: both;
  text-edge: cap;

  /* NewGray */
  color: #585858;
`

const Title = styled.h1`
  margin-top: 9px;
  margin-bottom: 16px;
  font-style: normal;
  font-weight: 700;
  font-size: 20px;
  line-height: 23px;
  /* leading-trim and text-edge are draft CSS properties.
  
  Read more: https://drafts.csswg.org/css-inline-3/#leading-trim
  */
  leading-trim: both;
  text-edge: cap;

  /* Primary/Black */
  color: #0E0E0D;


  /* Inside auto layout */
  flex: none;
  order: 1;
  flex-grow: 0;
`

const Description = styled.p`
  font-style: normal;
  font-weight: 500;
  font-size: 14px;
  line-height: 16px;
  /* leading-trim and text-edge are draft CSS properties.
  
  Read more: https://drafts.csswg.org/css-inline-3/#leading-trim
  */
  leading-trim: both;
  text-edge: cap;

  /* NewGray */
  color: #585858;


  /* Inside auto layout */
  flex: none;
  order: 1;
  flex-grow: 0;
`

const Button = styled.button`
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  padding: 12px 16px;
  gap: 10px;

  //position: absolute;
  //right: 15px;
  //bottom: 15px;
  background: transparent;
  /* Primary/Green */
  color: #30676A;
  border: 1.5px solid #30676A;
  border-radius: 10px;

  font-weight: 500;
  font-size: 16px;
  line-height: 19px;
  cursor: pointer;
`
