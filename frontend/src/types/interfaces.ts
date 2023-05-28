export interface Attendance {
    old_id: number;
    is_online: boolean;
    date: string; // date format
    time_start: string; // time format
    time_end: string; // time format
    id?: number;
    group_id?: number;
    useraccount_id?: number;
}

export interface CheckUserResponse {
    exists: boolean;
    user?: UserDetail;
}

export interface District {
    name: string;
    id?: number;
}

export type Gender = "Мужчина" | "Женщина";

export interface HTTPError {
    detail: string;
}

export interface HTTPValidationError {
    detail: ValidationError[];
}

export interface UserAccount {
    old_id: number;
    birthday: string; // date format
    address: string;
    gender: Gender;
    datetime_created?: string; // date-time format
    fullname?: string;
    id?: number;
}

export interface UserDetail {
    old_id: number;
    birthday: string; // date format
    address: string;
    gender: Gender;
    datetime_created?: string; // date-time format
    fullname?: string;
    id?: number;
    attendances?: Attendance[];
}

export interface UserListResponse {
    skip?: number;
    limit?: number;
    count?: number;
    users?: UserAccount[];
}

export interface ValidationError {
    loc: (string | number)[];
    msg: string;
    type: string;
}

export interface Option {
    id: number;
    question_id: number;
    slug: string;
    text: string;
}

export interface Question {
    question_type: string;
    text: string;
    slug: string;
    num: number;
    id: number;
    options: Option[];
}

export interface Survey {
    datetime_created: string;
    id: number;
    questions: Question[];
}

