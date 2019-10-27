<template>
    <div>
        <div class="mock-list-main">
            <el-button type="primary" size="small" @click="openAddMock">创建</el-button>
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
                    <template slot-scope="scope">
                        <span>http://localhost:8000/api/backend/make_mock/{{scope.row.id}}/</span>
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
                        <el-button type="text" size="small" @click="openEditMock(scope.row)">编辑</el-button>
                        <el-button type="text" size="small" @click="deleteSingleMock(scope.row)">删除</el-button>
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

        <el-dialog title="Mock" :visible.sync="showAddOrEditMock">

            <el-form :model="mockForm" :rules="rules" ref="ruleForm" label-width="80px" class="demo-ruleForm">
                <el-form-item label="名称" prop="name">
                    <el-input v-model="mockForm.name" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="描述" prop="description">
                    <el-input v-model="mockForm.description" autocomplete="off"></el-input>
                </el-form-item>

                <el-form-item label="方法" prop="method">
                    <el-select v-model="mockForm.method" placeholder="请选择请求方法">
                        <el-option label="get" value="get"></el-option>
                        <el-option label="post" value="post"></el-option>
                        <el-option label="put" value="put"></el-option>
                        <el-option label="delete" value="delete"></el-option>
                    </el-select>
                </el-form-item>

                <el-form-item label="响应" prop="response">
                    <editor v-model="mockForm.response" @init="editorInit" lang="json" theme="chrome"
                            height="300"></editor>

                </el-form-item>

            </el-form>

            <div slot="footer" class="dialog-footer">
                <el-button @click="showAddOrEditMock = false">取 消</el-button>
                <el-button type="primary" @click="addOrEditMock">确 定</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
    import {getMocksRequest, deleteSingMockRequest, addMockRequest, updateSingMockRequest} from "../../requests/mock";

    export default {
        name: "mockList",
        components: {
            editor: require('vue2-ace-editor'),
        },
        data() {
            return {
                tableData: [],

                page: {
                    page: 1,
                    total: 0,
                    size: 10,
                },

                showAddOrEditMock: false,
                opsType: 'add',
                currentMockId: 0,

                mockForm: {
                    name: "",
                    description: "",
                    method: "get",
                    response: "{}"
                },
                rules: {
                    name: [
                        {required: true, message: '请输入名称', trigger: 'blur'},
                    ],
                    method: [
                        {required: true, message: '请选择请求方法', trigger: 'change'}
                    ],
                }
            }
        },
        methods: {
            addOrEditMock() {
                this.$refs.ruleForm.validate((valid) => {
                    if (valid) { // 代表校验通过
                        if ("add" === this.opsType) {
                            this.addMock()
                        } else {
                            this.editMock()
                        }
                    } else {  //校验失败
                        return false;
                    }
                });

            },
            addMock() {
                let req = JSON.parse(JSON.stringify(this.mockForm));
                try {
                    req["response"] = JSON.parse(String(this.mockForm.response))
                } catch (e) {
                    console.log(e)
                    this.$message.error('请输入正确的json格式')
                    return;
                }
                addMockRequest(req).then(data => {
                    if (true === data.data.success) {
                        this.showAddOrEditMock = false
                        this.getMocksFun()
                    } else {
                        this.$message.info("创建接口失败")
                    }
                })

            },
            editMock() {
                let req = JSON.parse(JSON.stringify(this.mockForm));
                try {
                    req["response"] = JSON.parse(String(this.mockForm.response))

                } catch (e) {
                    console.log(e)
                    this.$message.error('请输入正确的json格式')
                    return;
                }
                updateSingMockRequest(this.currentMockId, req).then(data => {
                    if (true === data.data.success) {
                        this.showAddOrEditMock = false;
                        this.getMocksFun()
                    } else {
                        this.$message.info("创建接口失败")
                    }
                })
            },
            editorInit: function () {
                require('brace/ext/language_tools') //language extension prerequsite...
                require('brace/mode/json')    //改为json
                require('brace/mode/javascript')    //language
                require('brace/mode/less')
                require('brace/theme/chrome')
                require('brace/snippets/javascript') //snippet
            }
            ,
            deleteSingleMock(data) {
                this.$confirm('是否要永久删除Mock' + data.name + ', 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    deleteSingMockRequest(data.id).then(data => {
                        if (true === data.data.success) {
                            this.getMocksFun();
                        } else {
                            this.$message.info("删除接口成功")
                        }
                    })
                }).catch(() => {
                });
            }
            ,
            successAddOrEditMock() {
                this.showAddOrEditMock = false;
                this.getMocksFun();
            }
            ,
            cancelAddOrEditMock() {
                this.showAddOrEditMock = false;
            }
            ,
            openAddMock() {
                this.opsType = 'add';
                this.currentMockId = 0;
                this.mockForm = {
                    name: "",
                    description: "",
                    method: "get",
                    response: "{}",
                };
                this.showAddOrEditMock = true;
            }
            ,
            openEditMock(data) {
                this.opsType = 'edit';
                this.currentMockId = data.id;
                this.mockForm = {
                    name: data.name,
                    description: data.description,
                    method: data.method,
                    response: JSON.stringify(data.response),
                };
                this.showAddOrEditMock = true;
            }
            ,
            handleSizeChange(size) {
                this.page.size = size;
                this.getMocksFun()
            }
            ,
            handleCurrentChange(index) {
                this.page.page = index;
                this.getMocksFun()
            }
            ,
            getMocksFun() {
                let req = {
                    page: this.page.page,
                    size: this.page.size,
                };
                getMocksRequest(req).then(data => {
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
        }
        ,
        created() {
            this.getMocksFun();
        }
        ,
    }
</script>

<style scoped>
    .page-class {
        float: right;
    }

    .mock-list-main {
        padding-top: 10px;
    }
</style>