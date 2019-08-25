<template>
    <div class="home">
        <header-component></header-component>
    </div>
</template>

<script>
    import {getUserInfoRequest} from "../requests/user";
    import header from "../components/header"

    export default {
        name: 'home',
        components: {
            "header-component": header,
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
