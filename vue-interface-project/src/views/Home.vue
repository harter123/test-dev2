<template>
    <div class="home">
        <header-component @selectItem="selectItem" :isShowLogout="true" :isShowMenu="true"></header-component>
        <interface-index v-if="menuItem === 'interface'"></interface-index>
        <mock-index v-if="menuItem === 'mock'"></mock-index>
    </div>
</template>

<script>
    import {getUserInfoRequest} from "../requests/user";
    import header from "../components/header"
    import interfaceIndex from "./interface/index"
    import mockIndex from "./mock/list"

    export default {
        name: 'home',
        components: {
            "header-component": header,
            "interface-index": interfaceIndex,
            'mock-index': mockIndex,
        },
        data() {
            return {
                menuItem: 'interface',
            }
        },
        methods: {
            selectItem(key) {
                this.menuItem = key;
            },
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
