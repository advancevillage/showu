<template>
    <div>
        <Header/>
        <div id="container">
        </div>
        <Footer/>
    </div>
</template>

<script>
    import Header from '../common/Header'
    import Footer from '../common/Footer'

    export default {
        name: "Detail",
        components: {
            Header,
            Footer
        },
    }
</script>

<style scoped>

</style>