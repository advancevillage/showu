<template>
    <div id="header">
        <nav class="level">
            <p class="level-item has-text-centered"></p>
            <p class="level-item has-text-centered"><b-icon pack="fas" icon="user" size="is-medium" type="is-success"></b-icon><a class="header_notice_text">{{noticeText}}</a></p>
            <p class="level-item has-text-centered"></p>
            <!-- Right side -->
            <div class="level-right">
                <p v-for="item in selectItems" :key='item.id' >
                    <a class="header_select_items" :href="item.url">{{item.value}}</a>
                </p>
            </div>
        </nav>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                noticeText: "Show You! More Confident And Beautiful",
                selectItems: [
                    {id: "country", url: "/", value: "CN"},
                    {id: "themes", url: "/", value: ""},
                ]
            }
        },
        name: "Header"
    }
</script>

<style scoped>
    #header {
        width: 100%;
        height: 45px;
        background: skyblue;
        z-index: 25;
    }
    .level-item {
        padding: 10px 0;
    }
    .header_notice_text {
        color: white;
        text-align: center;
        text-decoration: underline;
    }
    .header_select_items {
        color: white;
        text-align: center;
        margin: 0 10px;
    }
</style>