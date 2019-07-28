<template>
  <div class="home">
    <header-component></header-component>
  </div>
</template>

<script>
    import header from  "../components/header"
export default {
  name: 'home',
    components: {
        "header-component": header,
    },
}
</script>

<style scoped>

</style>
