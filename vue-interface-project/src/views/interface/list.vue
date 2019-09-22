<template>
    <div>
        <el-button type="primary" size="small">创建</el-button>
        <el-table
                :data="tableData"
                style="width: 100%">
            <el-table-column
                    prop="name"
                    label="名称"
                    width="180">
            </el-table-column>
            <el-table-column
                    prop="method"
                    label="方法"
                    width="100">
            </el-table-column>
            <el-table-column
                    prop="path"
                    label="URL"
                    width="300">
            </el-table-column>
            <el-table-column
                    prop="description"
                    label="描述"
                    width="200">
            </el-table-column>
            <el-table-column
                    fixed="right"
                    label="操作"
                    width="100">
                <template slot-scope="scope">
                    <el-button type="text" size="small">编辑</el-button>
                    <el-button type="text" size="small">删除</el-button>
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
</template>

<script>
    import {getInterfacesRequest} from "../../requests/interface";

    export default {
        name: "list",
        props: {
            serviceId: {
                type: Number,
                default: undefined,
            },
        },
        data() {
            return {
                tableData: [],

                page: {
                    page: 1,
                    total: 0,
                    size: 10,
                }
            }
        },
        methods: {
            handleSizeChange(size) {
                this.page.size = size;
                this.getInterfacesFun()
            },
            handleCurrentChange(index) {
                this.page.page = index;
                this.getInterfacesFun()
            },
            getInterfacesFun() {
                if (!this.serviceId) {
                    return;
                }
                let req = {
                    service_id: this.serviceId,
                    page: this.page.page,
                    size: this.page.size,
                };
                getInterfacesRequest(req).then(data => {
                    if (true === data.data.success) {
                        this.tableData = data.data.data.list;
                        this.page.total = data.data.data.total;
                        this.page.page = data.data.data.page;
                        this.page.size = data.data.data.size;
                    } else {
                        this.$message.info("获取接口失败")
                    }
                })
            }
        },
        created() {
            this.getInterfacesFun();
        },
        watch: {
            serviceId: function () {
                this.getInterfacesFun()
            },
        }
    }
</script>

<style scoped>
    .page-class {
        float: right;
    }
</style>