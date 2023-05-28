import {createContext, useContext, useState} from "react";
import {UserDetail} from "../types/interfaces";
import {API} from "../api/API";

interface AuthState {
    isAuthenticated: "nonAuthenticated" | "nonuser" | "user";
    user: UserDetail | null;
}

interface AuthContextValue {
    authState: AuthState;
    login: (fullName: string, birthday: string) => Promise<void>;
    logout: () => void;
    getIsAuthenticated: () => "nonAuthenticated" | "nonuser" | "user";
    user: UserDetail | null;
}

const initialAuthState: AuthState = {
    isAuthenticated: "nonAuthenticated",
    user: null,
};


const AuthContext = createContext<AuthContextValue | null>(null);

export const AuthProvider: React.FC = ({children}: any) => {
    const [authState, setAuthState] = useState<AuthState>(initialAuthState);

    const logout = () => {
// Implement your logout logic here
    };

    const login = async (fullName: string, birthday: string): Promise<void> => {
        try {
            const userDetail: UserDetail = await API.checkUser(fullName, birthday) as UserDetail;
            if (userDetail === null || userDetail.id === null || userDetail.id === undefined) {
                throw new Error("User not found");
            }
            setAuthState({
                isAuthenticated: "user",
                user: userDetail,
            });
        } catch (error) {
            setAuthState({
                isAuthenticated: "nonuser",
                user: null,
            });
        }
    };

    const getIsAuthenticated = (): "nonAuthenticated" | "nonuser" | "user" => {
        return authState.isAuthenticated;
    }

    const authContextValue: AuthContextValue = {
        authState,
        login,
        logout,
        getIsAuthenticated,
        user: authState.user,


    };

    return (
        <AuthContext.Provider value={authContextValue}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuthStore = (): AuthContextValue => {
    const authContext = useContext(AuthContext);
    if (!authContext) {
        throw new Error("useAuthStore must be used within an AuthProvider");
    }
    return authContext;
};
