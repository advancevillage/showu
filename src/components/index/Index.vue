<template>
    <div>
        <Header/>
        <div id="container">
            <p>hello index</p>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import Header from '../common/Header'
    import Footer from '../common/Footer'

    export default {
        name: "Index",
        components: {
            Header,
            Footer
        }
    }
</script>

<style scoped>
    #container {
        min-height: 720px;
        min-width: 1024px;
        width: 100%;
        height: 100%;
    }
</style>