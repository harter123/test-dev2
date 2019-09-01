<template>
    <div class="interface-main">
        <div class="service-tree-main">
            <el-tree :data="data" :props="defaultProps" @node-click="handleNodeClick"></el-tree>
        </div>
        <div class="interface-list-main">
            34
        </div>
    </div>
</template>

<script>
    export default {
        name: "index",
        data() {
            return {
                data: [],
                defaultProps: {
                    children: 'children',
                    label: 'label'
                }
            }
        },
        methods: {
            handleNodeClick(data) {
                console.log(data);
            }
        },
        created() {

        }
    }
</script>

<style scoped>
    .interface-main {
        display: flex;
        padding-top: 10px;
    }

    .service-tree-main {
        width: 25%;
    }

    .interface-list-main {
        width: 75%;
    }
</style>