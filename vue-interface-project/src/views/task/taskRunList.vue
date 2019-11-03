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
                        prop="date"
                        label="日期"
                        min-width="20%">
                </el-table-column>
                <el-table-column
                        prop="total"
                        label="总个数"
                        min-width="20%">
                </el-table-column>
                <el-table-column
                        prop="success"
                        label="成功个数"
                        min-width="20%">
                </el-table-column>
                <el-table-column
                        prop="failed"
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