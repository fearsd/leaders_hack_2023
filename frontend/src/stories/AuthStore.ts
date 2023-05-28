import {makeAutoObservable} from "mobx";
import {UserDetail} from "../types/interfaces.ts";
import {createContext} from "react";

class AuthStore {
    isAuthenticated = false;
    user: UserDetail | undefined | null = undefined;

    constructor() {
        makeAutoObservable(this);
    }

    public get getUser() {
        return this.user;
    }

    get getIsAuthenticated() {
        return this.isAuthenticated;
    }

    public setIsAuthenticated(value: boolean) {
        this.isAuthenticated = value;
    }

    public setUser(user: UserDetail | null) {
        console.log("setUser", user);
        this.user = user;
        this.isAuthenticated = !!user;
    }

    public setFailAuth() {
        this.user = null;
        this.isAuthenticated = false;
    }
}

const authStore = createContext(new AuthStore());
export default authStore;
