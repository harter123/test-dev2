import axios from 'axios'

axios.defaults.withCredentials=true;

const host = "http://127.0.0.1:8000/";

export const getRequest = function (path, data={}) {
    return axios.get(host + path, {
        params: data,
    })
};

export const postRequest = function (path, data={}) {
    return axios.post(host + path, data)
};

export const putRequest = function (path, data={}) {
    return axios.put(host + path, data)
};

export const patchRequest = function (path, data={}) {
    return axios.patch(host + path, data)
};

export const deleteRequest = function (path, data={}) {
    return axios.delete(host + path, data)
};