import {DatePicker, Form, Input} from 'antd';
import styled from "styled-components";
import Logo from "../../assets/logo.svg";
import {useNavigate} from "react-router-dom";
import {useAuthStore} from "../../providers/AuthContext.tsx";
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-nocheck
import {useMemo} from "react";

const AuthPage = () => {
    const {getIsAuthenticated} = useAuthStore();
    const isAuthenticated = getIsAuthenticated();
    const navigate = useNavigate();
    useMemo(() => {
        if (isAuthenticated === "user") {
            navigate("/home");
        }
        if (isAuthenticated === "nonuser") {
            navigate("/survey");
        }
    }, [isAuthenticated, navigate]);
    return (
        <div style={{
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            alignItems: "center",
            height: "100%",
            position: "relative"
        }}>
            <div style={{display: "flex", justifyContent: "center", alignItems: "space-between", marginBottom: "24px"}}>
                <AuthTitle>Добро пожаловать</AuthTitle>
                <img src={Logo} alt={"Московское долголетие"}/>
            </div>
            <RegistrationForm/>
        </div>

    )
}

const AuthTitle = styled.h1`
  font-family: 'Manrope';
  font-style: normal;
  font-weight: 800;
  font-size: 36px;
  line-height: 49px;
  text-align: start;
`

const RegistrationForm = () => {
    const {login} = useAuthStore();

    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-ignore
    const onFinish = (values) => {
        const {lastName, firstName, middleName, birthdate} = values;
        const fullName = `${lastName} ${firstName} ${middleName}`;
        const birthday = birthdate.toISOString().split("T")[0];

        login(fullName, birthday);
    };

    return (
        <Form onFinish={onFinish} style={{width: "100%"}}>
            <Form.Item
                name="lastName"
                label="Фамилия"
                rules={[{required: true, message: "Введите фамилию"}]}
            >
                <Input/>
            </Form.Item>

            <Form.Item
                name="firstName"
                label="Имя"
                rules={[{required: true, message: "Введите имя"}]}
            >
                <Input/>
            </Form.Item>

            <Form.Item
                name="middleName"
                label="Отчество"
                rules={[{required: true, message: "Введите отчество"}]}
            >
                <Input/>
            </Form.Item>

            <Form.Item
                name="birthdate"
                label="Дата рождения"
                rules={[{required: true, message: "Выберите дату рождения"}]}
            >
                <DatePicker style={{width: "100%"}}/>
            </Form.Item>

            <Form.Item>
                <FormButton>
                    Зарегистрироваться
                </FormButton>
            </Form.Item>
        </Form>
    );
};


const FormButton = styled.button`
  background: #1C8C93;
  border-radius: 10px;
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 16px 36px;
  width: 100%;
  margin-top: 32px;
  bottom: 10px;
  left: 0;
  justify-content: center;
  right: 0;
  font-style: normal;
  font-weight: 600;
  font-size: 24px;
  line-height: 28px;
`

export default AuthPage;
