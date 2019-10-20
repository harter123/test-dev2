<template>
    <div class="main-head">
        <div class="menu-head">
            <div class="head-img">
                <img :src="vueImg" height="50px" width="50px"/>
                <span>接口测试系统</span>
            </div>
            <el-menu v-if="isShowMenu" background-color="#eff4fa" :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
                <el-menu-item index="interface">接口</el-menu-item>
                <el-menu-item index="task">任务</el-menu-item>
                <el-menu-item index="debug">调试</el-menu-item>
                <el-menu-item index="mock">mock</el-menu-item>
            </el-menu>

        </div>
        <el-button v-if="isShowLogout" size="small" @click="logout">注销</el-button>
    </div>
</template>

<script>
    import {logoutRequest} from "../requests/user";
    import img from "../assets/interface.png"

    export default {
        name: "header",
        props: {
            isShowLogout: {
                type: Boolean,
                default: false,
            },
            isShowMenu: {
                type: Boolean,
                default: false,
            }
        },
        data() {
            return {
                vueImg: img,
                activeIndex: "interface",
            }
        },
        methods: {
            handleSelect(key, keyPath) {
                this.$emit('selectItem', key)
            },
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
    .menu-head {
        display: flex;
    }
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
        margin-right: 30px;
    }
</style>