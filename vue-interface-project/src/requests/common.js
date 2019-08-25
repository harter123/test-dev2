import axios from 'axios'

const host = "http://127.0.0.1:8000/";

export const getRequest = function (path, data={}) {
    return axios.get(host + path, {
        params: data,
        withCredentials: true
    })
};

export const postRequest = function (path, data={}) {
    data["withCredentials"] = true;
    return axios.post(host + path, data)
};

export const putRequest = function (path, data={}) {
    data["withCredentials"] = true;
    return axios.put(host + path, data)
};

export const patchRequest = function (path, data={}) {
    data["withCredentials"] = true;
    return axios.patch(host + path, data)
};

export const deleteRequest = function (path, data={}) {
    data["withCredentials"] = true;
    return axios.delete(host + path, data)
};