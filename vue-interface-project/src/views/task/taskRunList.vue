<template>
    <div>

        <div class="Task-list-main">
            <div>
                <el-button size="small" @click="closePage">返回</el-button>
                <el-button type="primary" size="small" @click="runTask">执行</el-button>

                <div style="margin-top: 5px; margin-left: 3px">
                    任务： {{taskData.name}}
                </div>
            </div>
            <el-table
                    :data="tableData"
                    style="width: 100%">
                <el-table-column
                        prop="version"
                        label="版本"
                        min-width="20%">
                </el-table-column>
                <el-table-column
                        prop="create_time"
                        label="日期"
                        min-width="20%">
                </el-table-column>
                <el-table-column
                        prop="total"
                        label="总个数"
                        min-width="20%">
                </el-table-column>
                <el-table-column
                        prop="success_count"
                        label="成功个数"
                        min-width="20%">
                </el-table-column>
                <el-table-column
                        prop="failed_count"
                        label="失败个数"
                        min-width="20%">
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

    </div>
</template>

<script>
    import {runTaskRequest, getTaskResultsRequest} from "../../requests/task";

    export default {
        name: "TaskRunList",
        props: {
          taskData: Object,
        },
        data() {
            return {
                tableData: [],

                page: {
                    page: 1,
                    total: 0,
                    size: 10,
                },
            }
        },
        methods: {
            closePage(){
                this.$emit('cancel')
            },
            runTask(){
                runTaskRequest(this.taskData.id).then(data=>{
                    this.getTaskRunList();
                })
            },
            handleSizeChange(size) {
                this.page.size = size;
                this.getTaskRunList()
            },
            handleCurrentChange(index) {
                this.page.page = index;
                this.getTaskRunList()
            },
            getTaskRunList(){
                getTaskResultsRequest(this.taskData.id, this.page).then(data=>{
                    if (true === data.data.success) {
                        this.tableData = data.data.data.list;
                        this.page.total = data.data.data.total;
                        this.page.page = data.data.data.page;
                        this.page.size = data.data.data.size;
                    } else {
                        this.$message.info("获取任务结果失败")
                    }
                })
            }
        },
        created() {
            this.getTaskRunList();
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