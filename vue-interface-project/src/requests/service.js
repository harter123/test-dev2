import {getRequest, postRequest, deleteRequest, putRequest} from "./common";

export const getServicesTreeRequest = () => {
    return getRequest("api/backend/services/")
};

export const addServiceRequest = (data) => {
    return postRequest("api/backend/services/", data)
};

export const getSingleServiceRequest = (service_id) => {
    return getRequest("api/backend/service/" + service_id + "/")
};

export const deleteSingleServiceRequest = (service_id) => {
    return deleteRequest("api/backend/service/" + service_id + "/")
};

export const updateSingleServiceRequest = (service_id, data) => {
    return putRequest("api/backend/service/" + service_id + "/", data)
};

