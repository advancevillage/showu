<template>
    <div>
        <!-- 通知栏 -->
        <nav class="level">
            <p class="level-item has-text-centered"></p>
            <p class="level-item has-text-centered"><a class="notice_text">{{noticeText}}</a></p>
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
        name: "Notice",
        data() {
            return {
                noticeText: "Show You! More Confident And Beautiful",
                selectItems: [
                    {id: "country", url: "/", value: "CN"},
                    {id: "themes", url: "/", value: ""},
                ],
            }
        }
    }
</script>

<style scoped>
    .notice_text {
        color: white;
        text-align: center;
        text-decoration: underline;
    }
</style>