import {getRequest, postRequest, deleteRequest} from "./common";

export const loginRequest = (userData) => {
    return getRequest("api/backend/users/", userData)
};

export const registerRequest = (userData) => {
    return postRequest("api/backend/users/", userData)
};

export const logoutRequest = () => {
    return deleteRequest("api/backend/users/")
};

export const getUserInfoRequest = () => {
    return getRequest("api/backend/user/info/")
};

