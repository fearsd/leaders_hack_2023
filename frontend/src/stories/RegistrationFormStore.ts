// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-nocheck
import {makeAutoObservable} from "mobx";
import {UserDetail} from "../types/interfaces.ts";
import {API} from "../api/API.ts";
import AuthStore from "./AuthStore.ts";

class RegistrationFormStore {
    lastName = "";
    firstName = "";
    middleName = "";
    birthdate = "";
    authStoreRef: any;

    constructor() {
        makeAutoObservable(this);
    }

    static setAuthStoreRef(AuthStoreContext: AuthStore) {

    }

    setLastName(value: string) {
        this.lastName = value;
    }

    setFirstName(value: string) {
        this.firstName = value;
    }

    setMiddleName(value: string) {
        this.middleName = value;
    }

    setBirthdate(value: Date) {
        this.birthdate = value.toISOString().split('T')[0]
    }

    setAuthStoreRef(authStoreRef: any) {
        this.authStoreRef = authStoreRef;
    }

    onFinish = async () => {
        const {fullName, birthday} = this.getFormData();

        try {
            const userDetail: UserDetail = await API.checkUser(fullName, birthday) as UserDetail;
            authStoreRef.setUser(userDetail)
            console.log("User successfully checked:", userDetail);
        } catch (error) {
            console.log("Error checking user:", error);
            authStoreRef.setFailAuth();
        }
    };

    getFormData() {
        return {
            fullName: `${this.lastName} ${this.firstName} ${this.middleName}`,
            //YYYY-MM-DD
            birthday: new Date(this.birthdate).toISOString().split('T')[0],
        };
    }
}

export default RegistrationFormStore;

