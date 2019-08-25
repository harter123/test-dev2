<template>
    <div class="main-head">
        <div class="head-img">
            <img :src="vueImg" height="50px" width="50px"/>
            <span>接口测试系统</span>
        </div>
        <el-button size="small" @click="logout">注销</el-button>
    </div>
</template>

<script>
    import {logoutRequest} from "../requests/user";
    import img from "../assets/interface.png"

    export default {
        name: "header",
        data() {
            return {
                vueImg: img
            }
        },
        methods: {
            logout() {
                logoutRequest().then(data => {
                    this.$message.info("你已经退出登录");
                    this.$router.push("/login");
                }).catch(data => {
                    console.log(data);
                })
            }
        }
    }
</script>

<style scoped>
    .main-head {
        background: #eff4fa;
        height: 60px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 20px;
    }

    .head-img {
        display: flex;
        align-items: center;
    }
</style>