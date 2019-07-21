<template>
    <div>
        这是我的第一个组件, hahahah
    </div>
</template>

<script>
    export default {
        name: "myComponent",
        components:{},
        props: {
            data: {},
        },
        data(){
            return {}
        },
        methods: {

        },
        created(){
            console.log(this.data);
        }
    }
</script>

<style scoped>

</style>