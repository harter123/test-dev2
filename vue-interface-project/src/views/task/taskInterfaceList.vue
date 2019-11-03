<template>
    <div>

        <div class="Task-list-main">
            <div>
                <el-button size="small" @click="closePage">返回</el-button>
                <el-input class="task-interface-input" size="small" type="number" v-model="interfaceId" placeholder="请输入接口的id"></el-input>
                <el-button type="primary" size="small" @click="addTaskInterface">添加</el-button>

                <div style="margin-top: 5px; margin-left: 3px">
                    任务： {{taskData.name}}
                </div>
            </div>
            <el-table
                    :data="tableData"
                    style="width: 100%">
                <el-table-column
                        prop="name"
                        label="名称"
                        min-width="20%">
                </el-table-column>
                <el-table-column
                        prop="method"
                        label="方法"
                        min-width="10%">
                </el-table-column>
                <el-table-column
                        prop="path"
                        label="URL"
                        min-width="20%">
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
                        <el-button type="text" size="small" @click="removeTaskInterface(scope.row)">移除</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>

    </div>
</template>

<script>
    import {taskGetInterfacesRequest, taskAddInterfaceRequest, taskRemoveInterfaceRequest} from "../../requests/task";

    export default {
        name: "TaskInterfaceList",
        props: {
          taskData: Object,
        },
        data() {
            return {
                tableData: [],
                interfaceId: "",
            }
        },
        methods: {
            closePage(){
                this.$emit('cancel')
            },
            removeTaskInterface(data){
                taskRemoveInterfaceRequest(data.task_interface_id).then(data=>{
                    if (true === data.data.success) {
                        this.getTaskInterfaces();
                    } else {
                        this.$message.info("添加接口失败")
                    }
                })
            },
            addTaskInterface(){
                taskAddInterfaceRequest(this.taskData.id, this.interfaceId).then(data=>{
                    if (true === data.data.success) {
                        this.getTaskInterfaces();
                    } else {
                        this.$message.info("添加接口失败")
                    }
                })
            },
            getTaskInterfaces(){
                taskGetInterfacesRequest(this.taskData.id).then(data=>{
                    if (true === data.data.success) {
                        this.tableData = data.data.data;
                    } else {
                        this.$message.info("获取接口失败")
                    }
                })
            },
        }
        ,
        created() {
            this.getTaskInterfaces();
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
    .task-interface-input {
        width: 200px;margin-right: 10px; margin-left: 10px
    }
</style>