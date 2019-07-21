<template>
    <div class="hello">

        <my-component :data="value3"></my-component>

        <div>
            value1: {{value1}}
        </div>
        <div :class="value3">
            value2: <span v-html="value2"></span>
        </div>

        <div v-if="value4">
            value4-if: {{value4}}
        </div>
        <div v-show="value4">
            value4-show: {{value4}}
        </div>

        <ul>
            <li v-for="i in list1" :key="i">{{i}}</li>
        </ul>
        <ul>
            <li v-for="(i, index) in list1" :key="i">{{index}}: {{i}}</li>
        </ul>

        <ul>
            <li v-for="(value, key, index) in obj1" :key="index">{{index}}: {{key}}: {{value}}</li>
        </ul>

        <el-button v-on:click="clicka">默认按钮a</el-button>
        <el-button @click="clickb">默认按钮b</el-button>


        <input v-model="message" placeholder="">
        <el-button @click="clickc">默认按钮c</el-button>


        <input type="checkbox" id="checkbox" v-model="checked">

    </div>
</template>

<script>
    import myComponent from "./myComponent"

    export default {
        name: 'HelloWorld',
        components: {
            "my-component": myComponent,
        },
        props: {
            msg: String
        },
        data() {
            return {
                value1: "摩登",
                value2: "<h1>这是一个标题</h1>",
                value3: "value3_id",

                value4: false,

                list1: ["a", 'b', 'c', 'd'],
                obj1: {
                    a: "va",
                    b: "vb",
                    c: "vc",
                    d: "vd",
                },

                message: "m",

                checked: false,
            }
        },
        methods: {
            clicka(){
                alert("clicka")
            },
            clickb(){
                alert("clickb")
            },
            clickc(){
                this.message = "clickc";
            }
        },
        created() {

        },

        watch: {
            message:function () {
                console.log(this.message);
            },
            checked:function () {
                console.log(this.checked);
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
