<template>
    <div class="interface-main">
        <div class="service-tree-main">
            <el-button type="primary" plain size="small" @click="openAddServiceModal(0)">创建根节点</el-button>
            <el-tree class="margin-top-5" :data="data" :props="defaultProps" :default-expand-all="true"
                     @node-click="handleNodeClick">
                <div class="custom-tree-node" slot-scope="{ node, data }">
                    <span>{{ node.label }}</span>
                    <el-dropdown @command="handleCommand">
                          <span class="el-dropdown-link">
                            <i class="el-icon-arrow-down el-icon--right"></i>
                          </span>
                        <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item :command="{key: 'add', data: node}">Add</el-dropdown-item>
                            <el-dropdown-item :command="{key: 'edit', data: node}">Edit</el-dropdown-item>
                            <el-dropdown-item :command="{key: 'delete', data: node}">Delete</el-dropdown-item>

                        </el-dropdown-menu>
                    </el-dropdown>
                </div>
            </el-tree>


            <el-dialog title="创建服务" :visible.sync="addServiceDialogVisible">
                <el-form :model="addServiceData" :rules="rules" ref="addServiceFormRef">
                    <el-form-item label="名称" label-width="100px" prop="name">
                        <el-input v-model="addServiceData.name" autocomplete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="描述" label-width="100px" prop="description">
                        <el-input type="textarea" v-model="addServiceData.description" autocomplete="off"></el-input>
                    </el-form-item>
                </el-form>
                <div slot="footer" class="dialog-footer">
                    <el-button @click="addServiceDialogVisible = false">取 消</el-button>
                    <el-button type="primary" @click="addService">确 定</el-button>
                </div>
            </el-dialog>

            <el-dialog title="编辑服务" :visible.sync="editServiceDialogVisible">
                <el-form :model="editServiceData" ref="editServiceFormRef">
                    <el-form-item label="名称" label-width="100px" prop="name">
                        <el-input v-model="editServiceData.name" autocomplete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="描述" label-width="100px" prop="description">
                        <el-input type="textarea" v-model="editServiceData.description" autocomplete="off"></el-input>
                    </el-form-item>
                </el-form>
                <div slot="footer" class="dialog-footer">
                    <el-button @click="editServiceDialogVisible = false">取 消</el-button>
                    <el-button type="primary" @click="editService">确 定</el-button>
                </div>
            </el-dialog>
        </div>
        <div class="interface-list-main">
            <interface-list :serviceId="currentServiceId"></interface-list>
        </div>
    </div>
</template>

<script>
    import {
        getServicesTreeRequest,
        addServiceRequest,
        updateSingleServiceRequest,
        deleteSingleServiceRequest
    } from "../../requests/service"

    import interfaceList from "./list"

    export default {
        name: "index",
        components: {
            'interface-list': interfaceList
        },
        data() {
            return {
                data: [],
                defaultProps: {
                    children: 'children',
                    label: 'name'
                },

                editServiceDialogVisible: false,
                addServiceDialogVisible: false,
                editServiceData: {
                    name: "",
                    description: "",
                    parent: 0,
                    id: 0,
                },
                addServiceData: {
                    name: "",
                    description: "",
                    parent: 0,
                },
                rules: {
                    name: [
                        {required: true, message: '请输入名称', trigger: 'blur'},
                    ],
                    description: [
                        {required: true, message: '请输入描述', trigger: 'blur'},
                    ],
                },

                currentServiceId: undefined,
            }
        },
        methods: {
            editService() {
                this.$refs.editServiceFormRef.validate((valid) => {
                    if (valid) { // 代表校验通过
                        updateSingleServiceRequest(this.editServiceData.id, this.editServiceData).then(data => {
                            if (true === data.data.success) {
                                this.getServicesTreeFun();
                                this.editServiceDialogVisible = false;
                            } else {
                                this.$message.info("编辑服务失败")
                            }
                        })
                    } else {  //校验失败
                        return false;
                    }
                });
            },
            addService() {
                this.$refs.addServiceFormRef.validate((valid) => {
                    if (valid) { // 代表校验通过
                        addServiceRequest(this.addServiceData).then(data => {
                            if (true === data.data.success) {
                                this.getServicesTreeFun();
                                this.addServiceDialogVisible = false;
                            } else {
                                this.$message.info("创建服务失败")
                            }
                        })
                    } else {  //校验失败
                        return false;
                    }
                });
            },
            openDeleteServiceModal(data) {
                this.$confirm('是否要永久删除服务' + data.name + ', 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    deleteSingleServiceRequest(data.id).then(data => {
                        if (true === data.data.success) {
                            this.getServicesTreeFun();
                        } else {
                            this.$message.info("删除服务失败")
                        }
                    })
                }).catch(() => {
                });
            },
            openAddServiceModal(id) {
                this.addServiceData = {
                    name: "",
                    description: "",
                    parent: id,
                };
                this.addServiceDialogVisible = true;
            },
            openEditServiceModal(data) {
                this.editServiceData = {
                    name: data.name,
                    description: data.description,
                    parent: data.parent,
                    id: data.id
                };
                this.editServiceDialogVisible = true;
            },
            handleCommand(command) {
                let data = command.data.data;
                let key = command.key;
                switch (key) {
                    case "add":
                        this.openAddServiceModal(data.id);
                        break;
                    case "edit":
                        this.openEditServiceModal(data);
                        break;
                    case "delete":
                        this.openDeleteServiceModal(data);
                        break;
                }
            },
            handleNodeClick(data) {
                this.currentServiceId = data.id;
            },
            getServicesTreeFun() {
                getServicesTreeRequest().then(data => {
                    this.data = data.data.data;
                })
            }
        },
        created() {
            this.getServicesTreeFun();
        }
    }
</script>

<style scoped>
    .interface-main {
        display: flex;
        padding-top: 10px;
    }

    .service-tree-main {
        width: 20%;
    }

    .interface-list-main {
        width: 80%;
    }

    .margin-top-5 {
        margin-top: 5px;
    }
</style>