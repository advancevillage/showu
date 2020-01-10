<template>
    <div id="header">
        <!--通知栏-->
        <div class="notice">
            <Notice/>
        </div>
        <!-- 菜单页 -->
        <div class="menu">
            <Menu/>
        </div>
    </div>
</template>

<script>
    import  Notice from './header/Notice'
    import  Menu   from './header/Menu'

    export default {
        name: "Header",
        components: {
            Notice,
            Menu
        },
    }
</script>

<style scoped>
    #header {
        width: 100%;
        height: 45px;
        background: black;
        z-index: 25;
    }
    /* 通知栏 */
    .notice {
        width: 100%;
        height: 45px;
        padding: 10px 2%;
    }
    /* 菜单栏 */
    .menu {
        position: absolute;
        width: 100%;
        height: 45px;
        margin: 0;
        padding: 0;
    }
</style>