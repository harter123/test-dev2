import json

from django.forms import model_to_dict
from interface_main.models.interface import Interface
from interface_main.models.task import Task, TaskInterfaceRelation, TaskResult
from interface_main.utils.calc import CalcUtils
from interface_main.utils.http_format import response_success
from interface_main.utils.log import default_log
from interface_main.utils.task.task_runner import TaskRunner


def task_add_interface(request, task_id, interface_id):
    task = Task.objects.filter(id=task_id).first()
    if task is None:
        return response_success()

    interface = Interface.objects.filter(id=interface_id).first()
    if interface is None:
        return response_success()

    TaskInterfaceRelation.objects.create(task=task, interface=interface)
    return response_success()


def task_remove_interface(request, task_interface_id):
    TaskInterfaceRelation.objects.filter(id=task_interface_id).delete()
    return response_success()


def task_get_interfaces(request, task_id):
    task = Task.objects.filter(id=task_id).first()
    if task is None:
        return response_success([])
    tis = TaskInterfaceRelation.objects.filter(task=task)
    ret = []
    for i in tis:
        interface = i.interface
        data = model_to_dict(interface)
        data["task_interface_id"] = i.id  #TaskInterfaceRelation 这个表的id,用来给移除表关联
        ret.append(data)
    return response_success(ret)

def run_task(request, task_id):
    """
    执行任务
    :param request:
    :param task_id:
    :return:
    """
    task = Task.objects.filter(id=task_id).first()
    if task is None:
        return response_success()

    runner = TaskRunner(task)
    runner.run()
    return response_success()

def get_task_results(request, task_id):
    """
    获取任务的结果
    :param request:
    :param task_id:
    :return:
    """
    task = Task.objects.filter(id=task_id).first()
    if task is None:
        return response_success()

    version_results = TaskResult.objects.filter(task=task) # 这是获取全部的结果

    # 把所有的version都取出来，放到一个数组里面，然后去重
    version_list = []
    for i in version_results:
        version = i.version
        if version in version_list:
            continue
        else:
            version_list.append(version)

    ret = []
    for version in version_list:
        # 取某一个版本的所有结果
        tmp_results = TaskResult.objects.filter(task=task, version=version)

        if 0 == tmp_results.count():
            continue

        success_count = 0
        failed_count = 0
        for r in tmp_results:
            if r.success:
                success_count += 1
            else:
                failed_count += 1
        ret.append(
            {
            "total": tmp_results.count(),
            "version": version,
            "create_time": tmp_results[0].create_time,
            "success_count": success_count,
            "failed_count": failed_count
            }
        )

    data = request.GET
    size = int(data.get('size', 10))
    page = int(data.get('page', 1))
    ret = CalcUtils.page_data(ret, page, size)
    return response_success(ret)