<template>
    <div>
        <div v-if="showTaskRun==true || showInterfaces==true">
            <task-interface-list style="margin-top: 5px" v-if="showInterfaces==true"
                             :taskData="currentTask"
                             @cancel="showInterfaces=false"></task-interface-list>

            <task-run-list style="margin-top: 5px" v-if="showTaskRun==true"
                       :taskData="currentTask"
                       @cancel="showTaskRun=false"></task-run-list>
        </div>

        <div class="Task-list-main" v-else>
            <el-button type="primary" size="small" @click="openAddTask">创建</el-button>
            <el-table
                    :data="tableData"
                    style="width: 100%">
                <el-table-column
                        prop="name"
                        label="名称"
                        min-width="20%">
                    <template slot-scope="scope">
                        <a href="javascript:void(0)" @click="openTaskDetail(scope.row)">{{scope.row.name}}</a>
                    </template>
                </el-table-column>
                <el-table-column
                        prop="description"
                        label="描述"
                        min-width="35%">
                </el-table-column>
                <el-table-column
                        fixed="right"
                        label="操作"
                        min-width="15%">
                    <template slot-scope="scope">
                        <el-button type="text" size="small" @click="openEditTask(scope.row)">编辑</el-button>
                        <el-button type="text" size="small" @click="deleteSingleTask(scope.row)">删除</el-button>
                        <el-button type="text" size="small" @click="openTaskRun(scope.row)">执行面板</el-button>
                    </template>
                </el-table-column>
            </el-table>

            <el-pagination
                    class="page-class"
                    @size-change="handleSizeChange"
                    @current-change="handleCurrentChange"
                    :current-page="page.page"
                    :page-sizes="[10, 20, 50, 100]"
                    :page-size="page.size"
                    layout="total, sizes, prev, pager, next, jumper"
                    :total="page.total">
            </el-pagination>
        </div>

        <el-dialog title="Task" :visible.sync="showAddOrEditTask">

            <el-form :model="TaskForm" :rules="rules" ref="ruleForm" label-width="80px" class="demo-ruleForm">
                <el-form-item label="名称" prop="name">
                    <el-input v-model="TaskForm.name" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="描述" prop="description">
                    <el-input v-model="TaskForm.description" autocomplete="off"></el-input>
                </el-form-item>

            </el-form>

            <div slot="footer" class="dialog-footer">
                <el-button @click="showAddOrEditTask = false">取 消</el-button>
                <el-button type="primary" @click="addOrEditTask">确 定</el-button>
            </div>
        </el-dialog>


    </div>
</template>

<script>
    import {
        getTasksRequest,
        deleteSingleTaskRequest,
        addTaskRequest,
        updateSingleTaskRequest
    } from "../../requests/task";
    import taskInterfaceList from "./taskInterfaceList"
    import taskRunList from "./taskRunList"

    export default {
        name: "TaskList",
        components: {
            'task-interface-list': taskInterfaceList,
            'task-run-list': taskRunList
        },
        data() {
            return {
                tableData: [],

                page: {
                    page: 1,
                    total: 0,
                    size: 10,
                },

                showAddOrEditTask: false,
                opsType: 'add',
                currentTaskId: 0,

                TaskForm: {
                    name: "",
                    description: "",
                },
                rules: {
                    name: [
                        {required: true, message: '请输入名称', trigger: 'blur'},
                    ],
                    method: [
                        {required: true, message: '请选择请求方法', trigger: 'change'}
                    ],
                },

                showInterfaces: false,
                currentTask: undefined,
                showTaskRun: false,
            }
        },
        methods: {
            openTaskRun(data) {
                this.currentTask = data;
                this.showTaskRun = true;
            },
            openTaskDetail(data) {
                this.currentTask = data;
                this.showInterfaces = true;
            },
            addOrEditTask() {
                this.$refs.ruleForm.validate((valid) => {
                    if (valid) { // 代表校验通过
                        if ("add" === this.opsType) {
                            this.addTask()
                        } else {
                            this.editTask()
                        }
                    } else {  //校验失败
                        return false;
                    }
                });

            },
            addTask() {
                let req = this.TaskForm;
                addTaskRequest(req).then(data => {
                    if (true === data.data.success) {
                        this.showAddOrEditTask = false
                        this.getTasksFun()
                    } else {
                        this.$message.info("创建任务失败")
                    }
                })

            },
            editTask() {
                let req = this.TaskForm;
                updateSingleTaskRequest(this.currentTaskId, req).then(data => {
                    if (true === data.data.success) {
                        this.showAddOrEditTask = false;
                        this.getTasksFun()
                    } else {
                        this.$message.info("创建接口失败")
                    }
                })
            },
            deleteSingleTask(data) {
                this.$confirm('是否要永久删除Task' + data.name + ', 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    deleteSingleTaskRequest(data.id).then(data => {
                        if (true === data.data.success) {
                            this.getTasksFun();
                        } else {
                            this.$message.info("删除task成功")
                        }
                    })
                }).catch(() => {
                });
            },
            openAddTask() {
                this.opsType = 'add';
                this.currentTaskId = 0;
                this.TaskForm = {
                    name: "",
                    description: "",
                };
                this.showAddOrEditTask = true;
            },
            openEditTask(data) {
                this.opsType = 'edit';
                this.currentTaskId = data.id;
                this.TaskForm = {
                    name: data.name,
                    description: data.description,
                };
                this.showAddOrEditTask = true;
            }
            ,
            handleSizeChange(size) {
                this.page.size = size;
                this.getTasksFun()
            }
            ,
            handleCurrentChange(index) {
                this.page.page = index;
                this.getTasksFun()
            }
            ,
            getTasksFun() {
                let req = {
                    page: this.page.page,
                    size: this.page.size,
                };
                getTasksRequest(req).then(data => {
                    if (true === data.data.success) {
                        this.tableData = data.data.data.list;
                        this.page.total = data.data.data.total;
                        this.page.page = data.data.data.page;
                        this.page.size = data.data.data.size;
                    } else {
                        this.$message.info("获取任务失败")
                    }
                })
            }
        }
        ,
        created() {
            this.getTasksFun();
        }
        ,
    }
</script>

<style scoped>
    .page-class {
        float: right;
    }

    .Task-list-main {
        padding-top: 10px;
    }
</style>