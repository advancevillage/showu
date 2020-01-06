<template>
    <div>
        <Header/>
        <div id="container">
            <div class="container_warp">
                <div class="list_banner">
                    <Banner/>
                </div>
                <div class="list_warp">
                    <div class="list_warp_filter">
                        <Filters/>
                    </div>
                    <div class="list_warp_items">
                        <Items/>
                    </div>
                </div>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import Header  from '../common/Header'
    import Footer  from '../common/Footer'
    import Banner  from './Banner'
    import Filters from './Filters'
    import Items   from './Items'


    export default {
        name: "List",
        components: {
            Header,
            Footer,
            Banner,
            Filters,
            Items
        },
    }
</script>

<style scoped>
    .container_warp {
        width: 100%;
        padding: 60px 2% 0;
    }
    .list_banner {
        width: 100%;
        height: 20%;
    }
    .list_warp {
        min-height: 1024px;
        width: 100%;
        height: 80%;
        margin: 2% 0;
    }
    .list_warp_filter {
        float: left;
        width: 20%;
        height: 100%;
    }
    .list_warp_items {
        float: left;
        width: 80%;
        height: 100%;
    }
</style>