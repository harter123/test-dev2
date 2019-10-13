<template>
    <div>
        <add-or-edit-interface
                v-if="showAddOrEditInterface"
                :type="opsType"
                :serviceId="serviceId"
                :interfaceId="currentInterfaceId"
                :interfaceData="currentInterfaceData"
                @success="successAddOrEditInterface"
                @cancel="cancelAddOrEditInterface">
        </add-or-edit-interface>

        <div v-else>
            <el-button type="primary" size="small" @click="openAddInterface">创建</el-button>
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
                        <el-button type="text" size="small" @click="openEditInterface(scope.row)">编辑</el-button>
                        <el-button type="text" size="small" @click="deleteSingleInterface(scope.row)">删除</el-button>
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

    </div>
</template>

<script>
    import {getInterfacesRequest, deleteSingInterfaceRequest} from "../../requests/interface";

    import addOrEditInterface from "./addOrEditInterface"

    export default {
        name: "list",
        props: {
            serviceId: {
                type: Number,
                default: undefined,
            },
        },
        components: {
            'add-or-edit-interface': addOrEditInterface,
        },
        data() {
            return {
                tableData: [],

                page: {
                    page: 1,
                    total: 0,
                    size: 10,
                },

                showAddOrEditInterface: false,
                opsType: 'add',
                currentInterfaceId: 0,
                currentInterfaceData: {},
            }
        },
        methods: {
            deleteSingleInterface(data){
                this.$confirm('是否要永久删除接口' + data.name + ', 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    deleteSingInterfaceRequest(data.id).then(data => {
                        if (true === data.data.success) {
                            this.getInterfacesFun();
                        } else {
                            this.$message.info("删除接口成功")
                        }
                    })
                }).catch(() => {
                });
            },
            successAddOrEditInterface(){
                this.showAddOrEditInterface = false;
                this.getInterfacesFun();
            },
            cancelAddOrEditInterface(){
                this.showAddOrEditInterface = false;
            },
            openAddInterface(){
                this.opsType = 'add';
                this.currentInterfaceId = 0;
                this.currentInterfaceData = {};
                this.showAddOrEditInterface = true;
            },
            openEditInterface(data){
                this.opsType = 'edit';
                this.currentInterfaceId = data.id;
                this.currentInterfaceData = data;
                this.showAddOrEditInterface = true;
            },
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