// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-nocheck
import './App.css'
import styled from "styled-components";
import AuthPage from "./pages/authPage/AuthPage.tsx";
import {AuthProvider} from "./providers/AuthContext.tsx";
import {Route, Routes, useLocation} from "react-router-dom";
import HomePage from "./pages/homePage/HomePage.tsx";
import Menu from "./components/Menu.tsx";
import SearchPage from "./pages/searchPage/SearchPage.tsx";
import SurveyPage from "./pages/surveyPage/SurveyPage.tsx";

const routes = [
    {
        path: '/',
        element: <AuthPage/>,
    },
    {
        path: '/survey',
        element: <SurveyPage/>,
    },
    {
        path: '/home',
        element: <HomePage/>,
    },
    {
        path: '/search',
        element: <SearchPage/>,
    }
];

const menuLocation = [
    "/home",
    "/search",
    "/profile"
]

function App() {
    const location = useLocation();
    return (
        <AppWrapper>
            <AuthProvider>
                <AppContainer>
                    <Routes>
                        {routes.map((route, i) => (
                            <Route
                                key={i}
                                path={route.path}
                                element={route.element}
                            />
                        ))}
                    </Routes>
                </AppContainer>
                {
                    //if home then Menu
                    menuLocation.includes(location.pathname) && <Menu/>

                }
            </AuthProvider>
        </AppWrapper>
    )
}

const AppContainer = styled.div`

  touch-action: pan-y;
  padding: 20px;
  box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
  height: 100%;
  overflow-y: auto;
  background-color: #FBFBFB;
`;

const AppWrapper = styled.div`
  position: relative;
  max-width: 428px;
  height: 92vh;
  max-height: 800px;
  min-width: 320px;
  border-radius: 3px;
  margin: 0 auto;
  background-color: #FBFBFB;

  @media (max-width: 768px) {
    height: 100vh;
  }
`


export default App
