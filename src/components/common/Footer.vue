<template>
    <div id="footer">
        <div class="footer_container_left">
            <div class="footer_container_left_item">

            </div>
            <div class="footer_container_left_item">

            </div>
            <div class="footer_container_left_item">

            </div>
            <div class="footer_container_left_item">

            </div>
        </div>
        <div class="footer_container_right">
            <div class="footer_container_right_item">

            </div>
            <div class="footer_container_right_item">

            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Footer"
    }
</script>

<style scoped>
    #footer {
        width: 100%;
        height: 300px;
        background-color: gray;
        z-index: 25;
    }
    .footer_container_left {
        border: 1px solid yellow;
        width: 75%;
        height: 300px;
        float: left;
    }
    .footer_container_right {
        border: 1px solid blue;
        width: 25%;
        height: 300px;
        float: left;
    }
    .footer_container_left_item {
        border:4px solid red;
        float: left;
        width: 25%;
        height: 300px;
    }
    .footer_container_right_item {
        border:4px solid blue;
        width: 100%;
        height: 50%;
    }
</style>