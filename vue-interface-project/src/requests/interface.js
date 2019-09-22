import {getRequest, postRequest, deleteRequest, putRequest} from "./common";

export const getInterfacesRequest = (data) => {
    return getRequest("api/backend/interfaces/", data)
};

export const addInterfaceRequest = (data) => {
    return postRequest("api/backend/interfaces/", data)
};

export const getSingleInterfaceRequest = (interface_id) => {
    return getRequest("api/backend/interface/" + interface_id + "/")
};

export const deleteSingInterfaceRequest = (interface_id) => {
    return deleteRequest("api/backend/interface/" + interface_id + "/")
};

export const updateSingInterfaceRequest = (interface_id, data) => {
    return putRequest("api/backend/interface/" + interface_id + "/", data)
};

