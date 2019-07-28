<template>
    <div class="login">
        <header-component></header-component>
        <div class="login-context">
            <h2>账号登录</h2>

            <el-form label-position="left" :model="loginForm" :rules="rules" ref="loginFormRef" label-width="50px" class="demo-ruleForm">
                <el-form-item label="名称" prop="name">
                    <el-input v-model="loginForm.name" placeholder="请输入用户名"></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="passWord">
                    <el-input v-model="loginForm.passWord" show-password placeholder="请输入密码"></el-input>
                </el-form-item>
            </el-form>

            <div class="login-button-class">
                <el-button type="success" @click="login">登录</el-button>
                <el-button type="danger" @click="register">注册</el-button>
            </div>
        </div>
    </div>
</template>

<script>
    import header from  "../components/header"
    export default {
        name: 'login',
        components: {
            "header-component": header,
        },
        props: {},
        data() {
            return {
                loginForm: {
                    name: "",
                    passWord: "",
                },
                rules: {
                    name: [
                        {required: true, message: '请输入用户名称', trigger: 'blur'},
                        {min: 1, max: 30, message: '长度在 1 到 30 个字符', trigger: 'blur'}
                    ],
                    passWord: [
                        {required: true, message: '请输入用户密码', trigger: 'blur'},
                        {min: 1, max: 30, message: '长度在 1 到 30 个字符', trigger: 'blur'}
                    ],
                },

        }
        },
        methods: {
            login() {
                this.$refs.loginFormRef.validate((valid) => {
                    if (valid) { // 代表校验通过
                    } else {  //校验失败
                        return false;
                    }
                });
            },
            register() {
                this.$refs.loginFormRef.validate((valid) => {
                    if (valid) { // 代表校验通过
                    } else {  //校验失败
                        return false;
                    }
                });
            }
        },
        created() {

        }
    }
</script>

<style scoped>

    .login-context {
        width: 400px;
        margin-left: auto;
        margin-right: auto;
        border-radius: 2px;
        border: 1px solid #a0b1c4;

        margin-top: 50px;

        padding: 10px 30px;
    }

    .login-button-class {
        display: flex;
        justify-content: space-between;
    }
</style>