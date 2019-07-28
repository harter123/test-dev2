<template>
    <div class="main-head">
        <div class="head-img">
            <img :src="vueImg" height="50px" width="50px"/>
            <span>接口测试系统</span>
        </div>
    </div>
</template>

<script>
    import img from "../assets/interface.png"
    export default {
        name: "header",
        data(){
            return {
                vueImg: img
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