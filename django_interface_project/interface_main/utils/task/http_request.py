import requests
import traceback


class HttpRequest:

    @classmethod
    def assert_response(cls, interface, response):
        """
        # 断言格式:
    # [
    #     {
    #         "text", "文本","include": "true",
    #     },
    #     {
    #         "text": "文本", "include": "false",
    #     },
    # ]
        :param interface:
        :param response:
        :return:
        """
        if not response:
            return False
        assertions = interface.asserts
        if not isinstance(assertions, list):
            return True
        if 0 == len(assertions):
            return True

        for i in assertions:
            text = i.get('text', "")
            include = i.get('include', "")

            if not text:
                continue

            if include == "false":
                if str(text) in str(response):
                    return False
                else:
                    continue
            else: # include == "True"
                if str(text) not in str(response):
                    return False
                else:
                    continue
        return True

    @classmethod
    def send_request(cls, interface):
        if not interface:
            return ""

        url = interface.path
        parameter_type = interface.params_type

        method = interface.method
        header = interface.headers
        parameter = interface.params

        ret = ''
        try:
            if "GET" == method or "get" == method:
                ret = cls._get_request(url, interface.headers, interface.params)
            elif "POST" == method or "post" == method:
                ret = cls._post_request(url, header, parameter, parameter_type)
            elif "DELETE" == method or "delete" == method:
                ret = cls._delete_request(url, header, parameter, parameter_type)
            elif "PUT" == method or "put" == method:
                ret = cls._put_request(url, header, parameter, parameter_type)
            return ret
        except Exception:
            return traceback.format_exc()

    @classmethod
    def _get_request(cls, url, header, parameter):
        """
        get请求，数据都在url，超时30s
        :param url: 字符串
        :param header: 字典
        :param parameter: 字典
        :return:
        """
        ret = requests.get(url, params=parameter, headers=header, timeout=30)
        return ret.text

    @classmethod
    def _post_request(cls, url, header, parameter, parameter_type):
        """
        post 请求
        :param url:
        :param header: 字典
        :param parameter: 字典
        :param parameter_type: 代表是json 还是 form
        :return:
        """
        if not isinstance(header, dict):
            header = {}
        if "json" == parameter_type:
            header["content-type"] = "application/json"
            ret = requests.post(url, json=parameter, headers=header, timeout=30)
        else: # form形式
            header["content-type"] = "application/x-www-form-urlencoded"
            ret = requests.post(url, data=parameter, headers=header, timeout=30)
        return ret.text

    @classmethod
    def _delete_request(cls, url, header, parameter, parameter_type):
        """
        delete请求
        :param url:
        :param header:
        :param parameter:
        :param parameter_type:
        :return:
        """
        if not isinstance(header, dict):
            header = {}
        if "json" == parameter_type:
            header["content-type"] = "application/json"
            ret = requests.delete(url, json=parameter, headers=header, timeout=30)
        else:
            header["content-type"] = "application/x-www-form-urlencoded"
            ret = requests.delete(url, data=parameter, headers=header, timeout=30)
        return ret.text

    @classmethod
    def _put_request(cls, url, header, parameter, parameter_type):
        """
        put请求
        :param url:
        :param header:
        :param parameter:
        :param parameter_type:
        :return:
        """
        if not isinstance(header, dict):
            header = {}
        if "json" == parameter_type:
            header["content-type"] = "application/json"
            ret = requests.put(url, json=parameter, headers=header, timeout=30)
        else:
            header["content-type"] = "application/x-www-form-urlencoded"
            ret = requests.put(url, data=parameter, headers=header, timeout=30)
        return ret.text