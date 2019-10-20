import {getRequest, postRequest, deleteRequest, putRequest} from "./common";

export const getMocksRequest = (data) => {
    return getRequest("api/backend/mocks/", data)
};

export const addMockRequest = (data) => {
    return postRequest("api/backend/mocks/", data)
};

export const getSingleMockRequest = (mock_id) => {
    return getRequest("api/backend/mock/" + mock_id + "/")
};

export const deleteSingMockRequest = (mock_id) => {
    return deleteRequest("api/backend/mock/" +mock_id + "/")
};

export const updateSingMockRequest = (mock_id, data) => {
    return putRequest("api/backend/mock/" + mock_id + "/", data)
};

