<template>
    <div>
        <div class="ops-class">
            <el-button size="small" type="success" @click="saveInterface">保存</el-button>
            <el-button size="small" type="default" @click="cancel">取消</el-button>
        </div>
        <editor v-model="content" @init="editorInit" lang="json" theme="chrome" height="500"></editor>
    </div>
</template>

<script>
    import {addInterfaceRequest, updateSingInterfaceRequest} from "../../requests/interface";

    export default {
        name: "addOrEditInterface",
        components: {
            editor: require('vue2-ace-editor'),
        },
        // type用来表示是编辑还是创建
        props: ['serviceId', 'type', 'interfaceId', 'interfaceData'],
        data() {
            return {
                content: "",
                default: {
                    name: "",
                    method: "",
                    path: "",
                    description: "",
                    params_type: "json",
                    params: {},
                    headers: [],
                    asserts: [],
                    response: "",
                }
            }
        },
        methods: {
            saveInterface() {
                if ('add' == this.type) {
                    this.addInterface()
                } else {
                    this.editInterface()
                }
            },
            cancel() {
                this.$emit('cancel')
            },
            editorInit: function () {
                require('brace/ext/language_tools') //language extension prerequsite...
                require('brace/mode/json')    //改为json
                require('brace/mode/javascript')    //language
                require('brace/mode/less')
                require('brace/theme/chrome')
                require('brace/snippets/javascript') //snippet
            },

            addInterface() {
                let req = {};
                try{
                    req = JSON.parse(this.content)
                }catch (e) {
                    this.$message.error('请输入正确的json格式')
                }
                req["service_id"] = this.serviceId;

                addInterfaceRequest(req).then(data => {
                    if (true === data.data.success) {
                        this.$emit('success')
                    } else {
                        this.$message.info("创建接口失败")
                    }
                })

            },
            editInterface() {
                let req = {};
                try{
                    req = JSON.parse(this.content)
                }catch (e) {
                    this.$message.error('请输入正确的json格式')
                }
                req["service_id"] = this.serviceId;
                updateSingInterfaceRequest(this.interfaceId, req).then(data => {
                    if (true === data.data.success) {
                        this.$emit('success')
                    } else {
                        this.$message.info("创建接口失败")
                    }
                })
            }
        },
        created() {
            if ('edit' == this.type) {
                this.default = {
                    name: this.interfaceData.name,
                    method: this.interfaceData.method,
                    path: this.interfaceData.path,
                    description: this.interfaceData.description,
                    params_type: this.interfaceData.params_type,
                    params: this.interfaceData.params,
                    headers: this.interfaceData.headers,
                    asserts: this.interfaceData.asserts,
                    response: this.interfaceData.response,
                }
            }
            this.content = JSON.stringify(this.default, null, 4) // 这个是把对象转成json字符串
        }
    }
</script>

<style scoped>
    .ops-class {
        margin-bottom: 10px;
    }
</style>