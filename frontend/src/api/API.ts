import {District, UserDetail, ValidationError} from "../types/interfaces.ts";

export class API {
    private static API_URL = 'http://87.242.120.164:8000/api';

    ///api/districts
    public static getDistricts = async () => {
        try {
            const response = await fetch(`${this.API_URL}/districts`);
            return await response.json() as Promise<District[]>;
        } catch (e) {
            console.log(e as ValidationError);
        }
    }

// /api/check
//     Проверка
//
//     Проверка, состоит ли пользователь в проекте "Московское долголетие"
//     Parameters
//     Name	Description
//     fullname *
//     string
//     (query)
//
//     birthday *
//     string($date)
// (query)

    public static checkUser = async (fullname: string, birthday: string) => {
        try {
            const response = await fetch(`${this.API_URL}/check?fullname=${fullname}&birthday=${birthday}`);
            return await response.json() as Promise<UserDetail>
        } catch (e) {
            console.log(e as ValidationError);
        }
    }

    public static async getPoll() {
        try {
            const response = await fetch(`${this.API_URL}/poll`);
            console.log(response);
            return await response.json();
        } catch (e) {
            console.log(e as ValidationError);
        }
    }
}
