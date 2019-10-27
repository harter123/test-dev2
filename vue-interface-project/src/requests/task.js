import {getRequest, postRequest, deleteRequest, putRequest} from "./common";

export const getTasksRequest = () => {
    return getRequest("api/backend/tasks/")
};

export const addTaskRequest = (data) => {
    return postRequest("api/backend/tasks/", data)
};

export const getSingleTaskRequest = (taskId) => {
    return getRequest("api/backend/task/" + taskId + "/")
};

export const deleteSingleTaskRequest = (taskId) => {
    return deleteRequest("api/backend/task/" + taskId + "/")
};

export const updateSingleTaskRequest = (taskId, data) => {
    return putRequest("api/backend/task/" + taskId + "/", data)
};

export const taskAddInterfaceRequest = (taskId, interfaceId) => {
    return getRequest("api/backend/add/task_interface/" + taskId + "/" + interfaceId + "/")
};

export const taskRemoveInterfaceRequest = (taskInterfaceId) => {
    return getRequest("api/backend/remove/task_interface/" + taskInterfaceId + "/")
};

export const taskGetInterfacesRequest = (taskId) => {
    return getRequest("api/backend/show/task_interfaces/" + taskId + "/")
};
