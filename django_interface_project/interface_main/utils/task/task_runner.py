from django.forms import model_to_dict

from interface_main.models.task import TaskInterfaceRelation, TaskResult
from interface_main.utils.task.http_request import HttpRequest


class TaskRunner:

    def __init__(self, task):
        self.task = task

    def run(self):
        """
        执行一个任务
        :return:
        """
        if not self.task:
            return

        results = []
        relations = TaskInterfaceRelation.objects.filter(task=self.task)
        for i in relations:
            interface = i.interface
            result = self._run_interface(interface)
            results.append(result)
        self._save_result(results)

    def _run_interface(self, interface):
        """
        执行一个接口
        :param interface:
        :return:
        """
        text = HttpRequest.send_request(interface)
        success = HttpRequest.assert_response(interface, text)
        result = {
            "success": success,
            "request": model_to_dict(interface),
            "response": text,
        }
        return result


    def _save_result(self, results):
        """
        保存结果
        :return:
        """
        if not results:
            return

        # 找出所有的结果，按照version倒序
        task_results = TaskResult.objects.filter(task=self.task).order_by('-version')
        if not task_results:
            version = 1
        else:
            version = task_results[0].version + 1 # 最高的版本，然后 + 1


        # 把结果一个一个地创建
        for i in results:
            r = TaskResult()
            r.success = i["success"]
            r.version = version
            r.task = self.task
            r.request = i["request"]
            r.response = i["response"]
            r.save()
        return

        # 下面这种效率更高，因为下面是一次性创建所有的数据，只需要执行一条sql语句，
        # 上面中这种是一次创建一个数据，有多少个数据，就执行多少条sql语句

        # # 把结果一个一个地创建
        # rs = []
        # for i in results:
        #     r = TaskResult()
        #     r.success = i["success"]
        #     r.version = version
        #     r.task = self.task
        #     r.request = i["request"]
        #     r.response = i["response"]
        #     rs.append(r)
        # TaskResult.objects.bulk_create(rs)
        # return