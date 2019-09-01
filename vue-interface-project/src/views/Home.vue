<template>
    <div class="home">
        <header-component :isShowLogout="true" :isShowMenu="true"></header-component>
        <interface-index></interface-index>
    </div>
</template>

<script>
    import {getUserInfoRequest} from "../requests/user";
    import header from "../components/header"
    import interfaceIndex from "./interface/index"

    export default {
        name: 'home',
        components: {
            "header-component": header,
            "interface-index": interfaceIndex,
        },
        methods: {
            tellIfUserIsLogin() {
                getUserInfoRequest().then(data => {
                    if (false === data.data.success) {
                        this.$router.push("/login");
                    }
                }).catch(data => {
                    console.log(data);
                })
            },
        },
        created() {
            this.tellIfUserIsLogin();
        },
    }
</script>

<style scoped>

</style>
